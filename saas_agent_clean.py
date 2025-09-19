#!/usr/bin/env python3
"""
AWS SaaS Architecture Agent v3 - Clean Layout
This agent generates clean, well-spaced SaaS architecture diagrams similar to the LZ brainstorming style.
Supports multi-page layouts for large numbers of applications.
"""

import os
import questionary
from datetime import datetime
from typing import Dict, Any, List

def get_saas_requirements() -> Dict[str, Any]:
    """Collect SaaS architecture requirements from the user."""
    print("🚀 AWS SaaS Architecture Agent v3 - Clean Layout")
    print("=" * 60)
    print("This agent will design a comprehensive SaaS hosting architecture")
    print("with clean layout and multi-page support for large applications.")
    print()
    
    num_apps = questionary.select(
        "How many SaaS applications will you host?",
        choices=[
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
            "15", "20", "25", "30+"
        ]
    ).ask()
    
    app_type = questionary.select(
        "What type of applications are you hosting?",
        choices=[
            "Container-based applications",
            "Serverless applications", 
            "Mixed architecture (containers + serverless)",
            "Traditional web applications"
        ]
    ).ask()
    
    environments = questionary.select(
        "How many environments do you need?",
        choices=[
            "3 (Dev, Staging, Prod)",
            "4 (Dev, Test, Staging, Prod)",
            "5 (Dev, Test, QA, Staging, Prod)",
            "6+ (Enterprise with multiple testing stages)"
        ]
    ).ask()
    
    region = questionary.text(
        "What is your primary region/country? (e.g., US, EU, APAC, Germany, Ireland)",
        default="US"
    ).ask()
    
    compliance = questionary.checkbox(
        "Select compliance requirements:",
        choices=[
            "GDPR (European data protection)",
            "HIPAA (Healthcare data)",
            "SOC 2 (Security controls)",
            "PCI DSS (Payment card data)",
            "FedRAMP (US government)",
            "None"
        ]
    ).ask()
    
    data_residency = questionary.select(
        "Data residency requirements:",
        choices=[
            "Data must stay in selected region",
            "Data can be replicated globally", 
            "No specific requirements"
        ]
    ).ask()
    
    security_level = questionary.select(
        "What is your required security level?",
        choices=[
            "Standard (Basic AWS security)",
            "High (Enhanced monitoring and controls)",
            "Critical (Maximum security, dedicated infrastructure)"
        ]
    ).ask()
    
    tenancy_model = questionary.select(
        "What is your multi-tenancy model?",
        choices=[
            "Single-tenant (Dedicated per customer)",
            "Multi-tenant shared (Shared infrastructure)",
            "Hybrid (Mix of shared and dedicated)"
        ]
    ).ask()
    
    return {
        'num_apps': int(num_apps.replace('+', '')),
        'app_type': app_type,
        'environments': environments,
        'region': region,
        'compliance': compliance,
        'data_residency': data_residency,
        'security_level': security_level,
        'tenancy_model': tenancy_model
    }

