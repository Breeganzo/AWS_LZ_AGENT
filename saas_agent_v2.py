#!/usr/bin/env python3
"""
AWS SaaS Architecture Agent v2
==============================
Specialized agent for designing SaaS hosting architectures with compliance validation
and detailed AWS stencil-based draw.io diagrams with proper hierarchy.

Features:
- GDPR compliance validation with EU region checking
- Detailed environment-specific AWS service diagrams with proper connections
- Comprehensive guardrails and validation
- Professional draw.io output with correct AWS stencils and proper application distribution
"""

import questionary
import os
from datetime import datetime
from typing import Dict, List, Tuple, Any
import html

def escape_xml(text: str) -> str:
    """
    Escape XML special characters to prevent parsing errors.
    
    Args:
        text: Text to escape
    
    Returns:
        XML-safe text
    """
    # Use html.escape which handles &, <, > and can handle quotes
    return html.escape(text, quote=False)

def validate_gdpr_region(compliance_choices: List[str], region: str) -> Tuple[List[str], str]:
    """
    Validate GDPR compliance against region and provide fallback options.
    
    Args:
        compliance_choices: List of selected compliance requirements
        region: Selected region/country
    
    Returns:
        Tuple of (validated_compliance_choices, validated_region)
    """
    gdpr_selected = any('GDPR' in choice for choice in compliance_choices)
    eu_regions = ['eu', 'europe', 'european union', 'germany', 'france', 'italy', 'spain', 'netherlands', 'belgium', 'poland', 'ireland']
    
    if gdpr_selected:
        # Check if region is EU
        is_eu_region = any(eu_region in region.lower() for eu_region in eu_regions)
        
        if not is_eu_region:
            print(f"\n⚠️  GDPR Compliance Alert!")
            print(f"You selected GDPR compliance but your region is '{region}'.")
            print(f"GDPR (General Data Protection Regulation) only applies to EU regions.")
            
            gdpr_choice = questionary.select(
                "What would you like to do?",
                choices=[
                    "Change region to EU",
                    "Remove GDPR and select different compliance",
                    "I'm not sure - help me choose"
                ]
            ).ask()
            
            if gdpr_choice == "Change region to EU":
                new_region = questionary.select(
                    "Select your EU region:",
                    choices=[
                        "EU (General)",
                        "Germany",
                        "France", 
                        "Ireland",
                        "Netherlands",
                        "Other EU country"
                    ]
                ).ask()
                region = new_region.lower()
                
            elif gdpr_choice == "Remove GDPR and select different compliance":
                # Remove GDPR from compliance choices
                compliance_choices = [choice for choice in compliance_choices if 'GDPR' not in choice]
                
                print(f"\nSince you're in '{region}', here are relevant compliance options:")
                
                # Suggest region-appropriate compliance
                if region.lower() in ['us', 'usa', 'united states']:
                    suggested_compliance = questionary.checkbox(
                        "Select appropriate compliance for US:",
                        choices=[
                            "HIPAA (Healthcare)",
                            "SOX (Financial)",
                            "FedRAMP (Government)",
                            "SOC 2 (General)",
                            "None"
                        ]
                    ).ask()
                else:
                    suggested_compliance = questionary.checkbox(
                        "Select appropriate compliance:",
                        choices=[
                            "ISO 27001",
                            "SOC 2",
                            "PCI DSS (Payment processing)",
                            "Industry-specific requirements",
                            "None"
                        ]
                    ).ask()
                
                compliance_choices.extend(suggested_compliance)
                
            else:  # "I'm not sure - help me choose"
                print(f"\n📋 Compliance Guidance for '{region}':")
                
                if region.lower() in ['us', 'usa', 'united states']:
                    print("🇺🇸 For US-based SaaS:")
                    print("• HIPAA - if handling healthcare data")
                    print("• SOX - if serving financial institutions")
                    print("• FedRAMP - if serving government clients")
                    print("• SOC 2 - general security and privacy controls")
                elif any(eu_region in region.lower() for eu_region in eu_regions):
                    print("🇪🇺 For EU-based SaaS:")
                    print("• GDPR - mandatory for personal data processing")
                    print("• ISO 27001 - international security standard")
                else:
                    print("🌍 For international SaaS:")
                    print("• ISO 27001 - widely recognized security standard")
                    print("• SOC 2 - for US customer trust")
                    print("• Local data protection laws")
                
                # Re-ask for compliance after guidance
                compliance_choices = questionary.checkbox(
                    "Select compliance requirements after reviewing guidance:",
                    choices=[
                        "GDPR (EU only)",
                        "HIPAA (US Healthcare)",
                        "SOX (Financial)",
                        "FedRAMP (US Government)",
                        "SOC 2",
                        "ISO 27001",
                        "PCI DSS",
                        "None"
                    ]
                ).ask()
                
                # Validate again recursively
                return validate_gdpr_region(compliance_choices, region)
    
    return compliance_choices, region

