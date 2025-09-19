# AWS Landing Zone Architecture Agent

## Overview
This project provides a comprehensive AWS Landing Zone Architecture Agent that acts as a consultant to design and deploy AWS Landing Zone architectures tailored to your business requirements. The agent:

- **Gathers Requirements**: Interactive questionnaire for industry, compliance, regions, and security needs
- **Provides Expert Recommendations**: Industry-specific best practices for Financial, Healthcare, Retail, and other sectors
- **Generates Visual Diagrams**: Automatically creates AWS architecture diagrams using official AWS stencils
- **Ensures Compliance**: Built-in support for GDPR, HIPAA, PCI-DSS, and other compliance frameworks
- **Follows AWS Best Practices**: Implements AWS Control Tower, Organizations, and multi-account strategies

## Key Features

### 🎯 Industry-Specific Architectures
- **Financial Services**: Multiple OUs with strict security, compliance monitoring, and dedicated production environments
- **Healthcare**: HIPAA-compliant architectures with data encryption and access controls
- **Retail**: Scalable, cost-optimized architectures with global content delivery
- **Manufacturing, Education, Other**: Standard multi-account setups with security best practices

### 🛡️ Compliance & Security
- **GDPR**: Data residency controls, encryption, and audit logging for EU operations
- **HIPAA**: Healthcare data protection with end-to-end encryption
- **PCI-DSS**: Payment card industry compliance with network segmentation
- **SOX, ISO 27001**: Additional compliance frameworks supported

### 📊 Visual Architecture Diagrams
- Automatically generated using official AWS stencils and icons
- Shows complete hierarchy: Control Tower → Organization → OUs → Accounts → VPCs → Resources
- Industry-specific resource recommendations (EC2, ECS, RDS, KMS, etc.)
- Compliance controls and security measures visualized

### 🏗️ AWS Landing Zone Components
- **AWS Control Tower**: Automated setup and governance
- **AWS Organizations**: Multi-account management with OUs
- **Security OU**: Centralized security and compliance controls
- **Production/Non-Production OUs**: Environment separation
- **IAM Identity Center**: Centralized identity management
- **CloudTrail & Config**: Comprehensive logging and compliance monitoring

## Architecture Patterns

The agent generates different architecture patterns based on your requirements:

1. **Financial Architecture**: Security OU + Non-Prod OU (Dev, QA, Performance, UAT) + Production OU
2. **Healthcare Architecture**: HIPAA-compliant with health data encryption and access controls
3. **Retail Architecture**: Scalable multi-environment setup with cost optimization
4. **Standard Architecture**: Core setup for other industries with essential security controls

## What You Get

When you run the agent, it will:
1. Ask about your industry, compliance needs, and security requirements
2. Generate detailed recommendations specific to your business
3. Create a visual architecture diagram showing:
   - AWS Control Tower setup
   - Organization structure with appropriate OUs
   - Account separation (Dev, QA, Prod, etc.)
   - VPC and networking architecture
   - Security and compliance controls
   - Industry-specific AWS services

## Technology Stack
- **Python**: Core application language
- **Questionary**: Interactive command-line questionnaires
- **Diagrams**: Automatic generation of architecture diagrams using official AWS icons
- **AWS Services**: Control Tower, Organizations, IAM, VPC, EC2, RDS, S3, KMS, CloudTrail

## File Structure
```
aws/
├── aws_diagram_agent.py    # Main agent application
├── README.md              # This file
├── HOW_TO_RUN.md         # Detailed setup and usage instructions
└── images/               # Generated architecture diagrams
```

## Quick Start
1. Install Python 3.8+ and required packages
2. Run `python aws_diagram_agent.py`
3. Answer the interactive questions
4. Review your customized recommendations and architecture diagram

For detailed setup instructions, see [HOW_TO_RUN.md](HOW_TO_RUN.md).

---
This agent provides enterprise-grade AWS Landing Zone architecture guidance following AWS Well-Architected Framework principles and industry best practices.