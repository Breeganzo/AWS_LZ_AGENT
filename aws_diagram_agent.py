import questionary
import os

# AWS Landing Zone Architecture Agent
# Comprehensive tool for designing and generating AWS Landing Zone architectures using draw.io diagrams

def generate_drawio_diagram(industry, compliance, region, security_level, filename):
    """Generate draw.io compatible XML diagram with AWS stencils similar to         <mxCell id="{cell_id+1}" value="ECS Cluster&#xa;(Private VPC)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3cd;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="-120" y="230" width="80" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+2}" value="RDS Aurora&#xa;(Multi-AZ)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="-20" y="230" width="80" height="60" as="geometry"/>
        </mxCell>instorming format"""
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else ".", exist_ok=True)
    
    # Create the XML content directly as a string using professional AWS stencils
    xml_content = f'''<mxfile host="app.diagrams.net" modified="2024-09-19T00:00:00.000Z" agent="5.0" etag="abc" version="24.1.0">
  <diagram id="aws-landing-zone" name="AWS Landing Zone - {industry}">
    <mxGraphModel dx="1869" dy="1795" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Requirements and Assumptions -->
        <mxCell id="2" value="Industry: {industry}&#xa;Compliance: {', '.join(compliance) if compliance else 'Standard'}&#xa;Region: {region}&#xa;Security Level: {security_level}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="450" y="30" width="460" height="130" as="geometry"/>
        </mxCell>
        
        <!-- AWS Control Tower with Management Groups icon -->
        <mxCell id="3" value="AWS Control Tower" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/mscae/Management_Groups.svg;" vertex="1" parent="1">
          <mxGeometry x="305" y="70" width="50" height="40" as="geometry"/>
        </mxCell>'''
    
    cell_id = 4
    
    # Non-Prod OU with proper styling
    xml_content += f'''
        <!-- Non-Production OU -->
        <mxCell id="{cell_id}" value="Non-Prod OU" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="-150" y="190" width="1200" height="400" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Production OU with proper styling  
    xml_content += f'''
        <!-- Production OU -->
        <mxCell id="{cell_id}" value="Prod OU" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="-150" y="620" width="1200" height="400" as="geometry"/>
        </mxCell>'''
    cell_id += 1
    
    # Add detailed Non-Prod environment blocks with resources
    environments = ["DEV", "QA", "UAT"]
    for i, env in enumerate(environments):
        x_pos = -100 + i * 350
        xml_content += f'''
        
        <!-- {env} Environment Block -->
        <mxCell id="{cell_id}" value="{env} Environment" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1f5fe;strokeColor=#01579b;verticalAlign=top;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="230" width="320" height="320" as="geometry"/>
        </mxCell>
        
        <!-- {env} Account -->
        <mxCell id="{cell_id+1}" value="{env} Account" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/general/Subscriptions.svg;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 20}" y="260" width="24.79" height="40" as="geometry"/>
        </mxCell>
        
        <!-- {env} VPC -->
        <mxCell id="{cell_id+2}" value="Shared VPC&#xa;(10.{i}.0.0/16)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#f57c00;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 20}" y="320" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- {env} Private Subnets -->
        <mxCell id="{cell_id+3}" value="Private Subnets&#xa;App Tier" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 160}" y="320" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- {env} ECS Cluster -->
        <mxCell id="{cell_id+4}" value="ECS Cluster&#xa;(Shared)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 20}" y="390" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- {env} RDS -->
        <mxCell id="{cell_id+5}" value="RDS Aurora&#xa;(Shared)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 160}" y="390" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- {env} ALB -->
        <mxCell id="{cell_id+6}" value="Application&#xa;Load Balancer" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#2e7d32;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 20}" y="460" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- {env} Security Groups -->
        <mxCell id="{cell_id+7}" value="Security Groups&#xa;&amp; NACLs" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#c62828;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 160}" y="460" width="120" height="50" as="geometry"/>
        </mxCell>'''
        cell_id += 8
    
    # Add detailed Production environment blocks with resources
    xml_content += f'''
        
        <!-- Pre-Prod Environment Block -->
        <mxCell id="{cell_id}" value="Pre-Production Environment" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#2e7d32;verticalAlign=top;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="-100" y="660" width="500" height="320" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Account -->
        <mxCell id="{cell_id+1}" value="Pre-Prod Account" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/general/Subscriptions.svg;" vertex="1" parent="1">
          <mxGeometry x="-80" y="690" width="24.79" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod VPC -->
        <mxCell id="{cell_id+2}" value="Dedicated VPC&#xa;(10.100.0.0/16)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#f57c00;" vertex="1" parent="1">
          <mxGeometry x="-80" y="750" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Private/Public Subnets -->
        <mxCell id="{cell_id+3}" value="Multi-AZ Subnets&#xa;Private &amp; Public" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="100" y="750" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod EKS -->
        <mxCell id="{cell_id+4}" value="EKS Cluster&#xa;(Dedicated)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="-80" y="830" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod RDS with Multi-AZ -->
        <mxCell id="{cell_id+5}" value="RDS Aurora&#xa;Multi-AZ + Encryption" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="100" y="830" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Security -->
        <mxCell id="{cell_id+6}" value="KMS + WAF&#xa;Enhanced Security" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#c62828;" vertex="1" parent="1">
          <mxGeometry x="-80" y="910" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Monitoring -->
        <mxCell id="{cell_id+7}" value="CloudWatch&#xa;X-Ray Tracing" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e3f2fd;strokeColor=#1976d2;" vertex="1" parent="1">
          <mxGeometry x="100" y="910" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Production Environment Block -->
        <mxCell id="{cell_id+8}" value="Production Environment" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f1f8e9;strokeColor=#33691e;verticalAlign=top;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="450" y="660" width="550" height="320" as="geometry"/>
        </mxCell>
        
        <!-- Prod Account -->
        <mxCell id="{cell_id+9}" value="Prod Account" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/general/Subscriptions.svg;" vertex="1" parent="1">
          <mxGeometry x="470" y="690" width="24.79" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Prod VPC -->
        <mxCell id="{cell_id+10}" value="Production VPC&#xa;(10.200.0.0/16)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#f57c00;" vertex="1" parent="1">
          <mxGeometry x="470" y="750" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Prod Subnets -->
        <mxCell id="{cell_id+11}" value="Multi-AZ Subnets&#xa;High Availability" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="650" y="750" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Prod EKS -->
        <mxCell id="{cell_id+12}" value="EKS Cluster&#xa;Auto-Scaling" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="470" y="830" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Prod RDS -->
        <mxCell id="{cell_id+13}" value="RDS Aurora&#xa;Multi-Master" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="650" y="830" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Prod Security -->
        <mxCell id="{cell_id+14}" value="KMS + GuardDuty&#xa;Max Security" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#c62828;" vertex="1" parent="1">
          <mxGeometry x="470" y="910" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Prod Monitoring -->
        <mxCell id="{cell_id+15}" value="CloudWatch&#xa;Advanced Monitoring" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e3f2fd;strokeColor=#1976d2;" vertex="1" parent="1">
          <mxGeometry x="650" y="910" width="150" height="60" as="geometry"/>
        </mxCell>'''
    cell_id += 16
    
    # Add industry-specific elements
    if industry == "Financial":
        xml_content += f'''
        
        <!-- Financial Services - Compliance Layer -->
        <mxCell id="{cell_id}" value="Compliance &amp; Security Controls" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1100" y="190" width="400" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+1}" value="PCI-DSS&#xa;Compliance" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="1120" y="230" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+2}" value="KMS&#xa;Encryption" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="1250" y="230" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+3}" value="SOX&#xa;Compliance" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="1380" y="230" width="100" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Financial Services - Core Banking Infrastructure -->
        <mxCell id="{cell_id+4}" value="Core Banking Infrastructure" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1100" y="340" width="400" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+5}" value="Core Banking VPC&#xa;(Ultra-Secure)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="1120" y="380" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+6}" value="RDS Aurora&#xa;(Financial DB)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="1250" y="380" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+7}" value="DocumentDB&#xa;(Audit Logs)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="1380" y="380" width="100" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Financial Services - Trading Platform -->
        <mxCell id="{cell_id+8}" value="Trading Platform Infrastructure" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1100" y="490" width="400" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+9}" value="Trading VPC&#xa;(Low Latency)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="1120" y="530" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+10}" value="ElastiCache&#xa;(Market Data)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="1250" y="530" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+11}" value="Kinesis&#xa;(Real-time)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3cd;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="1380" y="530" width="100" height="60" as="geometry"/>
        </mxCell>'''
        cell_id += 12
        
    elif industry == "Healthcare":
        xml_content += f'''
        
        <!-- Healthcare HIPAA Controls -->
        <mxCell id="{cell_id}" value="HIPAA Compliance" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="700" y="150" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+1}" value="PHI Data Protection" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="850" y="150" width="120" height="40" as="geometry"/>
        </mxCell>'''
        cell_id += 2
        
    elif industry == "SaaS Hosting Provider":
        xml_content += f'''
        
        <!-- SaaS Multi-Tenancy Controls -->
        <mxCell id="{cell_id}" value="Multi-Tenant Isolation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="700" y="150" width="140" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+1}" value="Shared Non-Prod / Dedicated Prod" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="860" y="150" width="160" height="40" as="geometry"/>
        </mxCell>'''
        cell_id += 2
    
    # Add compliance controls
    if "GDPR" in compliance:
        xml_content += f'''
        
        <!-- GDPR Compliance -->
        <mxCell id="{cell_id}" value="GDPR Data Residency&#xa;{region} Region" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="1100" y="200" width="120" height="60" as="geometry"/>
        </mxCell>'''
        cell_id += 1
    
    if "HIPAA" in compliance:
        xml_content += f'''
        
        <!-- HIPAA Compliance -->
        <mxCell id="{cell_id}" value="HIPAA BAA&#xa;Encryption at Rest/Transit" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="1100" y="280" width="140" height="60" as="geometry"/>
        </mxCell>'''
        cell_id += 1
    
    # Add connections from Control Tower to environments
    xml_content += f'''
        
        <!-- Connection from Control Tower to Non-Prod OU -->
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="330" y="120" as="sourcePoint"/>
            <mxPoint x="450" y="190" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <!-- Connection from Control Tower to Prod OU -->
        <mxCell id="{cell_id+1}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="330" y="120" as="sourcePoint"/>
            <mxPoint x="450" y="620" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
    cell_id += 2
    
    # Close the XML structure
    xml_content += '''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    # Write the file
    with open(f"{filename}.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    return f"Generated draw.io diagram: {filename}.drawio"


def generate_saas_drawio_diagram(num_apps, num_environments, app_type, filename, industry="SaaS"):
    """Generate draw.io diagram specifically for SaaS hosting with professional AWS stencils"""
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else ".", exist_ok=True)
    
    # Create the XML content with professional styling like LZ brainstorming
    xml_content = f'''<mxfile host="app.diagrams.net" modified="2024-09-19T00:00:00.000Z" agent="5.0" etag="abc" version="24.1.0">
  <diagram id="saas-hosting" name="SaaS Hosting Architecture">
    <mxGraphModel dx="1869" dy="1795" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Requirements and Architecture Overview -->
        <mxCell id="2" value="Requirement: Hosting {num_apps} SaaS applications in {num_environments}&#xa;Assumption: {app_type}" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="450" y="30" width="460" height="130" as="geometry"/>
        </mxCell>
        
        <!-- SaaS Apps Management Group -->
        <mxCell id="3" value="SaaS Apps" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/mscae/Management_Groups.svg;" vertex="1" parent="1">
          <mxGeometry x="305" y="70" width="50" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Non-Production OU -->
        <mxCell id="4" value="Non-Prod" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="-150" y="190" width="363.69" height="180" as="geometry"/>
        </mxCell>
        
        <!-- Production OU -->
        <mxCell id="5" value="Prod" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="430" y="200" width="680" height="160" as="geometry"/>
        </mxCell>'''
    
    # Add environment-specific Management Groups and Subscriptions
    env_count = int(num_environments.split()[0]) if num_environments.split()[0].isdigit() else 4
    environments = ["DEV", "QA", "PERF", "UAT"][:env_count-1]  # Exclude prod from non-prod
    
    cell_id = 6
    
    # Non-Prod Management Groups
    for i, env in enumerate(environments):
        x_pos = 3.69 + i * 90
        xml_content += f'''
        
        <!-- {env} Management Group -->
        <mxCell id="{cell_id}" value="" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/mscae/Management_Groups.svg;" vertex="1" parent="1">
          <mxGeometry x="{x_pos}" y="230" width="50" height="40" as="geometry"/>
        </mxCell>
        
        <!-- {env} Subscription -->
        <mxCell id="{cell_id+1}" value="{env}" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/general/Subscriptions.svg;" vertex="1" parent="1">
          <mxGeometry x="{x_pos + 16.31}" y="290" width="24.79" height="40" as="geometry"/>
        </mxCell>'''
        cell_id += 2
    
    # Production Management Groups
    xml_content += f'''
        
        <!-- Pre-Prod Management Group -->
        <mxCell id="{cell_id}" value="" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/mscae/Management_Groups.svg;" vertex="1" parent="1">
          <mxGeometry x="585" y="240" width="50" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Production Management Group -->
        <mxCell id="{cell_id+1}" value="" style="image;sketch=0;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/mscae/Management_Groups.svg;" vertex="1" parent="1">
          <mxGeometry x="920" y="240" width="50" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Subscription -->
        <mxCell id="{cell_id+2}" value="Pre-Prod" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/general/Subscriptions.svg;" vertex="1" parent="1">
          <mxGeometry x="597.6" y="300" width="24.79" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Production Subscription -->
        <mxCell id="{cell_id+3}" value="Prod" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/general/Subscriptions.svg;" vertex="1" parent="1">
          <mxGeometry x="932.61" y="320" width="24.79" height="40" as="geometry"/>
        </mxCell>'''
    cell_id += 4
    
    # Add connections from SaaS Apps to environments
    xml_content += f'''
        
        <!-- Connections from SaaS Apps to Non-Prod -->
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.52;exitY=0.95;exitDx=0;exitDy=0;exitPerimeter=0;edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="300" y="300" as="sourcePoint"/>
            <mxPoint x="29" y="230" as="targetPoint"/>
            <Array as="points">
              <mxPoint x="331" y="140"/>
              <mxPoint x="29" y="140"/>
            </Array>
          </mxGeometry>
        </mxCell>
        
        <!-- Connections from SaaS Apps to Production -->
        <mxCell id="{cell_id+1}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.54;exitY=0.9;exitDx=0;exitDy=0;exitPerimeter=0;edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="300" y="300" as="sourcePoint"/>
            <mxPoint x="610" y="240" as="targetPoint"/>
            <Array as="points">
              <mxPoint x="332" y="140"/>
              <mxPoint x="610" y="140"/>
            </Array>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="{cell_id+2}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.56;exitY=0.9;exitDx=0;exitDy=0;exitPerimeter=0;edgeStyle=orthogonalEdgeStyle;" edge="1" parent="1" source="3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="300" y="300" as="sourcePoint"/>
            <mxPoint x="947" y="240" as="targetPoint"/>
            <Array as="points">
              <mxPoint x="333" y="140"/>
              <mxPoint x="947" y="140"/>
            </Array>
          </mxGeometry>
        </mxCell>'''
    cell_id += 3
    
    # Add detailed application deployment architecture
    xml_content += f'''
        
        <!-- Non-Prod Shared Infrastructure -->
        <mxCell id="{cell_id}" value="Dev Environment (Shared Resources)" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#e1f5fe;strokeColor=#01579b;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="-400" y="440" width="350" height="280" as="geometry"/>
        </mxCell>
        
        <!-- Dev VPC -->
        <mxCell id="{cell_id+1}" value="Dev VPC&#xa;(10.0.0.0/16)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#f57c00;" vertex="1" parent="1">
          <mxGeometry x="-380" y="480" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Dev Private Subnets -->
        <mxCell id="{cell_id+2}" value="Private Subnets&#xa;Multi-AZ" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="-240" y="480" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Dev ECS Cluster -->
        <mxCell id="{cell_id+3}" value="ECS Cluster&#xa;(Shared)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="-380" y="550" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Dev RDS Aurora -->
        <mxCell id="{cell_id+4}" value="RDS Aurora&#xa;(Shared)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="-240" y="550" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Dev ALB -->
        <mxCell id="{cell_id+5}" value="Application&#xa;Load Balancer" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#2e7d32;" vertex="1" parent="1">
          <mxGeometry x="-380" y="620" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Dev Security -->
        <mxCell id="{cell_id+6}" value="Security Groups&#xa;&amp; WAF" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#c62828;" vertex="1" parent="1">
          <mxGeometry x="-240" y="620" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Dev Additional Resources -->
        <mxCell id="{cell_id+7}" value="ElastiCache&#xa;(Session Store)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#ad1457;" vertex="1" parent="1">
          <mxGeometry x="-380" y="690" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Dev S3 & CloudFront -->
        <mxCell id="{cell_id+8}" value="S3 + CloudFront&#xa;(Static Assets)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8eaf6;strokeColor=#3f51b5;" vertex="1" parent="1">
          <mxGeometry x="-240" y="690" width="120" height="50" as="geometry"/>
        </mxCell>
        
        <!-- QA Environment -->
        <mxCell id="{cell_id+9}" value="QA Environment (Shared Resources)" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#e1f5fe;strokeColor=#01579b;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="0" y="440" width="350" height="280" as="geometry"/>
        </mxCell>
        
        <!-- QA Resources (similar to Dev but separate) -->
        <mxCell id="{cell_id+10}" value="QA VPC&#xa;(10.1.0.0/16)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#f57c00;" vertex="1" parent="1">
          <mxGeometry x="20" y="480" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+11}" value="Private Subnets&#xa;Multi-AZ" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="160" y="480" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+12}" value="ECS Cluster&#xa;(Shared)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="20" y="550" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+13}" value="RDS Aurora&#xa;(Shared)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="160" y="550" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+14}" value="Load Testing&#xa;Tools" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8f5e8;strokeColor=#2e7d32;" vertex="1" parent="1">
          <mxGeometry x="20" y="620" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+15}" value="Test Data&#xa;Management" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#c62828;" vertex="1" parent="1">
          <mxGeometry x="160" y="620" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+16}" value="API Gateway&#xa;(Testing)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#ad1457;" vertex="1" parent="1">
          <mxGeometry x="20" y="690" width="120" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+17}" value="Monitoring&#xa;&amp; Logging" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8eaf6;strokeColor=#3f51b5;" vertex="1" parent="1">
          <mxGeometry x="160" y="690" width="120" height="50" as="geometry"/>
        </mxCell>'''
    cell_id += 18
    
    # Add Pre-Prod Environment (Between Non-Prod and Prod)
    xml_content += f'''
        
        <!-- Pre-Production Environment -->
        <mxCell id="{cell_id}" value="Pre-Prod Environment (Production-Like)" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#e8f5e8;strokeColor=#2e7d32;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="400" y="440" width="500" height="280" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod VPC -->
        <mxCell id="{cell_id+1}" value="Pre-Prod VPC&#xa;(10.100.0.0/16)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#f57c00;" vertex="1" parent="1">
          <mxGeometry x="420" y="480" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Subnets -->
        <mxCell id="{cell_id+2}" value="Multi-AZ Subnets&#xa;Private &amp; Public" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="580" y="480" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Security -->
        <mxCell id="{cell_id+3}" value="Enhanced Security&#xa;GuardDuty + KMS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#c62828;" vertex="1" parent="1">
          <mxGeometry x="740" y="480" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod EKS -->
        <mxCell id="{cell_id+4}" value="EKS Cluster&#xa;(Production-like)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="420" y="560" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod RDS -->
        <mxCell id="{cell_id+5}" value="RDS Aurora&#xa;Multi-AZ + Encryption" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="580" y="560" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Services -->
        <mxCell id="{cell_id+6}" value="Full Stack Services&#xa;ALB + WAF + CDN" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8eaf6;strokeColor=#3f51b5;" vertex="1" parent="1">
          <mxGeometry x="740" y="560" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Performance Testing -->
        <mxCell id="{cell_id+7}" value="Performance Testing&#xa;Load Testing Tools" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fce4ec;strokeColor=#ad1457;" vertex="1" parent="1">
          <mxGeometry x="420" y="640" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Monitoring -->
        <mxCell id="{cell_id+8}" value="Advanced Monitoring&#xa;X-Ray + CloudWatch" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e3f2fd;strokeColor=#1976d2;" vertex="1" parent="1">
          <mxGeometry x="580" y="640" width="140" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Pre-Prod Backup & DR -->
        <mxCell id="{cell_id+9}" value="Backup &amp; DR&#xa;Cross-Region Sync" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="740" y="640" width="140" height="60" as="geometry"/>
        </mxCell>'''
    cell_id += 10
    
    # Add production applications with dedicated resources
    apps_per_row = 3
    for i in range(int(num_apps)):
        row = i // apps_per_row
        col = i % apps_per_row
        x = 510 + col * 280
        y = 800 + row * 200
        
        app_name = f"SaaS App{i+1:02d}"
        
        xml_content += f'''
        
        <!-- Production Application {i+1} -->
        <mxCell id="{cell_id}" value="{app_name} (Dedicated Resources)" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#f1f8e9;strokeColor=#33691e;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="{x}" y="{y}" width="260" height="180" as="geometry"/>
        </mxCell>
        
        <!-- App VPC -->
        <mxCell id="{cell_id+1}" value="Dedicated VPC&#xa;(10.{200+i}.0.0/16)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff3e0;strokeColor=#f57c00;" vertex="1" parent="1">
          <mxGeometry x="{x+10}" y="{y+30}" width="110" height="50" as="geometry"/>
        </mxCell>
        
        <!-- App Subnets -->
        <mxCell id="{cell_id+2}" value="Multi-AZ&#xa;Subnets" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f3e5f5;strokeColor=#7b1fa2;" vertex="1" parent="1">
          <mxGeometry x="{x+130}" y="{y+30}" width="110" height="50" as="geometry"/>
        </mxCell>
        
        <!-- App EKS -->
        <mxCell id="{cell_id+3}" value="EKS Cluster&#xa;(Auto-Scale)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="{x+10}" y="{y+90}" width="110" height="50" as="geometry"/>
        </mxCell>
        
        <!-- App RDS -->
        <mxCell id="{cell_id+4}" value="RDS Aurora&#xa;(Multi-AZ)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d1ecf1;strokeColor=#0c5460;" vertex="1" parent="1">
          <mxGeometry x="{x+130}" y="{y+90}" width="110" height="50" as="geometry"/>
        </mxCell>
        
        <!-- App Security & Monitoring -->
        <mxCell id="{cell_id+5}" value="ALB + WAF&#xa;KMS Encryption" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffebee;strokeColor=#c62828;" vertex="1" parent="1">
          <mxGeometry x="{x+10}" y="{y+150}" width="110" height="20" as="geometry"/>
        </mxCell>
        
        <!-- App Additional Services -->
        <mxCell id="{cell_id+6}" value="ElastiCache + S3&#xa;CloudFront CDN" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e8eaf6;strokeColor=#3f51b5;" vertex="1" parent="1">
          <mxGeometry x="{x+130}" y="{y+150}" width="110" height="20" as="geometry"/>
        </mxCell>'''
        cell_id += 7
    
    # Add financial services specific networking if applicable
    if industry == "Financial":
        xml_content += f'''
        
        <!-- Financial Services - Network Security -->
        <mxCell id="{cell_id}" value="Network Security &amp; Controls" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1200" y="550" width="350" height="180" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+1}" value="Private Subnets&#xa;(Isolated Workloads)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="1220" y="580" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+2}" value="Public Subnets&#xa;(ALB/NLB)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="1340" y="580" width="100" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+3}" value="AWS WAF&#xa;(DDoS Protection)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="1460" y="580" width="80" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+4}" value="Security Groups&#xa;(Zero Trust)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="1220" y="660" width="100" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+5}" value="NACLs&#xa;(Defense in Depth)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="1340" y="660" width="100" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="{cell_id+6}" value="GuardDuty&#xa;(Threat Detection)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="1460" y="660" width="80" height="50" as="geometry"/>
        </mxCell>'''
        cell_id += 7
    
    # Add connections from subscriptions to infrastructure (simplified)
    xml_content += f'''
        
        <!-- Connection from DEV subscription to Dev infrastructure -->
        <mxCell id="{cell_id}" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="29" y="330" as="sourcePoint"/>
            <mxPoint x="-300" y="440" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
    cell_id += 1
    
    # Close the XML structure
    xml_content += '''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    # Write the file
    with open(f"{filename}.drawio", "w", encoding="utf-8") as f:
        f.write(xml_content)
    
    return f"Generated SaaS hosting draw.io diagram: {filename}.drawio"


def generate_enhanced_saas_visualization(num_apps, num_environments, app_type):
    """Generate an enhanced visual representation of SaaS hosting architecture"""
    
    # Parse number of environments
    env_count = int(num_environments.split()[0]) if num_environments.split()[0].isdigit() else 5
    
    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│                         SaaS HOSTING ARCHITECTURE                   │")
    print("│                  Requirement: Hosting {} SaaS Applications           │".format(num_apps))
    print("│                  Assumption: {} │".format(app_type[:50].ljust(50)))
    print("│                  Environments: {} Total                              │".format(env_count))
    print("└─────────────────────────────────────────────────────────────────────┘")
    print("")
    print("                              📱 SaaS Apps")
    print("                                    │")
    print("                    ┌───────────────┼───────────────┐")
    print("                    │                               │")
    print("            ┌───────▼────────┐                ┌─────▼─────┐")
    print("            │    Non-Prod    │                │    Prod   │")
    print("            │      OU        │                │     OU    │")
    print("            └────────────────┘                └───────────┘")
    print("")
    
    # Non-Prod environments - show correct number based on selection
    print("    NON-PRODUCTION ENVIRONMENTS (Shared Resources)")
    if env_count == 4:
        print("    ┌─────────┬─────────┬─────────┐")
        print("    │   DEV   │   QA    │ Pre-Prod│")
        print("    └─────────┴─────────┴─────────┘")
        nonprod_envs = ["DEV", "QA", "Pre-Prod"]
    elif env_count == 5:
        print("    ┌─────────┬─────────┬─────────┬─────────┐")
        print("    │   DEV   │   QA    │  PERF   │ Pre-Prod│")
        print("    └─────────┴─────────┴─────────┴─────────┘")
        nonprod_envs = ["DEV", "QA", "PERF", "Pre-Prod"]
    elif env_count == 6:
        print("    ┌─────────┬─────────┬─────────┬─────────┬─────────┐")
        print("    │   DEV   │   QA    │  PERF   │   UAT   │ Pre-Prod│")
        print("    └─────────┴─────────┴─────────┴─────────┴─────────┘")
        nonprod_envs = ["DEV", "QA", "PERF", "UAT", "Pre-Prod"]
    
    print("\n    PRODUCTION ENVIRONMENT (Dedicated Resources)")
    print("    ┌────────────────────────────────────────────┐")
    print("    │                    PROD                    │")
    print("    └────────────────────────────────────────────┘")
    print("")
    
    # Show ALL SaaS applications clearly
    print(f"    ALL {num_apps} SaaS APPLICATIONS - Each with Dedicated Resources:")
    print("    " + "="*60)
    
    # Show applications in rows of 2 for better visualization
    apps_per_row = 2
    for i in range(0, int(num_apps), apps_per_row):
        app_range = range(i, min(i + apps_per_row, int(num_apps)))
        
        # App names row
        app_names = "                   ".join([f"App{j+1:02d}" for j in app_range])
        print(f"    {app_names}")
        
        # Show boxes for each app
        cluster_boxes = "    ".join(["┌─────────────┐" for _ in app_range])
        print(f"    {cluster_boxes}")
        
        cluster_name_rows = "    ".join(["│ Dedicated   │" for _ in app_range])
        print(f"    {cluster_name_rows}")
        
        cluster_name_rows = "    ".join(["│ Resources   │" for _ in app_range])
        print(f"    {cluster_name_rows}")
        
        print(f"    {cluster_boxes}")
        print("")


def generate_text_architecture(industry, compliance, region, security_level):
    """Generate a text-based architecture overview when diagrams can't be created"""
    
    print("AWS Landing Zone Architecture Structure:")
    print("├── AWS Control Tower")
    print("│   └── AWS Organization")
    print("│       ├── Root Account (Management)")
    print("│       ├── Security OU")
    print("│       │   ├── Security Account (CloudTrail, Config, etc.)")
    print("│       │   └── IAM Identity Center")
    
    if industry == "Financial":
        print("│       ├── Non-Production OU")
        print("│       │   ├── Dev Account")
        print("│       │   │   └── Shared VPC + Shared RDS")
        print("│       │   ├── QA Account")
        print("│       │   │   └── Shared VPC + Shared RDS")
        print("│       │   ├── Performance Account")
        print("│       │   │   └── Shared VPC + Shared RDS")
        print("│       │   └── UAT Account")
        print("│       │       └── Shared VPC + Shared RDS")
        print("│       └── Production OU")
        print("│           ├── Pre-Prod Account")
        print("│           │   └── Dedicated VPC + Dedicated RDS + KMS")
        print("│           └── Prod Account")
        print("│               └── Dedicated VPC + Dedicated RDS + KMS")
    elif industry == "Healthcare":
        print("│       ├── Non-Production OU")
        print("│       │   ├── Dev Account")
        print("│       │   │   └── Shared VPC + ECS Clusters")
        print("│       │   └── QA Account")
        print("│       │       └── Shared VPC + ECS Clusters")
        print("│       └── Production OU")
        print("│           └── Prod Account")
        print("│               └── HIPAA VPC + Health Records DB + KMS")
    elif industry == "Retail":
        print("│       ├── Non-Production OU")
        print("│       │   ├── Dev Account")
        print("│       │   │   └── Shared VPC + Catalog DB")
        print("│       │   ├── QA Account")
        print("│       │   │   └── Shared VPC + Catalog DB")
        print("│       │   └── Performance Account")
        print("│       │       └── Shared VPC + Catalog DB")
        print("│       └── Production OU")
        print("│           └── Prod Account")
        print("│               └── Production VPC + Production Catalog DB + CDN")
    elif industry == "SaaS Hosting Provider":
        print("│       ├── Non-Production OU")
        print("│       │   └── Shared Account")
        print("│       │       └── Shared VPC + ECS Clusters + PaaS Databases")
        print("│       └── Production OU")
        print("│           └── Dedicated Accounts per Application")
        print("│               └── Dedicated VPCs + ECS + RDS per App")


def get_recommendations(industry, compliance, region, security_level):
    """Generate industry and compliance-specific recommendations"""
    
    recommendations = [
        f"=== AWS LANDING ZONE RECOMMENDATIONS ===",
        f"Industry: {industry}",
        f"Compliance: {', '.join(compliance) if compliance else 'None'}",
        f"Region: {region}",
        f"Security Level: {security_level}",
        "",
        "GENERAL RECOMMENDATIONS:",
        "• Use AWS Control Tower for automated governance",
        "• Implement AWS Organizations for multi-account management",
        "• Set up AWS IAM Identity Center for centralized access",
        "• Enable AWS CloudTrail for comprehensive auditing",
        "• Use AWS Config for configuration compliance",
        "• Deploy AWS Security Hub for centralized security findings"
    ]
    
    # Industry-specific recommendations
    if industry == "Financial":
        recommendations.extend([
            "",
            "FINANCIAL SERVICES RECOMMENDATIONS:",
            "• Implement strict data encryption with AWS KMS",
            "• Use dedicated VPCs for production workloads",
            "• Enable AWS GuardDuty for fraud detection", 
            "• Consider AWS WAF for application protection",
            "• Use dedicated tenancy for sensitive workloads",
            "• Implement network segmentation between environments"
        ])
    elif industry == "Healthcare":
        recommendations.extend([
            "",
            "HEALTHCARE INDUSTRY RECOMMENDATIONS:",
            "• Ensure HIPAA compliance with proper encryption",
            "• Use AWS HealthLake for health data processing",
            "• Implement strict access controls with IAM",
            "• Enable VPC Flow Logs for network monitoring",
            "• Use AWS Macie for data classification and protection"
        ])
    elif industry == "Retail":
        recommendations.extend([
            "",
            "RETAIL INDUSTRY RECOMMENDATIONS:",
            "• Focus on scalability and cost optimization",
            "• Use AWS Auto Scaling for traffic spikes",
            "• Implement AWS CloudFront for global content delivery",
            "• Consider AWS Pinpoint for customer engagement",
            "• Use AWS Cost Explorer for cost management"
        ])
    elif industry == "SaaS Hosting Provider":
        recommendations.extend([
            "",
            "SAAS HOSTING PROVIDER RECOMMENDATIONS:",
            "• Use shared resources in Non-Prod for cost efficiency",
            "• Use dedicated resources in Prod for tenant isolation",
            "• Implement AWS ECS or EKS for containerized workloads",
            "• Use Amazon RDS or Aurora for managed databases",
            "• Consider AWS App Mesh for service mesh architecture",
            "• Implement AWS X-Ray for distributed tracing",
            "• Use AWS Secrets Manager for application secrets"
        ])
    
    # Compliance recommendations
    if "GDPR" in compliance:
        recommendations.extend([
            "",
            "GDPR COMPLIANCE RECOMMENDATIONS:",
            "• Ensure data residency in EU regions",
            "• Implement data encryption and access logging",
            "• Use AWS Config for compliance auditing",
            "• Enable data lifecycle management"
        ])
    
    if "HIPAA" in compliance:
        recommendations.extend([
            "",
            "HIPAA COMPLIANCE RECOMMENDATIONS:",
            "• Use AWS Business Associate Agreement",
            "• Implement end-to-end encryption",
            "• Enable comprehensive audit logging",
            "• Use AWS CloudHSM for key management"
        ])
    
    if "PCI-DSS" in compliance:
        recommendations.extend([
            "",
            "PCI-DSS COMPLIANCE RECOMMENDATIONS:",
            "• Segment payment processing environments",
            "• Use AWS WAF for web application protection",
            "• Implement network access controls",
            "• Regular security assessments and penetration testing"
        ])
    
    # Security level recommendations
    if security_level == "High":
        recommendations.extend([
            "",
            "HIGH SECURITY RECOMMENDATIONS:",
            "• Use AWS CloudHSM for dedicated key management",
            "• Enable AWS GuardDuty in all accounts",
            "• Implement AWS Inspector for vulnerability assessment",
            "• Use dedicated tenancy for sensitive workloads",
            "• Enable VPC Flow Logs and DNS query logging"
        ])
    
    return "\n".join(recommendations)


def main():
    """Main function to run the AWS Landing Zone Architecture Agent"""
    
    print("🚀 AWS Landing Zone Architecture Agent")
    print("="*40)
    print("This agent will help you design a comprehensive AWS Landing Zone")
    print("architecture based on your business requirements.\n")
    
    # Get user inputs
    industry = questionary.select(
        "What industry is your organization in?",
        choices=[
            "Financial",
            "Healthcare", 
            "Retail",
            "Manufacturing",
            "Education",
            "Government",
            "SaaS Hosting Provider",
            "Other"
        ]
    ).ask()
    
    # Special handling for SaaS hosting
    if industry == "SaaS Hosting Provider":
        num_apps = questionary.text("How many SaaS applications do you need to host? (e.g., 10):").ask()
        
        num_environments = questionary.select(
            "How many environments do you need?",
            choices=[
                "4 (Dev, QA, Pre-Prod, Prod)",
                "5 (Dev, QA, Performance, Pre-Prod, Prod)", 
                "6 (Dev, QA, Performance, UAT, Pre-Prod, Prod)"
            ]
        ).ask()
        
        app_type = questionary.select(
            "What type of applications?",
            choices=[
                "Containerized applications with PaaS DB",
                "Traditional applications with managed DB",
                "Microservices with container orchestration"
            ]
        ).ask()
        
        compliance = questionary.checkbox(
            "Select your compliance requirements:",
            choices=["GDPR", "HIPAA", "PCI-DSS", "SOX", "ISO 27001"]
        ).ask()
        
        region = questionary.text("What is your primary region/country? (e.g., US, EU, APAC):").ask()
        
        security_level = questionary.select(
            "What is your required security level?",
            choices=["Standard", "High", "Critical"]
        ).ask()
        
        # Generate SaaS hosting recommendations
        print("\n" + "="*60)
        print("=== SaaS HOSTING ARCHITECTURE RECOMMENDATIONS ===")
        print(f"Applications: {num_apps}")
        print(f"Environments: {num_environments}")
        print(f"Application Type: {app_type}")
        print(f"Compliance: {', '.join(compliance) if compliance else 'None'}")
        print(f"Region: {region}")
        print(f"Security Level: {security_level}")
        print()
        print("SaaS HOSTING RECOMMENDATIONS:")
        print("• Use AWS Control Tower for multi-account governance")
        print("• Implement separate OUs for Non-Prod and Prod environments")
        print("• Use shared resources in Non-Prod for cost efficiency")
        print("• Use dedicated resources in Prod for isolation and performance")
        print("• Use Amazon ECS or EKS for containerized workloads")
        print("• Use Amazon RDS or Aurora for managed PaaS databases")
        print("• Implement centralized logging and monitoring")
        
        # Generate SaaS hosting diagram
        filename = f"images/saas_hosting_{num_apps}apps_{region.lower()}"
        print(f"\n🎨 Generating SaaS hosting architecture diagram...")
        
        try:
            result = generate_saas_drawio_diagram(num_apps, num_environments, app_type, filename, industry)
            print(f"✅ SaaS hosting diagram generated successfully!")
            print(f"📁 Location: {filename}.drawio")
            
        except Exception as e:
            print(f"❌ Error generating draw.io diagram: {e}")
            print("\n🎨 DETAILED SAAS HOSTING ARCHITECTURE VISUALIZATION:")
            print("="*70)
            generate_enhanced_saas_visualization(num_apps, num_environments, app_type)
        
        print("\n" + "="*60)
        print("🛠️  NEXT STEPS FOR SAAS HOSTING:")
        print("1. Review the generated architecture diagram")
        print("2. Set up AWS Control Tower with proper OUs")
        print("3. Create shared infrastructure for Non-Prod environments")
        print("4. Create dedicated infrastructure for Prod environments")
        print("5. Implement container orchestration (ECS/EKS)")
        print("6. Set up managed databases (RDS/Aurora)")
        print("7. Configure auto-scaling and load balancing")
        print("8. Implement monitoring and alerting")
        
        return
    
    # Standard Landing Zone for other industries
    compliance = questionary.checkbox(
        "Select your compliance requirements:",
        choices=["GDPR", "HIPAA", "PCI-DSS", "SOX", "ISO 27001"]
    ).ask()
    
    region = questionary.text("What is your primary region/country? (e.g., US, EU, APAC):").ask()
    
    security_level = questionary.select(
        "What is your required security level?",
        choices=["Standard", "High", "Critical"]
    ).ask()
    
    num_environments = questionary.select(
        "How many environments do you need?",
        choices=[
            "3 (Basic: Dev, QA, Prod)",
            "4 (Standard: Dev, QA, UAT, Prod)", 
            "5 (Enterprise: Dev, QA, Performance, UAT, Prod)",
            "6 (Financial: Dev, QA, Performance, UAT, Pre-Prod, Prod)"
        ]
    ).ask()
    
    # Generate recommendations
    print("\n" + "="*60)
    recommendations = get_recommendations(industry, compliance, region, security_level)
    print(recommendations)
    
    # Generate diagram
    industry_str = industry.lower() if industry else "unknown"
    region_str = region.lower() if region else "unknown"
    filename = f"images/aws_landing_zone_{industry_str}_{region_str}"
    print(f"\n🎨 Generating architecture diagram...")
    
    try:
        generate_drawio_diagram(industry, compliance, region, security_level, filename)
        print(f"✅ Architecture diagram generated successfully!")
        print(f"📁 Location: {filename}.drawio")
        print(f"📁 You can also find it in the 'images' folder")
        
    except Exception as e:
        print(f"❌ Error generating draw.io diagram: {e}")
        print("\n🎨 TEXT-BASED ARCHITECTURE OVERVIEW:")
        print("="*50)
        generate_text_architecture(industry, compliance, region, security_level)
    
    print("\n" + "="*60)
    print("🛠️  NEXT STEPS:")
    print("1. Review the generated architecture diagram")
    print("2. Implement AWS Control Tower in your organization")
    print("3. Create the recommended Organizational Units (OUs)")
    print("4. Set up the required AWS accounts")
    print("5. Apply security guardrails and compliance controls")
    print("6. Deploy your workloads following the architecture")
    print("\n📚 For detailed implementation, consult AWS Control Tower documentation.")


if __name__ == "__main__":
    main()