def get_saas_requirements() -> Dict[str, Any]:
    """
    Collect SaaS hosting requirements with validation and guardrails.
    
    Returns:
        Dictionary containing all SaaS requirements
    """
    print("🚀 AWS SaaS Architecture Agent v2")
    print("=" * 52)
    print("This agent will design a comprehensive SaaS hosting architecture")
    print("with proper compliance validation and detailed AWS diagrams.\n")
    
    # Number of applications
    num_apps = questionary.text(
        "How many SaaS applications will you host?",
        validate=lambda x: x.isdigit() and int(x) > 0 and int(x) <= 100
    ).ask()
    
    # Application types
    app_type = questionary.select(
        "What type of applications are you hosting?",
        choices=[
            "Microservices with container orchestration",
            "Monolithic applications", 
            "Serverless applications",
            "Mixed architecture (containers + serverless)",
            "Legacy applications requiring VMs"
        ]
    ).ask()
    
    # Environments
    environments = questionary.select(
        "How many environments do you need?",
        choices=[
            "3 (Dev, QA, Prod)",
            "4 (Dev, QA, Pre-Prod, Prod)",
            "5 (Dev, QA, UAT, Pre-Prod, Prod)",
            "6+ (Enterprise with multiple testing stages)"
        ]
    ).ask()
    
    # Primary region
    region = questionary.text(
        "What is your primary region/country? (e.g., US, EU, APAC, Germany, Ireland):"
    ).ask()
    
    # Compliance requirements
    compliance = questionary.checkbox(
        "Select compliance requirements:",
        choices=[
            "GDPR (EU Data Protection)",
            "HIPAA (US Healthcare)",
            "SOX (Financial)",
            "FedRAMP (US Government)",
            "SOC 2 (Security & Privacy)",
            "ISO 27001 (Security Management)",
            "PCI DSS (Payment Processing)",
            "None"
        ]
    ).ask()
    
    # Validate GDPR region compatibility
    compliance, region = validate_gdpr_region(compliance, region)
    
    # Data residency requirements
    data_residency = questionary.select(
        "Data residency requirements:",
        choices=[
            "Data must stay in selected region",
            "Data can be replicated to other regions",
            "Global data distribution allowed",
            "Not applicable"
        ]
    ).ask()
    
    # Security level
    security_level = questionary.select(
        "What is your required security level?",
        choices=[
            "Standard (Basic security controls)",
            "High (Enhanced monitoring and controls)",
            "Critical (Maximum security, dedicated resources)"
        ]
    ).ask()
    
    # Multi-tenancy model
    tenancy_model = questionary.select(
        "What is your multi-tenancy model?",
        choices=[
            "Single-tenant (Dedicated resources per customer)",
            "Multi-tenant shared (Shared infrastructure)",
            "Hybrid (Mix of shared and dedicated)",
            "Configurable per customer"
        ]
    ).ask()
    
    return {
        'num_apps': int(num_apps),
        'app_type': app_type,
        'environments': environments,
        'region': region,
        'compliance': compliance,
        'data_residency': data_residency,
        'security_level': security_level,
        'tenancy_model': tenancy_model
    }

