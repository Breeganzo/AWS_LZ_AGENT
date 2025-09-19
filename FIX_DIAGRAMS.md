# QUICK FIX: Install Graphviz to Generate Images

## The Problem
The agent is creating files but not generating actual images because Graphviz is not installed.

## SOLUTION 1: Manual Installation (Recommended)

### Step 1: Download Graphviz
1. Go to: https://graphviz.org/download/
2. Click on "Windows"
3. Download: `windows_10_cmake_Release_x64_graphviz-install-X.X.X-win64.exe`

### Step 2: Install
1. Run the downloaded .exe file
2. Follow the installation wizard
3. **IMPORTANT**: Remember the installation path (usually `C:\Program Files\Graphviz`)

### Step 3: Add to PATH
1. Press `Win + X` and select "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. In "System Variables", find "Path" and click "Edit"
5. Click "New" and add: `C:\Program Files\Graphviz\bin`
6. Click OK on all windows

### Step 4: Test
1. Close and reopen PowerShell
2. Run: `dot -V`
3. You should see version information

### Step 5: Run Agent Again
```powershell
python aws_diagram_agent.py
```

## SOLUTION 2: Alternative (if Solution 1 doesn't work)

Use Chocolatey package manager:
```powershell
# Install Chocolatey first (if not installed)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Then install Graphviz
choco install graphviz -y
```

## What You'll Get After Installation
- Beautiful PNG diagrams showing your AWS architecture
- Professional-looking diagrams with official AWS icons
- Visual representation of your SaaS hosting setup

## Current Workaround
For now, the agent provides detailed text-based architecture that shows the same information as the visual diagrams would contain.