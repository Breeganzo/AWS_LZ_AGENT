#!/usr/bin/env python3

# Test script to generate SaaS diagram directly
import sys
import os
sys.path.append('.')
from aws_diagram_agent import generate_saas_drawio_diagram

print("Testing SaaS diagram generation...")

try:
    result = generate_saas_drawio_diagram(
        num_apps="7",
        num_environments="4 (Dev, QA, Pre-Prod, Prod)",
        app_type="Traditional applications with managed DB",
        filename="images/test_saas_7apps_enhanced",
        industry="SaaS Hosting Provider"
    )
    print(f"✅ {result}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()