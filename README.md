# 🏗️ AWS Landing Zone Agent - Intelligent Cloud Architecture Consultant# 🏗️ AWS Landing Zone Architect



[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)## 🚀 Overview

[![Streamlit](https://img.shields.io/badge/Streamlit-1.49+-red.svg)](https://streamlit.io)

[![AWS](https://img.shields.io/badge/AWS-Architecture-orange.svg)](https://aws.amazon.com)**AWS Landing Zone Architect** is an intelligent, AI-powered consultant that helps design enterprise-grade AWS Landing Zone architectures tailored to your specific business, compliance, and security requirements. Built with modern web technologies and enhanced with AI capabilities, it provides comprehensive recommendations, professional documentation, and visual diagrams for AWS cloud infrastructure.



> **An AI-powered AWS architecture consultant that generates personalized landing zone recommendations, professional diagrams, and comprehensive documentation based on your specific requirements.**## ✨ Key Features



## 🌟 Features### 🎯 **Industry-Specific Architecture Patterns**

- **Financial Services**: PCI DSS compliant with dedicated security controls

### 🧠 **Intelligent Assessment**- **Healthcare & Life Sciences**: HIPAA compliant with PHI protection

- **Comprehensive Questionnaire**: 15+ detailed questions covering industry, compliance, scale, and technical requirements- **Government & Public Sector**: FedRAMP compliant with maximum security

- **AI-Powered Analysis**: Uses Google Gemini AI for intelligent pattern matching and recommendations- **Retail & E-commerce**: Scalable, cost-optimized global architectures

- **Industry-Specific Guidance**: Tailored recommendations for Financial Services, Healthcare, Government, Technology, and more- **Manufacturing, Education, Technology**: Customized patterns for each industry



### 🏗️ **Architecture Patterns**### 🧠 **AI-Powered Intelligence**

- **Single Account Setup**: For small teams and simple workloads- **Google Gemini Integration**: Advanced AI insights and recommendations

- **AWS Landing Zone Standard**: Enterprise-grade multi-account structure with Control Tower- **Implementation Guidance**: AI-generated best practices and migration strategies

- **Financial Services**: PCI DSS compliant architecture with enhanced security- **Risk Assessment**: Potential challenges and mitigation strategies

- **Healthcare**: HIPAA-compliant setup with data protection controls- **Cost Optimization**: AI-suggested cost optimization opportunities

- **Government**: FedRAMP-ready architecture for public sector

### 🎨 **Dual Diagram Generation**

### 🎨 **Professional Diagrams**- **Mermaid.js Diagrams**: Web-friendly, interactive diagrams for presentations

- **Mermaid.js Diagrams**: Web-friendly, interactive diagrams- **Draw.io XML**: Professional diagrams with official AWS stencils for desktop editing

- **Draw.io XML Export**: Desktop-friendly diagrams for detailed editing- **Industry-Specific Visuals**: Compliance controls and security measures highlighted

- **Automatic File Organization**: Diagrams saved in organized directories- **Multi-Format Export**: PNG, SVG, PDF, and editable formats

- **Multiple Export Formats**: Download or save to structured folders

### 📑 **Professional Export Capabilities**

### 📊 **Smart Decision Matrix**- **📄 Word Documents**: Professionally formatted reports with implementation details

- **Pattern Scoring**: Intelligent scoring based on your requirements- **📋 JSON**: Machine-readable format for automation and integration

- **Compliance Mapping**: Automatic compliance framework selection- **📝 Markdown**: Documentation-friendly format for wikis and repositories

- **Cost Optimization**: Recommendations based on team size and usage patterns- **🎨 Draw.io Files**: Editable diagrams for further customization

- **Regional Considerations**: Multi-region deployment strategies

### 🛡️ **Comprehensive Compliance Support**

### 📑 **Export & Documentation**- **GDPR**: EU data residency and privacy controls

- **Word Documents**: Professional architecture reports- **HIPAA**: Healthcare data protection and audit trails

- **JSON Export**: Machine-readable configuration data- **PCI DSS**: Payment card industry security standards

- **Markdown Reports**: Version-control friendly documentation- **SOX**: Financial reporting compliance

- **Diagram Files**: Organized in `images/mermaid/` and `images/drawio/`- **FedRAMP**: Government security authorization

- **ISO 27001**: Information security management

## 🚀 Quick Start

### 🌍 **Global Multi-Region Support**

### Prerequisites- **15+ AWS Regions**: Support for global deployments

- Python 3.8 or higher- **Data Residency**: Region-specific compliance controls

- Internet connection (for AI features)- **Disaster Recovery**: Multi-region backup and failover strategies

- **Global Load Balancing**: Route 53 and CloudFront integration

### 1. Install Dependencies

```bash## 🏗️ Architecture Patterns

pip install -r requirements.txt

```### 🏢 **Single Account Architecture**

- **Use Case**: Small organizations (1-5 applications)

### 2. Configure Environment (Optional)- **Structure**: Environment separation via VPCs

Create a `.env` file for AI features:- **Benefits**: Simple management, cost-effective

```bash- **Best For**: Startups, simple workloads, development environments

# Copy the template

cp .env.example .env### 🏭 **Multi-Account Basic Architecture**

- **Use Case**: Medium organizations (5-20 applications)

# Add your Google AI API key (optional - works without it)- **Structure**: Separate accounts per environment

GEMINI_API_KEY=your_api_key_here- **Benefits**: Clear environment isolation, basic governance

```- **Best For**: Growing teams, basic compliance needs



### 3. Launch the Application### 🏛️ **AWS Landing Zone Standard**

```bash- **Use Case**: Enterprise organizations (20+ applications)

streamlit run src/app.py- **Structure**: Control Tower with Security, Production, and Non-Production OUs

```- **Benefits**: Enterprise governance, standardized security

- **Best For**: Large enterprises, multiple business units

### 4. Access the Web Interface

Open your browser to: `http://localhost:8501`### 🏦 **Financial Services Landing Zone**

- **Use Case**: Financial institutions and fintech

## 📖 How to Use- **Structure**: Enhanced security with PCI DSS and SOX compliance

- **Benefits**: Regulatory compliance, audit trails, data protection

### Step 1: Complete the Assessment- **Best For**: Banks, payment processors, financial services

1. **Launch the app** and click "🚀 Start Architecture Assessment"

2. **Answer the questionnaire** - 15 comprehensive questions about:### 🏥 **Healthcare Landing Zone**

   - Industry and compliance requirements- **Use Case**: Healthcare organizations and life sciences

   - Application scale and workload types- **Structure**: HIPAA-compliant with PHI protection

   - Security and networking needs- **Benefits**: Healthcare compliance, data encryption, access controls

   - Team size and automation preferences- **Best For**: Hospitals, healthcare providers, medical device companies

   - Timeline and budget considerations

### 🏛️ **Government Landing Zone**

### Step 2: Review Recommendations- **Use Case**: Government agencies and contractors

The AI will analyze your responses and provide:- **Structure**: FedRAMP authorized with maximum security

- **Recommended Architecture Pattern** with detailed explanation- **Benefits**: Government compliance, classified data handling

- **Industry-Specific Compliance** guidance- **Best For**: Federal agencies, defense contractors, public sector

- **AWS Services List** tailored to your needs

- **Implementation Timeline** and cost considerations### 🌐 **Hybrid Cloud Architecture**

- **Use Case**: Legacy system integration

### Step 3: Generate Professional Diagrams- **Structure**: AWS with on-premises connectivity

Choose your preferred diagram format:- **Benefits**: Gradual migration, hybrid workloads

- **🌐 Mermaid (Web-friendly)**: Interactive diagrams for presentations- **Best For**: Large enterprises with existing infrastructure

- **🖥️ Draw.io XML (Desktop-friendly)**: Editable diagrams for detailed work

- **📂 Both (Save to Files)**: Automatically organized in project folders### 🌍 **Multi-Region Architecture**

- **Use Case**: Global organizations

### Step 4: Export Documentation- **Structure**: Geographically distributed across multiple regions

- **📄 Word Report**: Comprehensive architecture documentation- **Benefits**: Disaster recovery, global reach, data residency

- **📋 JSON Export**: Configuration data for automation- **Best For**: International companies, high availability requirements

- **📝 Markdown**: Developer-friendly documentation

## 📋 Comprehensive Assessment

## 📁 Project Structure

### 🎯 **15-Question Assessment**

```1. **Industry Classification**: 9+ industry options

aws/2. **Application Portfolio**: 1-100+ applications

├── src/                          # Core application code3. **Compliance Requirements**: 10+ compliance frameworks

│   ├── agent.py                  # Main AI agent with Gemini integration4. **Data Residency**: Regional and sovereignty requirements

│   ├── app.py                    # Streamlit web interface5. **AWS Regions**: 13+ supported regions

│   ├── decision_matrix.py        # Architecture pattern scoring6. **Security Posture**: 4 security levels

│   ├── diagram_generator.py      # Mermaid & Draw.io diagram generation7. **Workload Types**: 12+ workload categories

│   └── questionnaire.py          # Assessment questions management8. **Environment Strategy**: 5+ account organization patterns

├── data/9. **Network Connectivity**: 7+ connectivity options

│   └── questionnaire.json        # Comprehensive assessment questions10. **Backup & Recovery**: 6+ backup strategies

├── templates/11. **Cost Optimization**: 5+ cost approaches

│   └── diagrams.json            # Diagram templates and patterns12. **Team Size**: 6+ team size categories

├── images/                       # Generated diagrams (auto-created)13. **Automation Level**: 5+ automation levels

│   ├── mermaid/                 # Mermaid diagram files (.md)14. **Monitoring Requirements**: 8+ monitoring options

│   └── drawio/                  # Draw.io XML files (.drawio)15. **Implementation Timeline**: 6+ timeline options

├── .vscode/                     # VS Code configuration

├── requirements.txt             # Python dependencies## 🚀 Quick Start

├── .env.example                 # Environment variables template

└── README.md                    # This file### **1. Prerequisites**

``````bash

# Python 3.8 or higher

## 🔧 Architecture Patternspython --version



### 🏢 **Single Account**# Git (for cloning)

- **Best for**: Small teams (1-5 people), simple workloadsgit --version

- **Use cases**: Startups, proof of concepts, development environments```

- **Services**: Single AWS account with VPC separation

### **2. Installation**

### 🏗️ **AWS Landing Zone Standard**```bash

- **Best for**: Enterprise organizations (20+ applications)# Clone the repository

- **Use cases**: Multi-team environments, compliance requirementsgit clone https://github.com/kyndryl-global-delivery/aws-landing-zone-architect.git

- **Services**: AWS Control Tower, Organizations with OUs, centralized loggingcd aws-landing-zone-architect



### 🏦 **Financial Services**# Install dependencies

- **Best for**: Banks, fintech, payment processorspip install -r requirements.txt

- **Use cases**: PCI DSS compliance, sensitive financial data```

- **Services**: Enhanced monitoring, dedicated compliance account

### **3. Configuration (Optional)**

### 🏥 **Healthcare**```bash

- **Best for**: Healthcare providers, medical device companies# Copy environment template

- **Use cases**: HIPAA compliance, patient data protectioncp .env.template .env

- **Services**: Encrypted storage, audit trails, access controls

# Add your Gemini AI API key (for enhanced insights)

### 🏛️ **Government**# Edit .env file and add: GEMINI_API_KEY=your_api_key_here

- **Best for**: Public sector, government agencies```

- **Use cases**: FedRAMP compliance, classified workloads

- **Services**: GovCloud regions, enhanced security controls### **4. Run the Application**

```bash

## 🛠️ Technical Features# Start the Streamlit web application

streamlit run src/app.py

### AI Integration

- **Google Gemini AI**: Advanced natural language processing for intelligent recommendations# Open your browser to: http://localhost:8501

- **Fallback Mode**: Works without API key with predefined logic```

- **Context-Aware**: Considers industry, scale, and compliance together

### **5. Alternative: Command Line Interface**

### Diagram Generation```bash

- **Dual Format Support**: Both Mermaid.js and Draw.io XML# Use the original command-line interface

- **Automatic Organization**: Files saved with timestamps and proper namingpython aws_diagram_agent.py

- **XML Compliance**: Proper entity escaping for Draw.io compatibility```

- **Rich Visualizations**: AWS service icons and professional layouts

## 💡 Usage Guide

### Decision Engine

- **Multi-Factor Scoring**: Weighs compliance, scale, complexity, and cost### **🎯 Web Interface (Recommended)**

- **Pattern Matching**: Intelligent selection from multiple architecture patterns1. **Start Assessment**: Click "Start AWS Assessment" on the welcome page

- **Customization**: Industry-specific modifications and recommendations2. **Answer Questions**: Progress through the 15-question assessment

3. **Review Recommendations**: Get AI-powered architecture recommendations

## 📋 Requirements4. **Choose Diagram Format**: Select Mermaid (web) or Draw.io (desktop)

5. **Export Results**: Download in multiple formats (Word, JSON, Markdown, Draw.io)

### Dependencies

```### **📊 What You'll Get**

streamlit==1.49.1- **Architecture Recommendation**: Industry-specific pattern with confidence score

google-generativeai==0.8.3- **AI Insights**: Implementation guidance, challenges, and best practices

python-dotenv==1.0.1- **Visual Diagrams**: Professional AWS architecture diagrams

python-docx==1.1.2- **Implementation Plan**: Step-by-step deployment guidance

pandas==2.2.3- **Export Options**: Multiple formats for different use cases

plotly==5.24.1

requests==2.32.3## 🛠️ Technology Stack

streamlit-mermaid==0.1.0

mermaid-py==0.3.0### **Frontend**

```- **Streamlit**: Modern web UI framework

- **Streamlit-Mermaid**: Interactive diagram rendering

### System Requirements- **HTML/CSS/JavaScript**: Custom UI components

- **Python**: 3.8 or higher

- **Memory**: 512MB RAM minimum### **Backend**

- **Storage**: 100MB for application and generated files- **Python 3.8+**: Core application language

- **Network**: Internet connection for AI features (optional)- **Google Gemini AI**: Advanced AI insights and recommendations

- **Decision Matrix**: Rule-based architecture scoring

## 🌍 Supported Regions

### **Diagram Generation**

The agent provides recommendations for all major AWS regions with special focus on:- **Mermaid.js**: Web-native diagram generation

- **US East/West**: Standard deployments- **Draw.io XML**: Professional diagram export

- **Europe**: GDPR compliance considerations- **Official AWS Icons**: Enterprise-grade visual assets

- **Asia Pacific**: Data residency requirements

- **GovCloud**: Government and compliance workloads### **Export Formats**

- **python-docx**: Professional Word document generation

## 🔒 Security & Compliance- **JSON**: Machine-readable data format

- **Markdown**: Documentation-friendly format

### Compliance Frameworks Supported- **XML**: Draw.io compatible diagrams

- **GDPR**: European data protection regulation

- **HIPAA**: Healthcare data protection## 📁 Project Structure

- **PCI DSS**: Payment card industry standards

- **SOX**: Sarbanes-Oxley financial compliance```

- **FedRAMP**: Federal risk and authorization managementaws-landing-zone-architect/

- **ISO 27001**: Information security management├── src/                          # Source code

│   ├── app.py                   # Main Streamlit application

### Security Features│   ├── agent.py                 # Core agent logic and AI integration

- **No Data Storage**: Assessment data not permanently stored│   ├── questionnaire.py         # Assessment questionnaire engine

- **Environment Variables**: Secure API key management│   ├── decision_matrix.py       # Architecture decision algorithms

- **Local Processing**: Diagrams generated locally│   └── diagram_generator.py     # Dual diagram generation

- **Export Control**: User controls all data export├── data/                        # Configuration data

│   └── questionnaire.json      # Assessment questions and logic

## 🎯 Use Cases├── templates/                   # Diagram templates

│   └── diagrams.json           # Mermaid diagram templates

### 🏢 **Enterprise Migration**├── images/                      # Generated diagrams (auto-created)

- Legacy system modernization├── exports/                     # Export downloads (auto-created)

- Multi-account strategy planning├── .env.template               # Environment configuration template

- Compliance requirement mapping├── .env.example               # Example environment setup

- Cost optimization analysis├── requirements.txt           # Python dependencies

├── aws_diagram_agent.py      # Legacy command-line interface

### 🚀 **Startup Scaling**├── README.md                 # This documentation

- Simple to complex architecture evolution└── .vscode/                  # VS Code configuration

- Compliance preparation    ├── launch.json          # Debug configurations

- Team growth planning    └── settings.json        # Editor settings

- Technology stack recommendations```



### 🏛️ **Compliance Projects**## ⚙️ Configuration

- Regulatory requirement analysis

- Security control implementation### **Environment Variables**

- Audit preparation```bash

- Documentation generation# Required for AI insights (optional but recommended)

GEMINI_API_KEY=your_gemini_api_key_here

### 🔄 **Architecture Reviews**

- Current state assessment# Application settings

- Best practice validationAPP_NAME=AWS Landing Zone Architect

- Optimization opportunitiesAPP_VERSION=2.0

- Future state planningDEBUG=False



## 🤝 Contributing# Export directories

EXPORT_DIR=exports

This is a Kyndryl internal project. For contributions or feature requests, please contact the development team.DIAGRAMS_DIR=diagrams

```

## 📞 Support

### **Getting Gemini AI API Key**

For technical support or questions:1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)

- **Internal Teams**: Contact via Slack or internal support channels2. Sign in with your Google account

- **Documentation**: Check this README and inline code documentation3. Create a new API key

- **Issues**: Report via internal issue tracking system4. Add to your `.env` file: `GEMINI_API_KEY=your_key_here`



## 📄 License## 🔧 Development



© 2025 Kyndryl. Internal use only.### **Running in Development Mode**

```bash

---# Install development dependencies

pip install -r requirements.txt

## 🚀 **Ready to Start?**

# Run with debug enabled

1. **Install dependencies**: `pip install -r requirements.txt`streamlit run src/app.py --server.runOnSave true

2. **Launch the app**: `streamlit run src/app.py`

3. **Open your browser**: `http://localhost:8501`# Run tests (if available)

4. **Begin assessment**: Click "🚀 Start Architecture Assessment"python -m pytest tests/

```

**Your first AWS architecture is just a few questions away!** 🎉
### **Adding New Architecture Patterns**
1. **Update Decision Matrix**: Add new pattern in `src/decision_matrix.py`
2. **Add Diagram Templates**: Include Mermaid template in `templates/diagrams.json`
3. **Update Diagram Generator**: Add Draw.io XML generation logic
4. **Test**: Verify pattern selection and diagram generation

### **Customizing Questions**
1. **Edit Questionnaire**: Modify `data/questionnaire.json`
2. **Update Logic**: Adjust conditional logic in `src/questionnaire.py`
3. **Test Assessment**: Verify question flow and validation

## 🌟 Advanced Features

### **🔄 API Integration Potential**
- REST API endpoints for automation
- Integration with AWS APIs for real-time validation
- CI/CD pipeline integration for infrastructure as code

### **📊 Analytics and Reporting**
- Assessment analytics and trends
- Recommendation success tracking
- Usage patterns and optimization insights

### **🎨 Customization Options**
- Brand customization for consultants
- Custom compliance frameworks
- Organization-specific templates

## 🤝 Contributing

We welcome contributions to improve the AWS Landing Zone Architect:

### **🐛 Bug Reports**
- Use GitHub Issues to report bugs
- Include detailed reproduction steps
- Provide environment information

### **💡 Feature Requests**
- Submit enhancement ideas via GitHub Issues
- Describe the use case and expected benefits
- Consider implementation complexity

### **🔧 Pull Requests**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and test thoroughly
4. Commit with descriptive messages
5. Push and submit a pull request

## 📝 License

This project is part of Kyndryl's cloud architecture consulting tools and is intended for internal and client use. Please refer to the LICENSE file for specific terms and conditions.

## 🆘 Support

### **📞 Getting Help**
- **Issues**: Create GitHub Issues for bugs and feature requests
- **Documentation**: Refer to this README and inline code documentation
- **Community**: Join discussions in GitHub Discussions

### **🔍 Troubleshooting**

**Common Issues:**
1. **Streamlit Not Starting**: Check Python version (3.8+) and dependencies
2. **AI Insights Not Working**: Verify GEMINI_API_KEY in .env file
3. **Diagram Generation Errors**: Ensure all dependencies are installed
4. **Export Failures**: Check file permissions and disk space

**Debug Mode:**
```bash
# Enable debug logging
export DEBUG=True
streamlit run src/app.py
```

## 🏆 Awards and Recognition

- **AWS Well-Architected**: Follows AWS best practices and design principles
- **Industry Standards**: Supports major compliance frameworks
- **Enterprise Ready**: Designed for large-scale enterprise deployments

## 🔮 Roadmap

### **📅 Upcoming Features**
- **Q1 2024**: AWS API integration for real-time validation
- **Q2 2024**: Cost estimation and optimization recommendations
- **Q3 2024**: Terraform/CloudFormation template generation
- **Q4 2024**: Advanced security scanning and recommendations

### **🎯 Long-term Vision**
- Full Infrastructure as Code generation
- Real-time AWS environment scanning
- Automated compliance monitoring
- Integration with AWS Control Tower APIs

---

**🚀 Ready to architect your AWS Landing Zone?** 

Run `streamlit run src/app.py` and begin your comprehensive AWS assessment!