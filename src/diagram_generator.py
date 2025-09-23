import logging
import json
import os
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class AWSDiagramGenerator:
    """
    AWS diagram generator supporting both Mermaid.js and Draw.io XML formats
    """
    
    def __init__(self):
        """Initialize the diagram generator"""
        self.templates = self._load_templates()
    
    def _escape_xml(self, text: str) -> str:
        """Escape XML entities properly"""
        return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')
    
    def _load_templates(self) -> Dict[str, Any]:
        """Load diagram templates"""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            templates_dir = os.path.join(os.path.dirname(current_dir), 'templates')
            templates_file = os.path.join(templates_dir, 'diagrams.json')
            
            if os.path.exists(templates_file):
                with open(templates_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            logger.warning(f"Could not load diagram templates: {e}")
        
        # Return default templates if loading fails
        return self._get_default_templates()
    
    def _get_default_templates(self) -> Dict[str, Any]:
        """Get default diagram templates"""
        return {
            "mermaid": {
                "landing_zone_standard": """
                graph TB
                    subgraph "AWS Organization"
                        CT[AWS Control Tower]
                        
                        subgraph "Security OU"
                            SA[Security Account]
                            LA[Logging Account]
                            AT[Audit Account]
                        end
                        
                        subgraph "Production OU"
                            PA[Production Account]
                            subgraph "Prod VPC"
                                PWA[Web Apps]
                                PDB[Databases]
                            end
                        end
                        
                        subgraph "Non-Production OU"
                            DA[Development Account]
                            TA[Testing Account]
                            subgraph "Dev VPC"
                                DWA[Dev Web Apps]
                                DDB[Dev Databases]
                            end
                        end
                    end
                    
                    CT --> SA
                    CT --> LA
                    CT --> AT
                    CT --> PA
                    CT --> DA
                    CT --> TA
                """,
                "single_account": """
                graph TB
                    subgraph "Single AWS Account"
                        subgraph "Production VPC"
                            PWA[Production Apps]
                            PDB[Production DB]
                        end
                        
                        subgraph "Development VPC"
                            DWA[Development Apps]
                            DDB[Development DB]
                        end
                        
                        IAM[IAM Users & Roles]
                        CT[CloudTrail]
                        CW[CloudWatch]
                    end
                """
            }
        }
    
    def generate_mermaid(self, recommendation: Dict[str, Any], answers: Dict[str, Any]) -> str:
        """Generate Mermaid.js diagram"""
        pattern_id = recommendation['pattern']['id']
        industry = answers.get('industry', 'General')
        
        # Get base template
        template = self._get_mermaid_template(pattern_id)
        
        # Customize based on industry and answers
        diagram = self._customize_mermaid_diagram(template, recommendation, answers)
        
        return diagram
    
    def _get_mermaid_template(self, pattern_id: str) -> str:
        """Get Mermaid template for a specific pattern"""
        mermaid_templates = self.templates.get('mermaid', {})
        
        # Map pattern IDs to templates
        template_map = {
            'single_account': 'single_account',
            'multi_account_basic': 'landing_zone_standard',
            'landing_zone_standard': 'landing_zone_standard',
            'landing_zone_financial': 'landing_zone_standard',
            'landing_zone_healthcare': 'landing_zone_standard',
            'landing_zone_government': 'landing_zone_standard',
            'hybrid_cloud': 'landing_zone_standard',
            'multi_region': 'landing_zone_standard'
        }
        
        template_key = template_map.get(pattern_id, 'landing_zone_standard')
        return mermaid_templates.get(template_key, self._get_default_mermaid())
    
    def _get_default_mermaid(self) -> str:
        """Get default Mermaid diagram"""
        return """
        graph TB
            subgraph "AWS Landing Zone"
                CT[AWS Control Tower]
                ORG[AWS Organizations]
                
                subgraph "Security OU"
                    SEC[Security Account]
                    LOG[Logging Account]
                end
                
                subgraph "Production OU"
                    PROD[Production Workloads]
                end
                
                subgraph "Non-Production OU"
                    DEV[Development]
                    TEST[Testing]
                end
            end
            
            CT --> ORG
            ORG --> SEC
            ORG --> LOG
            ORG --> PROD
            ORG --> DEV
            ORG --> TEST
        """
    
    def _customize_mermaid_diagram(self, template: str, recommendation: Dict[str, Any], answers: Dict[str, Any]) -> str:
        """Customize Mermaid diagram based on answers"""
        diagram = template
        
        # Add industry-specific customizations
        industry = answers.get('industry', '')
        if 'Financial' in industry:
            diagram = diagram.replace('Security Account', 'Security Account<br/>PCI DSS Controls')
        elif 'Healthcare' in industry:
            diagram = diagram.replace('Security Account', 'Security Account<br/>HIPAA Controls')
        elif 'Government' in industry:
            diagram = diagram.replace('Security Account', 'Security Account<br/>FedRAMP Controls')
        
        # Add compliance annotations
        compliance = answers.get('compliance_requirements', [])
        if compliance and compliance != ['None']:
            compliance_text = ', '.join(compliance[:2])  # Show first 2 compliance requirements
            diagram = diagram.replace('AWS Control Tower', f'AWS Control Tower<br/>Compliance: {compliance_text}')
        
        # Add region information
        regions = answers.get('regions', [])
        if len(regions) > 1:
            region_text = f"Multi-Region: {len(regions)} regions"
            diagram = diagram.replace('AWS Landing Zone', f'AWS Landing Zone<br/>{region_text}')
        
        return diagram
    
    def generate_drawio(self, recommendation: Dict[str, Any], answers: Dict[str, Any]) -> str:
        """Generate Draw.io XML diagram"""
        pattern_id = recommendation['pattern']['id']
        industry = answers.get('industry', 'General')
        compliance = answers.get('compliance_requirements', [])
        regions = answers.get('regions', [])
        
        # Build the XML structure
        xml_content = self._build_drawio_xml(pattern_id, industry, compliance, regions, recommendation)
        
        return xml_content
    
    def _build_drawio_xml(self, pattern_id: str, industry: str, compliance: List[str], regions: List[str], recommendation: Dict[str, Any]) -> str:
        """Build the complete Draw.io XML structure"""
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
        
        # Escape XML entities properly
        
        # XML header
        xml_content = f'''<mxfile host="app.diagrams.net" modified="{timestamp}" agent="AWS Landing Zone Architect" version="24.1.0">
  <diagram id="aws-landing-zone" name="AWS Landing Zone - {self._escape_xml(industry)}">
    <mxGraphModel dx="1869" dy="1795" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Header Information -->
        <mxCell id="2" value="Industry: {self._escape_xml(industry)}&#xa;Pattern: {self._escape_xml(recommendation['pattern']['name'])}&#xa;Compliance: {self._escape_xml(', '.join(compliance) if compliance else 'Standard')}&#xa;Regions: {self._escape_xml(', '.join(regions[:3]) if regions else 'Not specified')}" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fillColor=#f8f9fa;strokeColor=#dee2e6;" vertex="1" parent="1">
          <mxGeometry x="450" y="30" width="350" height="100" as="geometry"/>
        </mxCell>'''
        
        cell_id = 3
        
        # Add AWS Control Tower (if applicable)
        if pattern_id != 'single_account':
            xml_content += f'''
        
        <!-- AWS Control Tower -->
        <mxCell id="{cell_id}" value="AWS Control Tower" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.control_tower;" vertex="1" parent="1">
          <mxGeometry x="305" y="150" width="60" height="60" as="geometry"/>
        </mxCell>'''
            cell_id += 1
        
        # Add organization structure based on pattern
        if pattern_id == 'single_account':
            xml_content += self._add_single_account_structure(cell_id)
        else:
            xml_content += self._add_multi_account_structure(cell_id, pattern_id, industry, compliance)
        
        # Close XML
        xml_content += '''
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
        
        return xml_content
    
    def _add_single_account_structure(self, start_id: int) -> str:
        """Add single account structure to Draw.io XML"""
        return f'''
        
        <!-- Single AWS Account -->
        <mxCell id="{start_id}" value="AWS Account" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;verticalAlign=top;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="100" y="250" width="500" height="400" as="geometry"/>
        </mxCell>
        
        <!-- Production VPC -->
        <mxCell id="{start_id+1}" value="Production VPC" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="120" y="290" width="220" height="150" as="geometry"/>
        </mxCell>
        
        <!-- Development VPC -->
        <mxCell id="{start_id+2}" value="Development VPC" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;verticalAlign=top;" vertex="1" parent="1">
          <mxGeometry x="360" y="290" width="220" height="150" as="geometry"/>
        </mxCell>
        
        <!-- Production Applications -->
        <mxCell id="{start_id+3}" value="Web Applications" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.ec2_instance;" vertex="1" parent="1">
          <mxGeometry x="140" y="320" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Production Database -->
        <mxCell id="{start_id+4}" value="Database" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F48CC;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.rds_instance;" vertex="1" parent="1">
          <mxGeometry x="220" y="320" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Development Applications -->
        <mxCell id="{start_id+5}" value="Dev Applications" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.ec2_instance;" vertex="1" parent="1">
          <mxGeometry x="380" y="320" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Development Database -->
        <mxCell id="{start_id+6}" value="Dev Database" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F48CC;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.rds_instance;" vertex="1" parent="1">
          <mxGeometry x="460" y="320" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- IAM -->
        <mxCell id="{start_id+7}" value="IAM" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#DD344C;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.iam;" vertex="1" parent="1">
          <mxGeometry x="140" y="500" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- CloudTrail -->
        <mxCell id="{start_id+8}" value="CloudTrail" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#DD344C;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.cloudtrail;" vertex="1" parent="1">
          <mxGeometry x="220" y="500" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- CloudWatch -->
        <mxCell id="{start_id+9}" value="CloudWatch" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#CC2264;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.cloudwatch;" vertex="1" parent="1">
          <mxGeometry x="300" y="500" width="40" height="40" as="geometry"/>
        </mxCell>'''
    
    def _add_multi_account_structure(self, start_id: int, pattern_id: str, industry: str, compliance: List[str]) -> str:
        """Add multi-account structure to Draw.io XML"""
        cell_id = start_id
        
        xml_content = f'''
        
        <!-- AWS Organizations -->
        <mxCell id="{cell_id}" value="AWS Organizations" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.organizations;" vertex="1" parent="1">
          <mxGeometry x="305" y="230" width="60" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Security OU -->
        <mxCell id="{cell_id+1}" value="Security OU" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;verticalAlign=top;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="350" width="200" height="300" as="geometry"/>
        </mxCell>
        
        <!-- Non-Production OU -->
        <mxCell id="{cell_id+2}" value="Non-Production OU" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;verticalAlign=top;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="350" width="250" height="300" as="geometry"/>
        </mxCell>
        
        <!-- Production OU -->
        <mxCell id="{cell_id+3}" value="Production OU" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;verticalAlign=top;fontSize=12;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="540" y="350" width="200" height="300" as="geometry"/>
        </mxCell>'''
        
        cell_id += 4
        
        # Add Security OU accounts
        security_title = "Security & Compliance"
        if 'Financial' in industry:
            security_title += "\\nPCI DSS Controls"
        elif 'Healthcare' in industry:
            security_title += "\\nHIPAA Controls"
        elif 'Government' in industry:
            security_title += "\\nFedRAMP Controls"
        
        xml_content += f'''
        
        <!-- Security Account -->
        <mxCell id="{cell_id}" value="{self._escape_xml(security_title)}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#DD344C;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.security_hub;" vertex="1" parent="1">
          <mxGeometry x="80" y="390" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Logging Account -->
        <mxCell id="{cell_id+1}" value="{self._escape_xml('Centralized\\nLogging')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#DD344C;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.cloudtrail;" vertex="1" parent="1">
          <mxGeometry x="160" y="390" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Audit Account -->
        <mxCell id="{cell_id+2}" value="{self._escape_xml('Audit &\\nCompliance')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#DD344C;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.config;" vertex="1" parent="1">
          <mxGeometry x="120" y="460" width="40" height="40" as="geometry"/>
        </mxCell>'''
        
        cell_id += 3
        
        # Add Non-Production accounts
        xml_content += f'''
        
        <!-- Development Account -->
        <mxCell id="{cell_id}" value="{self._escape_xml('Development\\nAccount')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.account;" vertex="1" parent="1">
          <mxGeometry x="290" y="390" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Testing Account -->
        <mxCell id="{cell_id+1}" value="{self._escape_xml('Testing\\nAccount')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.account;" vertex="1" parent="1">
          <mxGeometry x="370" y="390" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Staging Account -->
        <mxCell id="{cell_id+2}" value="{self._escape_xml('Staging\\nAccount')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.account;" vertex="1" parent="1">
          <mxGeometry x="450" y="390" width="40" height="40" as="geometry"/>
        </mxCell>'''
        
        cell_id += 3
        
        # Add Production accounts
        xml_content += f'''
        
        <!-- Production Account -->
        <mxCell id="{cell_id}" value="{self._escape_xml('Production\\nWorkloads')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F48CC;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.account;" vertex="1" parent="1">
          <mxGeometry x="570" y="390" width="40" height="40" as="geometry"/>
        </mxCell>
        
        <!-- Production VPC -->
        <mxCell id="{cell_id+1}" value="{self._escape_xml('Production VPC')}" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;verticalAlign=top;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="550" y="460" width="170" height="120" as="geometry"/>
        </mxCell>
        
        <!-- Production Applications -->
        <mxCell id="{cell_id+2}" value="{self._escape_xml('Applications')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.ec2_instance;" vertex="1" parent="1">
          <mxGeometry x="565" y="490" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Production Database -->
        <mxCell id="{cell_id+3}" value="{self._escape_xml('Database')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F48CC;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.rds_instance;" vertex="1" parent="1">
          <mxGeometry x="615" y="490" width="30" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Load Balancer -->
        <mxCell id="{cell_id+4}" value="{self._escape_xml('Load Balancer')}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#FF9900;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=9;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.application_load_balancer;" vertex="1" parent="1">
          <mxGeometry x="665" y="490" width="30" height="30" as="geometry"/>
        </mxCell>'''
        
        # Add connections
        xml_content += f'''
        
        <!-- Connections -->
        <mxCell id="{cell_id+5}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="1" source="{start_id}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="335" y="310" as="sourcePoint"/>
            <mxPoint x="150" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="{cell_id+6}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="1" source="{start_id}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="335" y="310" as="sourcePoint"/>
            <mxPoint x="395" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="{cell_id+7}" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="1" source="{start_id}">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="335" y="310" as="sourcePoint"/>
            <mxPoint x="640" y="350" as="targetPoint"/>
          </mxGeometry>
        </mxCell>'''
        
        return xml_content
    
    def save_diagrams(self, recommendations: Dict[str, Any], diagram_format: str = "both") -> Dict[str, str]:
        """
        Save diagrams to proper directories with organized filenames
        
        Args:
            recommendations: The recommendations dict containing pattern info
            diagram_format: "mermaid", "drawio", or "both"
        
        Returns:
            Dict with saved file paths
        """
        saved_files = {}
        
        # Generate timestamp for filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Extract pattern info for filename
        pattern_name = recommendations.get('pattern', {}).get('name', 'aws_architecture')
        industry = recommendations.get('industry', 'general')
        
        # Clean filename components
        pattern_clean = pattern_name.lower().replace(' ', '_').replace('-', '_')
        industry_clean = industry.lower().replace(' ', '_').replace('-', '_')
        
        base_filename = f"{pattern_clean}_{industry_clean}_{timestamp}"
        
        if diagram_format in ["mermaid", "both"]:
            # Generate and save Mermaid diagram
            mermaid_content = self.generate_mermaid(recommendations, {})
            mermaid_path = os.path.join("images", "mermaid", f"{base_filename}.md")
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(mermaid_path), exist_ok=True)
            
            with open(mermaid_path, 'w', encoding='utf-8') as f:
                f.write(f"# AWS Architecture Diagram\n\n")
                f.write(f"**Industry:** {industry}\n")
                f.write(f"**Pattern:** {pattern_name}\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("```mermaid\n")
                f.write(mermaid_content)
                f.write("\n```\n")
            
            saved_files['mermaid'] = os.path.abspath(mermaid_path)
            logger.info(f"Mermaid diagram saved to: {mermaid_path}")
        
        if diagram_format in ["drawio", "both"]:
            # Generate and save Draw.io diagram
            drawio_content = self.generate_drawio(recommendations, {})
            drawio_path = os.path.join("images", "drawio", f"{base_filename}.drawio")
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(drawio_path), exist_ok=True)
            
            with open(drawio_path, 'w', encoding='utf-8') as f:
                f.write(drawio_content)
            
            saved_files['drawio'] = os.path.abspath(drawio_path)
            logger.info(f"Draw.io diagram saved to: {drawio_path}")
        
        return saved_files
    
    def get_diagram_file_path(self, recommendations: Dict[str, Any], format_type: str) -> str:
        """
        Generate proper file path for diagram
        
        Args:
            recommendations: The recommendations dict
            format_type: "mermaid" or "drawio"
        
        Returns:
            Relative file path
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        pattern_name = recommendations.get('pattern', {}).get('name', 'aws_architecture')
        industry = recommendations.get('industry', 'general')
        
        # Clean filename components
        pattern_clean = pattern_name.lower().replace(' ', '_').replace('-', '_')
        industry_clean = industry.lower().replace(' ', '_').replace('-', '_')
        
        base_filename = f"{pattern_clean}_{industry_clean}_{timestamp}"
        
        if format_type == "mermaid":
            return os.path.join("images", "mermaid", f"{base_filename}.md")
        elif format_type == "drawio":
            return os.path.join("images", "drawio", f"{base_filename}.drawio")
        else:
            raise ValueError(f"Unsupported format type: {format_type}")