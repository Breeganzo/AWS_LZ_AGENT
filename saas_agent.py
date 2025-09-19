#!/usr/bin/env python3
"""
AWS SaaS Architecture Agent
===========================
Specialized agent for designing SaaS hosting architectures with compliance validation
and detailed AWS stencil-based draw.io diagrams.

Features:
- GDPR compliance validation with EU region checking
- Detailed environment-specific AWS service diagrams
- Comprehensive guardrails and validation
- Professional draw.io output with proper AWS stencils
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
    print("🚀 AWS SaaS Architecture Agent")
    print("=" * 50)
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
    Generate a detailed SaaS architecture diagram with proper AWS stencils and hierarchy.
    
    Args:
        requirements: Dictionary containing SaaS requirements
    
    Returns:
        Path to the generated diagram file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    region_suffix = requirements['region'].lower().replace(' ', '_')
    filename = f"saas_detailed_{requirements['num_apps']}apps_{region_suffix}_{timestamp}.drawio"
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
        environments = ["Dev", "QA", "UAT", "Staging", "Pre-Prod", "Prod"]
    
    # Determine production and non-production environments
    prod_envs = [env for env in environments if 'Prod' in env]
    nonprod_envs = [env for env in environments if 'Prod' not in env]
    
    # Calculate application distribution across environments
    num_apps = requirements['num_apps']
    
    # Generate title with proper XML escaping
    compliance_text = ', '.join(requirements['compliance']) if requirements['compliance'] else 'None'
    title_text = f"SaaS Architecture: {requirements['num_apps']} Apps | {requirements['environments']}&#xa;Region: {requirements['region']} | Compliance: {compliance_text}&#xa;Security: {requirements['security_level']} | Tenancy: {requirements['tenancy_model']}"
    title_text = escape_xml(title_text)
    # Start building the draw.io XML
    xml_content = f'''<mxfile host="app.diagrams.net" modified="2024-09-19T00:00:00.000Z" agent="5.0" etag="abc" version="24.1.0">
  <diagram id="saas-detailed" name="SaaS Detailed Architecture">
    <mxGraphModel dx="2500" dy="2000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title and Requirements -->
        <mxCell id="2" value="{title_text}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="800" height="60" as="geometry"/>
        </mxCell>
        
        <!-- AWS Control Tower -->
        <mxCell id="3" value="AWS Control Tower" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/mscae/Management_Groups.svg;" vertex="1" parent="1">
          <mxGeometry x="425" y="100" width="50" height="40" as="geometry"/>
        </mxCell>'''
    
    cell_id = 4
    y_offset = 180
    
    # Generate Non-Production OU
    if nonprod_envs:
        nonprod_width = len(nonprod_envs) * 200 + 100
        xml_content += f'''
        
        <!-- Non-Production OU -->
        <mxCell id="{cell_id}" value="Non-Production Environments" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;verticalAlign=top;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="{y_offset}" width="{nonprod_width}" height="400" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Generate each non-prod environment with detailed AWS services
        x_start = 80
        for i, env in enumerate(nonprod_envs):
            env_x = x_start + (i * 200)
            
            # Environment container
            xml_content += f'''
        
        <!-- {env} Environment -->
        <mxCell id="{cell_id}" value="{env}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8f9fa;strokeColor=#dee2e6;verticalAlign=top;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{y_offset + 40}" width="180" height="340" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # AWS Services in this environment
            service_y = y_offset + 70
            
            # ECS/EKS for container orchestration
            if "container" in requirements['app_type'].lower():
                xml_content += f'''
        <mxCell id="{cell_id}" value="ECS/EKS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Compute/Amazon_Elastic_Container_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 20}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
                cell_id += 1
                service_y += 60
            
            # Application Load Balancer
            xml_content += f'''
        <mxCell id="{cell_id}" value="ALB" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/NetworkingContentDelivery/Elastic_Load_Balancing.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 80}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # RDS Database
            xml_content += f'''
        <mxCell id="{cell_id}" value="RDS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Database/Amazon_RDS.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 140}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            service_y += 60
            
            # ElastiCache
            xml_content += f'''
        <mxCell id="{cell_id}" value="ElastiCache" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Database/Amazon_ElastiCache.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 20}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # CloudWatch
            xml_content += f'''
        <mxCell id="{cell_id}" value="CloudWatch" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/ManagementGovernance/Amazon_CloudWatch.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 80}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # S3 for static assets
            xml_content += f'''
        <mxCell id="{cell_id}" value="S3" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Storage/Amazon_Simple_Storage_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 140}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            service_y += 60
            
            # VPC
            xml_content += f'''
        <mxCell id="{cell_id}" value="VPC" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/NetworkingContentDelivery/Amazon_VPC.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 50}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            service_y += 60
            
            # Application instances (based on number of apps)
            apps_per_env = min(requirements['num_apps'], 3)  # Show max 3 apps per env for clarity
            for app_idx in range(apps_per_env):
                app_x = env_x + 20 + (app_idx * 50)
                xml_content += f'''
        <mxCell id="{cell_id}" value="App{app_idx + 1}" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Compute/Amazon_EC2.svg;" vertex="1" parent="1">
          <mxGeometry x="{app_x}" y="{service_y}" width="30" height="30" as="geometry"/>
        </mxCell>'''
                cell_id += 1
    
    # Generate Production OU
    if prod_envs:
        prod_y_offset = y_offset + 450
        prod_width = len(prod_envs) * 300 + 100
        xml_content += f'''
        
        <!-- Production OU -->
        <mxCell id="{cell_id}" value="Production Environments" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;verticalAlign=top;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="{prod_y_offset}" width="{prod_width}" height="450" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Generate each prod environment with enhanced AWS services
        x_start = 80
        for i, env in enumerate(prod_envs):
            env_x = x_start + (i * 300)
            
            # Environment container
            xml_content += f'''
        
        <!-- {env} Environment -->
        <mxCell id="{cell_id}" value="{env}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8f9fa;strokeColor=#dee2e6;verticalAlign=top;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{prod_y_offset + 40}" width="280" height="390" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # AWS Services in production environment (more comprehensive)
            service_y = prod_y_offset + 70
            
            # Auto Scaling Group
            xml_content += f'''
        <mxCell id="{cell_id}" value="Auto Scaling" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Compute/Amazon_EC2_Auto_Scaling.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 20}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # Application Load Balancer
            xml_content += f'''
        <mxCell id="{cell_id}" value="ALB" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/NetworkingContentDelivery/Elastic_Load_Balancing.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 80}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # ECS/EKS for container orchestration
            if "container" in requirements['app_type'].lower():
                xml_content += f'''
        <mxCell id="{cell_id}" value="ECS/EKS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Compute/Amazon_Elastic_Container_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 140}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
                cell_id += 1
            
            # CloudFront CDN
            xml_content += f'''
        <mxCell id="{cell_id}" value="CloudFront" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/NetworkingContentDelivery/Amazon_CloudFront.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 200}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            service_y += 60
            
            # RDS with Multi-AZ
            xml_content += f'''
        <mxCell id="{cell_id}" value="RDS Multi-AZ" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Database/Amazon_RDS.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 20}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # ElastiCache Cluster
            xml_content += f'''
        <mxCell id="{cell_id}" value="ElastiCache" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Database/Amazon_ElastiCache.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 80}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # S3 with versioning
            xml_content += f'''
        <mxCell id="{cell_id}" value="S3" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/Storage/Amazon_Simple_Storage_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 140}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # WAF
            xml_content += f'''
        <mxCell id="{cell_id}" value="WAF" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/SecurityIdentityCompliance/AWS_WAF.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 200}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            service_y += 60
            
            # CloudWatch with enhanced monitoring
            xml_content += f'''
        <mxCell id="{cell_id}" value="CloudWatch" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/ManagementGovernance/Amazon_CloudWatch.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 20}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # AWS Secrets Manager
            xml_content += f'''
        <mxCell id="{cell_id}" value="Secrets Mgr" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/SecurityIdentityCompliance/AWS_Secrets_Manager.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 80}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # KMS for encryption
            xml_content += f'''
        <mxCell id="{cell_id}" value="KMS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/SecurityIdentityCompliance/AWS_Key_Management_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 140}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # GuardDuty
            xml_content += f'''
        <mxCell id="{cell_id}" value="GuardDuty" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/SecurityIdentityCompliance/Amazon_GuardDuty.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 200}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            service_y += 60
            
            # VPC with multiple AZs
            xml_content += f'''
        <mxCell id="{cell_id}" value="VPC Multi-AZ" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=10;image=img/lib/aws4/NetworkingContentDelivery/Amazon_VPC.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 80}" y="{service_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            service_y += 60
            
            # Application instances (showing scalability)
            apps_per_env = min(requirements['num_apps'], 4)  # Show max 4 apps in prod
            for app_idx in range(apps_per_env):
                app_x = env_x + 20 + (app_idx * 60)
                xml_content += f'''
        <mxCell id="{cell_id}" value="App{app_idx + 1}" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Compute/Amazon_EC2.svg;" vertex="1" parent="1">
          <mxGeometry x="{app_x}" y="{service_y}" width="30" height="30" as="geometry"/>
        </mxCell>'''
                cell_id += 1
    
    # Add compliance and security controls section
    compliance_y = prod_y_offset + 500 if prod_envs else y_offset + 450
    xml_content += f'''
        
        <!-- Compliance and Security Controls -->
        <mxCell id="{cell_id}" value="Compliance &amp; Security Controls" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;verticalAlign=top;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="{compliance_y}" width="800" height="120" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Add specific compliance controls based on requirements
    control_x = 80
    for compliance_req in requirements['compliance']:
        if compliance_req != 'None':
            xml_content += f'''
        <mxCell id="{cell_id}" value="{compliance_req}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="{control_x}" y="{compliance_y + 40}" width="100" height="30" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            control_x += 120
    
    # Add connections from Control Tower to environments
    connection_y = 150
    for i, env in enumerate(nonprod_envs + prod_envs):
        env_x = 80 + (i * 200) if env in nonprod_envs else 80 + ((len(nonprod_envs) + prod_envs.index(env)) * 200)
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="3" target="{4 + i}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="450" y="200" as="sourcePoint"/>
            <mxPoint x="500" y="150" as="targetPoint"/>
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
    
    # Application-specific recommendations
    if "container" in requirements['app_type'].lower():
        print("• Deploy applications using Amazon ECS or EKS")
        print("• Use AWS Fargate for serverless container management")
        print("• Implement container image scanning with ECR")
    elif "serverless" in requirements['app_type'].lower():
        print("• Use AWS Lambda for application logic")
        print("• Implement API Gateway for REST APIs")
        print("• Use DynamoDB for NoSQL data storage")
    
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
    """Main function to run the SaaS architecture agent."""
    try:
        # Get requirements with validation
        requirements = get_saas_requirements()
        
        # Provide recommendations
        provide_saas_recommendations(requirements)
        
        # Generate detailed diagram
        print("\n🎨 Generating detailed SaaS architecture diagram...")
        diagram_path = generate_detailed_saas_diagram(requirements)
        print(f"✅ Detailed architecture diagram generated successfully!")
        print(f"📁 Location: {diagram_path}")
        
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