def generate_detailed_saas_diagram(requirements: Dict[str, Any]) -> str:
    """
    Generate a detailed SaaS architecture diagram with hierarchical structure like the reference image.
    Shows clear organizational structure with connections between components.
    
    Args:
        requirements: Dictionary containing SaaS requirements
    
    Returns:
        Path to the generated diagram file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    region_suffix = requirements['region'].lower().replace(' ', '_')
    filename = f"saas_hierarchical_{requirements['num_apps']}apps_{region_suffix}_{timestamp}.drawio"
    filepath = os.path.join("images", filename)
    
    # Ensure images directory exists
    os.makedirs("images", exist_ok=True)
    
    # Parse environments
    env_text = requirements['environments']
    if "3 (" in env_text:
        environments = ["Dev", "QA", "Prod"]
    elif "4 (" in env_text:
        environments = ["Dev", "QA", "Pre-Prod", "Prod"]
    elif "5 (" in env_text:
        environments = ["Dev", "QA", "UAT", "Pre-Prod", "Prod"]
    else:
        environments = ["Dev", "QA", "Performance", "UAT", "Pre-Prod", "Prod"]
    
    # Determine production and non-production environments
    prod_envs = [env for env in environments if 'Prod' in env]
    nonprod_envs = [env for env in environments if 'Prod' not in env]
    
    # Generate title with proper XML escaping
    compliance_text = ', '.join(requirements['compliance']) if requirements['compliance'] else 'None'
    title_text = f"Requirement: Hosting {requirements['num_apps']} SaaS applications in {len(environments)} different environments\\nAssumption: {requirements['app_type']} and PaaS DB"
    title_text = escape_xml(title_text)
    
    # Start building the draw.io XML with hierarchical structure
    xml_content = f'''<mxfile host="app.diagrams.net" modified="2024-09-19T00:00:00.000Z" agent="5.0" etag="abc" version="24.1.0">
  <diagram id="saas-hierarchical" name="SaaS Hierarchical Architecture">
    <mxGraphModel dx="2000" dy="1500" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title Box -->
        <mxCell id="2" value="{title_text}" style="text;html=1;align=right;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=10;fillColor=#f8f9fa;strokeColor=#dee2e6;" vertex="1" parent="1">
          <mxGeometry x="1050" y="50" width="320" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Root SaaS Apps -->
        <mxCell id="3" value="SaaS Apps" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/aws4/ManagementGovernance/AWS_Organizations.svg;" vertex="1" parent="1">
          <mxGeometry x="650" y="150" width="60" height="60" as="geometry"/>
        </mxCell>'''
    
    cell_id = 4
    
    # Non-Production OU
    xml_content += f'''
        
        <!-- Non-Prod OU -->
        <mxCell id="{cell_id}" value="Non-Prod" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#cfe2ff;strokeColor=#0d6efd;verticalAlign=top;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="100" y="280" width="{len(nonprod_envs) * 180 + 40}" height="400" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Production OU
    xml_content += f'''
        
        <!-- Prod OU -->
        <mxCell id="{cell_id}" value="Prod" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1e7dd;strokeColor=#0f5132;verticalAlign=top;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{200 + len(nonprod_envs) * 180}" y="280" width="{len(prod_envs) * 180 + 40}" height="400" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    # Non-Production OU Account Icons and Connections
    nonprod_account_ids = []
    for i, env in enumerate(nonprod_envs):
        account_x = 180 + (i * 180)
        account_y = 240
        
        # Account Icon above Non-Prod OU
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/aws4/ManagementGovernance/AWS_Organizations.svg;" vertex="1" parent="1">
          <mxGeometry x="{account_x}" y="{account_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
        nonprod_account_ids.append(cell_id)
        cell_id += 1
        
        # Connection from SaaS Apps to Account
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.25;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="3" target="{nonprod_account_ids[-1]}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="650" y="220" as="sourcePoint"/>
            <mxPoint x="{account_x + 20}" y="240" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
        cell_id += 1
        
        # Yellow connection box
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffc107;strokeColor=#ffc107;" vertex="1" parent="1">
          <mxGeometry x="{account_x + 10}" y="285" width="20" height="15" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Environment Label
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{account_x - 10}" y="310" width="60" height="20" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Environment containers within Non-Prod OU
        env_container_y = 340
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e3f2fd;strokeColor=#1976d2;verticalAlign=top;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{account_x - 20}" y="{env_container_y}" width="80" height="300" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Determine cluster type based on tenancy model
        if "Single-tenant" in requirements['tenancy_model']:
            cluster_types = ["Dedicated\\nCluster\\nVNET", "Dedicated\\nPaaS\\nVNET"]
        else:
            cluster_types = ["Shared\\nCluster\\nVNET", "Shared\\nPaaS\\nVNET"]
        
        # Add clusters for each application
        apps_to_show = min(requirements['num_apps'], 2)  # Show up to 2 apps per environment
        for app_idx in range(apps_to_show):
            cluster_y = env_container_y + 40 + (app_idx * 120)
            xml_content += f'''
        <mxCell id="{cell_id}" value="{cluster_types[app_idx % 2]}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3cd;strokeColor=#856404;fontSize=9;align=center;" vertex="1" parent="1">
          <mxGeometry x="{account_x - 15}" y="{cluster_y}" width="70" height="80" as="geometry"/>
        </mxCell>'''
            cell_id += 1
    
    # Production OU Account Icons and Connections
    prod_account_ids = []
    for i, env in enumerate(prod_envs):
        account_x = 400 + len(nonprod_envs) * 180 + (i * 240)
        account_y = 240
        
        # Account Icon above Prod OU
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/aws4/ManagementGovernance/AWS_Organizations.svg;" vertex="1" parent="1">
          <mxGeometry x="{account_x}" y="{account_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
        prod_account_ids.append(cell_id)
        cell_id += 1
        
        # Connection from SaaS Apps to Account
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.75;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="3" target="{prod_account_ids[-1]}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="700" y="220" as="sourcePoint"/>
            <mxPoint x="{account_x + 20}" y="240" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
        cell_id += 1
        
        # Yellow connection box
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffc107;strokeColor=#ffc107;" vertex="1" parent="1">
          <mxGeometry x="{account_x + 10}" y="285" width="20" height="15" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Environment Label
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{account_x - 20}" y="310" width="80" height="20" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Environment containers within Prod OU
        env_container_y = 340
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env} App{requirements['num_apps']}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#2e7d32;verticalAlign=top;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{account_x - 30}" y="{env_container_y}" width="120" height="280" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Production clusters (typically dedicated for better performance)
        prod_cluster_types = ["Dedicated\\nCluster\\nVNET", "Dedicated\\nPaaS\\nVNET"]
        
        # Show production clusters
        for cluster_idx in range(2):
            cluster_y = env_container_y + 40 + (cluster_idx * 100)
            xml_content += f'''
        <mxCell id="{cell_id}" value="{prod_cluster_types[cluster_idx]}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d4edda;strokeColor=#155724;fontSize=9;align=center;" vertex="1" parent="1">
          <mxGeometry x="{account_x - 20}" y="{cluster_y}" width="100" height="70" as="geometry"/>
        </mxCell>'''
            cell_id += 1
    
    # Add Control Tower to manage all accounts
    xml_content += f'''
        <mxCell id="{cell_id}" value="AWS Control Tower" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/aws4/ManagementGovernance/AWS_Control_Tower.svg;" vertex="1" parent="1">
          <mxGeometry x="750" y="130" width="60" height="60" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Add connections from Control Tower to all accounts
    for account_id in nonprod_account_ids + prod_account_ids:
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;dashed=1;strokeColor=#666666;" edge="1" parent="1" source="{cell_id - len(nonprod_account_ids + prod_account_ids) - 1}" target="{account_id}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="780" y="200" as="sourcePoint"/>
            <mxPoint x="400" y="250" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
        cell_id += 1

    # Close the XML
    xml_content += '''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    return filepath

def provide_saas_recommendations(requirements: Dict[str, Any]) -> None:
    """
    Provide detailed SaaS architecture recommendations based on requirements.
    
    Args:
        requirements: Dictionary containing SaaS requirements
    """
    print("\n" + "=" * 70)
    print("=== SaaS ARCHITECTURE RECOMMENDATIONS ===")
    print(f"Applications: {requirements['num_apps']}")
    print(f"Environments: {requirements['environments']}")
    print(f"Application Type: {requirements['app_type']}")
    print(f"Compliance: {', '.join(requirements['compliance']) if requirements['compliance'] else 'None'}")
    print(f"Region: {requirements['region']}")
    print(f"Security Level: {requirements['security_level']}")
    print(f"Tenancy Model: {requirements['tenancy_model']}")
    print(f"Data Residency: {requirements['data_residency']}")
    
    print("\n🏗️  ARCHITECTURE RECOMMENDATIONS:")
    print("• Use AWS Control Tower for centralized governance")
    print("• Implement separate OUs for Non-Prod and Prod environments")
    print("• Use Infrastructure as Code (CloudFormation/Terraform)")
    print(f"• Deploy {requirements['num_apps']} applications across {len(requirements['environments'].split('(')[0].strip())} environments")
    
    # Application-specific recommendations
    if "container" in requirements['app_type'].lower():
        print("• Deploy applications using Amazon ECS or EKS")
        print("• Use AWS Fargate for serverless container management")
        print("• Implement container image scanning with ECR")
    elif "serverless" in requirements['app_type'].lower():
        print("• Use AWS Lambda for application logic")
        print("• Implement API Gateway for REST APIs")
        print("• Use DynamoDB for NoSQL data storage")
    elif "mixed" in requirements['app_type'].lower():
        print("• Use ECS/Fargate for containerized components")
        print("• Use Lambda for event-driven serverless components")
        print("• Implement proper service mesh for communication")
    
    # Security recommendations based on level
    if requirements['security_level'] == "Critical":
        print("• Use dedicated tenancy for sensitive workloads")
        print("• Implement network segmentation with VPC")
        print("• Enable AWS Config for compliance monitoring")
        print("• Use AWS Security Hub for centralized security")
    
    # Compliance-specific recommendations
    if any('GDPR' in comp for comp in requirements['compliance']):
        print("• Implement data encryption at rest and in transit")
        print("• Use AWS CloudTrail for audit logging")
        print("• Implement data retention and deletion policies")
        print("• Use AWS Macie for data discovery and classification")
    
    if any('HIPAA' in comp for comp in requirements['compliance']):
        print("• Use HIPAA-eligible AWS services only")
        print("• Implement access logging and monitoring")
        print("• Use AWS KMS for encryption key management")
    
    # Multi-tenancy recommendations
    if requirements['tenancy_model'] == "Single-tenant":
        print("• Provision dedicated AWS accounts per customer")
        print("• Use AWS Organizations for account management")
    elif "Multi-tenant" in requirements['tenancy_model']:
        print("• Implement tenant isolation at application level")
        print("• Use database schemas or separate databases per tenant")
        print("• Implement tenant-aware monitoring and billing")

def main():
    """Main function to run the SaaS architecture agent v2."""
    try:
        # Get requirements with validation
        requirements = get_saas_requirements()
        
        # Provide recommendations
        provide_saas_recommendations(requirements)
        
        # Generate detailed diagram
        print("\n🎨 Generating detailed SaaS architecture diagram with proper hierarchy...")
        diagram_path = generate_detailed_saas_diagram(requirements)
        print(f"✅ Detailed architecture diagram generated successfully!")
        print(f"📁 Location: {diagram_path}")
        print(f"📊 Shows all {requirements['num_apps']} applications distributed across environments")
        
        print("\n" + "=" * 70)
        print("🛠️  NEXT STEPS FOR SAAS IMPLEMENTATION:")
        print("1. Review the generated detailed architecture diagram")
        print("2. Set up AWS Control Tower with proper OUs")
        print("3. Create infrastructure templates (CloudFormation/Terraform)")
        print("4. Implement CI/CD pipelines for each environment")
        print("5. Set up monitoring and alerting across all environments")
        print("6. Implement security controls and compliance measures")
        print("7. Configure auto-scaling and load balancing")
        print("8. Set up backup and disaster recovery procedures")
        print("9. Implement tenant onboarding and management processes")
        print("10. Test the architecture with sample applications")
        
        return diagram_path
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return None
    except Exception as e:
        print(f"\nError: {e}")
        return None

if __name__ == "__main__":
    main()