def generate_clean_saas_diagram(requirements: Dict[str, Any]) -> str:
    """
    Generate a clean SaaS architecture diagram using draw.io XML format
    with clean layout similar to LZ brainstorming style and multi-page support.
    
    Args:
        requirements: Dictionary containing SaaS requirements
        
    Returns:
        str: Path to the generated diagram file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"saas_clean_{requirements['num_apps']}apps_{requirements['region'].lower()}_{timestamp}.drawio"
    filepath = os.path.join("images", filename)
    
    # Ensure images directory exists
    os.makedirs("images", exist_ok=True)
    
    # Parse environments
    env_text = requirements['environments']
    if "6+" in env_text:
        nonprod_envs = ["Dev", "QA", "Performance", "UAT"]
        prod_envs = ["Pre-Prod", "Prod"]
    elif "5" in env_text:
        nonprod_envs = ["Dev", "QA", "UAT"]
        prod_envs = ["Pre-Prod", "Prod"]
    elif "4" in env_text:
        nonprod_envs = ["Dev", "QA"]
        prod_envs = ["Pre-Prod", "Prod"]
    else:
        nonprod_envs = ["Dev", "QA"]
        prod_envs = ["Prod"]
    
    # Calculate how many pages we need for individual apps
    total_apps = requirements['num_apps']
    apps_per_page = 6  # Max 6 apps per page for clean layout
    app_pages = max(1, (total_apps + apps_per_page - 1) // apps_per_page) if total_apps > 6 else 0
    
    total_pages = 1 + app_pages  # Overview + app detail pages
    
    # Start building the multi-page XML
    xml_content = f'''<mxfile host="app.diagrams.net" modified="2024-09-19T00:00:00.000Z" agent="5.0" etag="abc" version="24.1.0" pages="{total_pages}">'''
    
    # Generate overview page
    xml_content += generate_overview_page(requirements, nonprod_envs, prod_envs)
    
    # Generate application detail pages if needed
    if app_pages > 0:
        for page_num in range(app_pages):
            start_app = page_num * apps_per_page + 1
            end_app = min((page_num + 1) * apps_per_page, total_apps)
            xml_content += generate_application_page(
                page_num + 2, start_app, end_app, requirements, nonprod_envs, prod_envs
            )
    
    xml_content += "</mxfile>"
    
    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    return filepath

def generate_overview_page(requirements: Dict[str, Any], nonprod_envs: list, prod_envs: list) -> str:
    """Generate the main overview page showing the architecture structure."""
    xml_content = f'''
  <diagram id="overview" name="Architecture Overview">
    <mxGraphModel dx="2200" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="1200" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title and Requirements -->
        <mxCell id="2" value="Requirement: Hosting {requirements['num_apps']} SaaS applications in {len(nonprod_envs + prod_envs)} different environments&#xa;Assumption: {requirements['app_type']} and PaaS DB&#xa;Region: {requirements['region']} | Security: {requirements['security_level']} | Tenancy: {requirements['tenancy_model']}" style="text;html=1;align=right;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=11;fillColor=#f8f9fa;strokeColor=#dee2e6;" vertex="1" parent="1">
          <mxGeometry x="1050" y="30" width="500" height="80" as="geometry"/>
        </mxCell>
        
        <!-- AWS Control Tower -->
        <mxCell id="3" value="AWS Control Tower" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=14;image=img/lib/aws4/ManagementGovernance/AWS_Control_Tower.svg;" vertex="1" parent="1">
          <mxGeometry x="700" y="40" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Root SaaS Apps Management Group -->
        <mxCell id="4" value="SaaS Apps" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=14;image=img/lib/aws4/ManagementGovernance/AWS_Organizations.svg;" vertex="1" parent="1">
          <mxGeometry x="700" y="150" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Connection from Control Tower to SaaS Apps -->
        <mxCell id="5" value="" style="endArrow=classic;html=1;rounded=0;dashed=1;strokeColor=#666666;" edge="1" parent="1" source="3" target="4">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="730" y="120" as="sourcePoint"/>
            <mxPoint x="730" y="140" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
    
    cell_id = 6
    
    # Non-Production OU (larger, cleaner layout)
    nonprod_width = 1200
    nonprod_x = 50
    nonprod_y = 280
    
    xml_content += f'''
        
        <!-- Non-Production OU -->
        <mxCell id="{cell_id}" value="Non-Prod" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;verticalAlign=top;fontSize=16;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{nonprod_x}" y="{nonprod_y}" width="{nonprod_width}" height="180" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Non-prod environment accounts with better spacing
    env_spacing = nonprod_width // len(nonprod_envs)
    for i, env in enumerate(nonprod_envs):
        env_x = nonprod_x + 100 + (i * env_spacing)
        env_y = nonprod_y + 40
        
        # Management Group for environment
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/aws4/ManagementGovernance/AWS_Organizations.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{env_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Yellow connection indicator
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffc107;strokeColor=#ffc107;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 10}" y="{env_y + 50}" width="20" height="10" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Environment label
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 20}" y="{env_y + 70}" width="80" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Clean environment container
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e3f2fd;strokeColor=#1976d2;verticalAlign=top;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 30}" y="{env_y + 100}" width="100" height="120" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # ECS/Container Service Icon
        if "container" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
            xml_content += f'''
        <mxCell id="{cell_id}" value="ECS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Compute/Amazon_Elastic_Container_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 20}" y="{env_y + 120}" width="25" height="25" as="geometry"/>
        </mxCell>'''
            cell_id += 1
        
        # Lambda Service Icon for serverless
        if "serverless" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
            xml_content += f'''
        <mxCell id="{cell_id}" value="Lambda" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Compute/AWS_Lambda.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 10}" y="{env_y + 120}" width="25" height="25" as="geometry"/>
        </mxCell>'''
            cell_id += 1
        
        # ALB Load Balancer
        xml_content += f'''
        <mxCell id="{cell_id}" value="ALB" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/NetworkingContentDelivery/Elastic_Load_Balancing.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 20}" y="{env_y + 155}" width="25" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # RDS Database
        xml_content += f'''
        <mxCell id="{cell_id}" value="RDS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Database/Amazon_RDS.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 10}" y="{env_y + 155}" width="25" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Cluster type label (smaller, below icons)
        if "Single-tenant" in requirements['tenancy_model']:
            cluster_text = "Dedicated"
        else:
            cluster_text = "Shared"
            
        xml_content += f'''
        <mxCell id="{cell_id}" value="{cluster_text}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 30}" y="{env_y + 190}" width="100" height="20" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Connection from SaaS Apps to environment
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#1976d2;" edge="1" parent="1" source="4" target="{cell_id - 4}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="730" y="220" as="sourcePoint"/>
            <mxPoint x="{env_x + 20}" y="{env_y}" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
        cell_id += 1
    
    # Production OU (larger, cleaner layout)
    prod_y = nonprod_y + 220
    prod_width = 1200
    
    xml_content += f'''
        
        <!-- Production OU -->
        <mxCell id="{cell_id}" value="Prod" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;verticalAlign=top;fontSize=16;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{nonprod_x}" y="{prod_y}" width="{prod_width}" height="200" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Production environment accounts with better spacing
    prod_spacing = prod_width // len(prod_envs)
    for i, env in enumerate(prod_envs):
        env_x = nonprod_x + 200 + (i * prod_spacing)
        env_y = prod_y + 40
        
        # Management Group for environment
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/aws4/ManagementGovernance/AWS_Organizations.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{env_y}" width="40" height="40" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Yellow connection indicator
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffc107;strokeColor=#ffc107;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 10}" y="{env_y + 50}" width="20" height="10" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Environment label
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 20}" y="{env_y + 70}" width="80" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Production environment container (enhanced)
        xml_content += f'''
        <mxCell id="{cell_id}" value="{env} App{requirements['num_apps']}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#2e7d32;verticalAlign=top;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 40}" y="{env_y + 100}" width="120" height="140" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Auto Scaling Group for Production
        xml_content += f'''
        <mxCell id="{cell_id}" value="Auto Scaling" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Compute/Amazon_EC2_Auto_Scaling.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 30}" y="{env_y + 125}" width="25" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # ECS Fargate for Production containers
        if "container" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
            xml_content += f'''
        <mxCell id="{cell_id}" value="Fargate" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Compute/AWS_Fargate.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{env_y + 125}" width="25" height="25" as="geometry"/>
        </mxCell>'''
            cell_id += 1
        
        # Lambda for Production serverless
        if "serverless" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
            xml_content += f'''
        <mxCell id="{cell_id}" value="Lambda" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Compute/AWS_Lambda.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 30}" y="{env_y + 125}" width="25" height="25" as="geometry"/>
        </mxCell>'''
            cell_id += 1
        
        # Application Load Balancer for Production
        xml_content += f'''
        <mxCell id="{cell_id}" value="ALB" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/NetworkingContentDelivery/Elastic_Load_Balancing.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 30}" y="{env_y + 165}" width="25" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # RDS Multi-AZ for Production
        xml_content += f'''
        <mxCell id="{cell_id}" value="RDS Multi-AZ" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Database/Amazon_RDS.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{env_y + 165}" width="25" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # ElastiCache for Production
        xml_content += f'''
        <mxCell id="{cell_id}" value="Cache" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=8;image=img/lib/aws4/Database/Amazon_ElastiCache.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 30}" y="{env_y + 165}" width="25" height="25" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # KMS for encryption
        xml_content += f'''
        <mxCell id="{cell_id}" value="KMS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/SecurityIdentityCompliance/AWS_Key_Management_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 30}" y="{env_y + 205}" width="20" height="20" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # CloudWatch for monitoring
        xml_content += f'''
        <mxCell id="{cell_id}" value="CloudWatch" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/ManagementGovernance/Amazon_CloudWatch.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{env_y + 205}" width="20" height="20" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # WAF for security
        xml_content += f'''
        <mxCell id="{cell_id}" value="WAF" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/SecurityIdentityCompliance/AWS_WAF.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 30}" y="{env_y + 205}" width="20" height="20" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Dedicated cluster label
        xml_content += f'''
        <mxCell id="{cell_id}" value="Dedicated (Multi-AZ)" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x - 40}" y="{env_y + 230}" width="120" height="15" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Connection from SaaS Apps to production environment
        xml_content += f'''
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;strokeColor=#2e7d32;" edge="1" parent="1" source="4" target="{cell_id - 4}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="730" y="220" as="sourcePoint"/>
            <mxPoint x="{env_x + 20}" y="{env_y}" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
        cell_id += 1
    
    # Add summary information with enhanced visuals
    xml_content += f'''
        
        <!-- Global Services Section -->
        <mxCell id="{cell_id}" value="Global Services" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;verticalAlign=top;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="750" width="300" height="120" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Route 53 DNS
    xml_content += f'''
        <mxCell id="{cell_id}" value="Route 53" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/NetworkingContentDelivery/Amazon_Route_53.svg;" vertex="1" parent="1">
          <mxGeometry x="70" y="780" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # CloudFront CDN
    xml_content += f'''
        <mxCell id="{cell_id}" value="CloudFront" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/NetworkingContentDelivery/Amazon_CloudFront.svg;" vertex="1" parent="1">
          <mxGeometry x="130" y="780" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # WAF Security
    xml_content += f'''
        <mxCell id="{cell_id}" value="WAF" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/SecurityIdentityCompliance/AWS_WAF.svg;" vertex="1" parent="1">
          <mxGeometry x="190" y="780" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Certificate Manager
    xml_content += f'''
        <mxCell id="{cell_id}" value="ACM" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/SecurityIdentityCompliance/AWS_Certificate_Manager.svg;" vertex="1" parent="1">
          <mxGeometry x="250" y="780" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # IAM for identity management
    xml_content += f'''
        <mxCell id="{cell_id}" value="IAM" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/SecurityIdentityCompliance/AWS_Identity_and_Access_Management_IAM.svg;" vertex="1" parent="1">
          <mxGeometry x="70" y="820" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # AWS Config for compliance
    xml_content += f'''
        <mxCell id="{cell_id}" value="Config" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/ManagementGovernance/AWS_Config.svg;" vertex="1" parent="1">
          <mxGeometry x="130" y="820" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # CloudTrail for auditing
    xml_content += f'''
        <mxCell id="{cell_id}" value="CloudTrail" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/ManagementGovernance/AWS_CloudTrail.svg;" vertex="1" parent="1">
          <mxGeometry x="190" y="820" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Systems Manager
    xml_content += f'''
        <mxCell id="{cell_id}" value="SSM" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=9;image=img/lib/aws4/ManagementGovernance/AWS_Systems_Manager.svg;" vertex="1" parent="1">
          <mxGeometry x="250" y="820" width="30" height="30" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Summary Information with better formatting
    xml_content += f'''
        
        <!-- Summary Information -->
        <mxCell id="{cell_id}" value="📊 Architecture Summary:\\n• Total Applications: {requirements['num_apps']}\\n• Environments: {len(nonprod_envs + prod_envs)} ({len(nonprod_envs)} Non-Prod + {len(prod_envs)} Prod)\\n• Architecture: {requirements['app_type']}\\n• Tenancy: {requirements['tenancy_model']}\\n• Security Level: {requirements['security_level']}\\n• Data Residency: {requirements['data_residency']}\\n\\n🔧 Key Features:\\n• Auto Scaling Groups in Production\\n• Multi-AZ RDS databases\\n• Encryption at rest and in transit\\n• Centralized logging and monitoring" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;rounded=1;fontSize=10;fillColor=#e3f2fd;strokeColor=#1976d2;" vertex="1" parent="1">
          <mxGeometry x="400" y="750" width="400" height="220" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Compliance badges if applicable
    if requirements['compliance'] and 'None' not in requirements['compliance']:
        badge_x = 850
        badge_y = 750
        for i, compliance in enumerate(requirements['compliance']):
            if compliance != 'None':
                xml_content += f'''
        <mxCell id="{cell_id}" value="✅ {compliance}\\nCompliant" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d4edda;strokeColor=#155724;fontSize=9;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{badge_x}" y="{badge_y + i * 60}" width="80" height="50" as="geometry"/>
        </mxCell>'''
                cell_id += 1
    
    xml_content += '''
      </root>
    </mxGraphModel>
  </diagram>'''
    
    return xml_content

def generate_application_page(page_num: int, start_app: int, end_app: int, 
                            requirements: Dict[str, Any], nonprod_envs: list, prod_envs: list) -> str:
    """Generate a detailed page for individual applications."""
    xml_content = f'''
  <diagram id="apps-{page_num}" name="Applications {start_app}-{end_app}">
    <mxGraphModel dx="2200" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1800" pageHeight="1200" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Page Title -->
        <mxCell id="2" value="SaaS Applications {start_app} to {end_app} - Detailed View&#xa;Architecture: {requirements['app_type']}&#xa;Tenancy: {requirements['tenancy_model']}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontSize=14;fillColor=#e3f2fd;strokeColor=#1976d2;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="30" width="600" height="80" as="geometry"/>
        </mxCell>'''
    
    cell_id = 3
    
    # Calculate grid layout for applications
    apps_in_page = end_app - start_app + 1
    cols = 3  # 3 applications per row
    rows = (apps_in_page + cols - 1) // cols
    
    app_width = 500
    app_height = 300
    spacing_x = 50
    spacing_y = 50
    start_x = 100
    start_y = 150
    
    for app_idx in range(apps_in_page):
        app_num = start_app + app_idx
        col = app_idx % cols
        row = app_idx // cols
        
        x = start_x + col * (app_width + spacing_x)
        y = start_y + row * (app_height + spacing_y)
        
        # Application container
        xml_content += f'''
        
        <!-- Application {app_num} Container -->
        <mxCell id="{cell_id}" value="SaaS Application {app_num}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8f9fa;strokeColor=#495057;verticalAlign=top;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{x}" y="{y}" width="{app_width}" height="{app_height}" as="geometry"/>
        </mxCell>'''
        cell_id += 1
        
        # Non-Production environments for this app
        env_width = (app_width - 40) // len(nonprod_envs)
        for i, env in enumerate(nonprod_envs):
            env_x = x + 20 + (i * env_width)
            env_y = y + 40
            
            xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{env_y}" width="{env_width - 10}" height="100" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # AWS service icons for non-prod environments
            icon_y = env_y + 25
            
            # ECS/Container Service
            if "container" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
                xml_content += f'''
        <mxCell id="{cell_id}" value="ECS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Compute/Amazon_Elastic_Container_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 10}" y="{icon_y}" width="20" height="20" as="geometry"/>
        </mxCell>'''
                cell_id += 1
            
            # Lambda Service
            if "serverless" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
                xml_content += f'''
        <mxCell id="{cell_id}" value="λ" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Compute/AWS_Lambda.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + env_width - 40}" y="{icon_y}" width="20" height="20" as="geometry"/>
        </mxCell>'''
                cell_id += 1
            
            # RDS Database
            xml_content += f'''
        <mxCell id="{cell_id}" value="DB" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Database/Amazon_RDS.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 10}" y="{icon_y + 35}" width="20" height="20" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # S3 Storage
            xml_content += f'''
        <mxCell id="{cell_id}" value="S3" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Storage/Amazon_Simple_Storage_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + env_width - 40}" y="{icon_y + 35}" width="20" height="20" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # Cluster type text (smaller, centered)
            if "Single-tenant" in requirements['tenancy_model']:
                cluster_text = "Dedicated"
            else:
                cluster_text = "Shared"
                
            xml_content += f'''
        <mxCell id="{cell_id}" value="{cluster_text}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x + (env_width - 50) // 2}" y="{icon_y + 10}" width="50" height="15" as="geometry"/>
        </mxCell>'''
            cell_id += 1
        
        # Production environments for this app
        prod_env_width = (app_width - 40) // len(prod_envs)
        for i, env in enumerate(prod_envs):
            env_x = x + 20 + (i * prod_env_width)
            env_y = y + 170
            
            xml_content += f'''
        <mxCell id="{cell_id}" value="{env}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;verticalAlign=top;fontSize=10;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x}" y="{env_y}" width="{prod_env_width - 10}" height="110" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # Production AWS service icons with enhanced security
            icon_y = env_y + 25
            
            # Auto Scaling for production
            xml_content += f'''
        <mxCell id="{cell_id}" value="ASG" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Compute/Amazon_EC2_Auto_Scaling.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 5}" y="{icon_y}" width="18" height="18" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # ECS Fargate for production containers
            if "container" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
                xml_content += f'''
        <mxCell id="{cell_id}" value="Fargate" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Compute/AWS_Fargate.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + prod_env_width - 35}" y="{icon_y}" width="18" height="18" as="geometry"/>
        </mxCell>'''
                cell_id += 1
            
            # Lambda for production serverless
            if "serverless" in requirements['app_type'].lower() or "mixed" in requirements['app_type'].lower():
                xml_content += f'''
        <mxCell id="{cell_id}" value="λ" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Compute/AWS_Lambda.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + (prod_env_width // 2) - 9}" y="{icon_y}" width="18" height="18" as="geometry"/>
        </mxCell>'''
                cell_id += 1
            
            # RDS Multi-AZ for production
            xml_content += f'''
        <mxCell id="{cell_id}" value="RDS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Database/Amazon_RDS.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 5}" y="{icon_y + 30}" width="18" height="18" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # ElastiCache for production caching
            xml_content += f'''
        <mxCell id="{cell_id}" value="Cache" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=7;image=img/lib/aws4/Database/Amazon_ElastiCache.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + prod_env_width - 35}" y="{icon_y + 30}" width="18" height="18" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # KMS for encryption
            xml_content += f'''
        <mxCell id="{cell_id}" value="KMS" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=6;image=img/lib/aws4/SecurityIdentityCompliance/AWS_Key_Management_Service.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 5}" y="{icon_y + 55}" width="15" height="15" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # CloudWatch for monitoring
            xml_content += f'''
        <mxCell id="{cell_id}" value="CW" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=6;image=img/lib/aws4/ManagementGovernance/Amazon_CloudWatch.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + (prod_env_width // 2) - 7}" y="{icon_y + 55}" width="15" height="15" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # WAF for security
            xml_content += f'''
        <mxCell id="{cell_id}" value="WAF" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=6;image=img/lib/aws4/SecurityIdentityCompliance/AWS_WAF.svg;" vertex="1" parent="1">
          <mxGeometry x="{env_x + prod_env_width - 30}" y="{icon_y + 55}" width="15" height="15" as="geometry"/>
        </mxCell>'''
            cell_id += 1
            
            # Production label
            xml_content += f'''
        <mxCell id="{cell_id}" value="Dedicated (Multi-AZ, Encrypted)" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=7;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{env_x + 5}" y="{icon_y + 75}" width="{prod_env_width - 20}" height="15" as="geometry"/>
        </mxCell>'''
            cell_id += 1
    
    xml_content += '''
      </root>
    </mxGraphModel>
  </diagram>'''
    
    return xml_content

def provide_saas_recommendations(requirements: Dict[str, Any]) -> None:
    """Provide detailed SaaS architecture recommendations based on requirements."""
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
    print(f"• Deploy {requirements['num_apps']} applications across multiple environments")
    
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
    
    # Compliance recommendations
    if "GDPR" in requirements['compliance']:
        print("• Implement data encryption at rest and in transit")
        print("• Use AWS Config for GDPR compliance monitoring")
        print("• Implement data retention and deletion policies")
    elif "HIPAA" in requirements['compliance']:
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
    """Main function to run the clean SaaS architecture agent."""
    try:
        # Get requirements with validation
        requirements = get_saas_requirements()
        
        # Provide recommendations
        provide_saas_recommendations(requirements)
        
        # Generate clean diagram with multi-page support
        print("\n🎨 Generating clean SaaS architecture diagram with multi-page layout...")
        diagram_path = generate_clean_saas_diagram(requirements)
        print(f"✅ Clean architecture diagram generated successfully!")
        print(f"📁 Location: {diagram_path}")
        print(f"📊 Shows all {requirements['num_apps']} applications with clean, uncluttered layout")
        
        if requirements['num_apps'] > 6:
            print(f"📄 Multi-page layout: Overview + individual application details")
        
        print("\n" + "=" * 70)
        print("🛠️  NEXT STEPS FOR SAAS IMPLEMENTATION:")
        print("1. Review the generated clean architecture diagram")
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