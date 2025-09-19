# How to Run the AWS Landing Zone Architecture Agent

## Prerequisites

### System Requirements
- **Python 3.8 or higher**
- **Windows, macOS, or Linux**
- **Internet connection** (for downloading Python packages)

### Required Python Packages
The agent requires the following Python packages:
- `diagrams` - For generating AWS architecture diagrams
- `questionary` - For interactive command-line questionnaires
- `Pillow` - Image processing (dependency for diagrams)
- `graphviz` - Graph visualization (dependency for diagrams)

## Installation Steps

### Step 1: Install Python
If you don't have Python installed:
1. Download Python from [python.org](https://python.org)
2. Install Python 3.8 or higher
3. Ensure Python is added to your system PATH

### Step 2: Install Graphviz (CRITICAL - Required for Diagrams)

**⚠️ IMPORTANT**: Graphviz must be installed on your system for diagram generation to work.

**On Windows:**
1. Download Graphviz from [graphviz.org](https://graphviz.org/download/)
2. Download the Windows installer (e.g., `windows_10_cmake_Release_x64_graphviz-install-X.X.X-win64.exe`)
3. Run the installer and install Graphviz
4. **CRITICAL**: Add Graphviz to your system PATH:
   - Open System Properties → Advanced → Environment Variables
   - Edit the "Path" variable in System Variables
   - Add `C:\Program Files\Graphviz\bin` (or wherever you installed it)
   - Click OK and restart your command prompt
5. Verify installation by running: `dot -V`

**Alternative Windows Installation using Chocolatey:**
```powershell
# If you have Chocolatey installed
choco install graphviz
```

**On macOS:**
```bash
brew install graphviz
```

**On Linux (Ubuntu/Debian):**
```bash
sudo apt-get install graphviz
```

### Step 3: Install Python Dependencies
Open a terminal/command prompt in the project directory and run:

```powershell
# Install required packages
pip install diagrams questionary Pillow
```

If you encounter permission issues, try:
```powershell
pip install --user diagrams questionary Pillow
```

### Step 4: Verify Installation
Test that everything is installed correctly:
```powershell
python -c "import diagrams, questionary; print('All packages installed successfully!')"
```

## Running the Agent

### Basic Usage
1. Open a terminal/command prompt
2. Navigate to the project directory:
   ```powershell
   cd "C:\Users\YourUsername\OneDrive - kyndryl\Documents\aws"
   ```
3. Run the agent:
   ```powershell
   python aws_diagram_agent.py
   ```

### What to Expect
The agent will guide you through an interactive questionnaire:

1. **Industry Selection**: Choose from Financial, Healthcare, Retail, Manufacturing, Education, or Other
2. **Compliance Requirements**: Select applicable frameworks (GDPR, HIPAA, PCI-DSS, SOX, ISO 27001)
3. **Region/Country**: Specify your primary region (US, EU, APAC, etc.)
4. **Security Level**: Choose Standard, High, or Very High
5. **Environment Count**: Specify number of environments needed

### Sample Interaction
```
🚀 AWS Landing Zone Architecture Agent
=====================================
This agent will help you design a comprehensive AWS Landing Zone
architecture based on your business requirements.

? What industry is your organization in? Financial
? Select your compliance requirements: GDPR, PCI-DSS
? What is your primary region/country? (e.g., US, EU, APAC): EU
? What is your required security level? High
? How many environments do you need? (e.g., Dev, QA, Prod): 5

============================================================
=== AWS LANDING ZONE RECOMMENDATIONS ===
Industry: Financial
Compliance: GDPR, PCI-DSS
Region: EU
Security Level: High

FINANCIAL INDUSTRY RECOMMENDATIONS:
• Use AWS Control Tower for governance and compliance
• Implement multiple OUs: Security, Non-Production, Production
• Enable AWS Config for compliance monitoring
...

🎨 Generating architecture diagram...
✅ Architecture diagram generated successfully!
📁 Location: images/aws_landing_zone_financial_eu.png
```

## Output Files

### Generated Diagrams
The agent creates architecture diagrams in the `images/` folder with names like:
- `aws_landing_zone_financial_eu.png`
- `aws_landing_zone_healthcare_us.png`
- `aws_landing_zone_retail_apac.png`

### Diagram Contents
Each diagram shows:
- **AWS Control Tower** setup
- **AWS Organization** structure
- **Organizational Units (OUs)** for different environments
- **AWS Accounts** (Dev, QA, Prod, Security, etc.)
- **VPCs and networking** architecture
- **Security services** (KMS, IAM, CloudTrail)
- **Industry-specific services** (RDS, ECS, S3, etc.)
- **Compliance controls** based on your requirements

## Troubleshooting

### Common Issues

**Error: "failed to execute WindowsPath('dot'), make sure the Graphviz executables are on your systems' PATH"**
- **Solution**: This is the most common error. Graphviz is not properly installed or not in PATH.
  1. Download and install Graphviz from [graphviz.org](https://graphviz.org/download/)
  2. Add `C:\Program Files\Graphviz\bin` to your system PATH
  3. Restart your command prompt/terminal
  4. Test with: `dot -V`
  5. If still not working, try installing via Chocolatey: `choco install graphviz`

**Error: "diagrams module not found"**
- Solution: Install the diagrams package: `pip install diagrams`

**Error: "graphviz not found"**
- Solution: Install Graphviz system package and add to PATH

**Error: Permission denied**
- Solution: Use `pip install --user` or run as administrator

**Error: "No module named 'questionary'"**
- Solution: Install questionary: `pip install questionary`

**Diagram not generating**
- Check that the `images/` directory exists
- Ensure Graphviz is properly installed and in PATH
- Try running with administrator privileges

### Verification Commands
```powershell
# Check Python version
python --version

# Check if packages are installed
pip list | grep diagrams
pip list | grep questionary

# Test Graphviz
dot -V
```

## Advanced Usage

### Custom Modifications
You can modify `aws_diagram_agent.py` to:
- Add new industry types
- Include additional compliance frameworks
- Customize diagram layouts
- Add more AWS services
- Integrate with external APIs

### Batch Processing
For multiple organizations, you can modify the script to read requirements from a configuration file instead of interactive input.

## Next Steps After Running the Agent

1. **Review the Generated Diagram**: Open the PNG file in the `images/` folder
2. **Study the Recommendations**: Follow the detailed recommendations printed by the agent
3. **Implement AWS Control Tower**: Set up Control Tower in your AWS organization
4. **Create Organizational Units**: Implement the recommended OU structure
5. **Deploy Security Controls**: Apply the recommended security and compliance measures
6. **Validate Architecture**: Ensure the implementation matches the generated diagram

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Ensure all Python packages are installed correctly
4. Review the generated recommendations and diagrams

---
This agent provides a starting point for AWS Landing Zone design. For production implementation, consult with AWS architects and follow the AWS Well-Architected Framework.