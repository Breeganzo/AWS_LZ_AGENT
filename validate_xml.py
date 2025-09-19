#!/usr/bin/env python3
"""
Simple XML validation script to check if the draw.io file is well-formed
"""

import xml.etree.ElementTree as ET
import sys

def validate_xml_file(filepath):
    """Validate that the XML file is well-formed"""
    try:
        tree = ET.parse(filepath)
        print(f"✅ XML file '{filepath}' is valid and well-formed!")
        root = tree.getroot()
        print(f"📄 Root element: {root.tag}")
        
        # Count some key elements
        diagrams = root.findall('.//diagram')
        cells = root.findall('.//mxCell')
        print(f"📊 Found {len(diagrams)} diagram(s) and {len(cells)} cells")
        
        return True
        
    except ET.ParseError as e:
        print(f"❌ XML Parse Error in '{filepath}': {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: '{filepath}'")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "images/aws_landing_zone_financial_eu.drawio"
    
    validate_xml_file(filepath)