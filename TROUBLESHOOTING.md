# Troubleshooting Guide

## Common Errors and Solutions

### 1. ModuleNotFoundError: No module named 'pip'

**Error message:**
```
ModuleNotFoundError: No module named 'pip'
```

**Solutions:**
1. Reinstall pip in the virtual environment:
```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

2. If that doesn't work, try manual pip installation:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### 2. Microsoft Visual C++ Build Tools Error

**Error message:**
```
Microsoft Visual C++ Build Tools not found!
```

**Solutions:**
1. Download and install Build Tools from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. During installation, select:
   - Workload "Desktop development with C++"
   - Individual components:
     - MSVC v140 - VS 2015 C++ build tools
     - Windows 10 SDK

### 3. Python Path Issues

**Error message:**
```
Python was not found; run without arguments to install from the Microsoft Store
```

**Solutions:**
1. Uninstall Microsoft Store Python
2. Download Python from python.org
3. During installation:
   - Check "Add Python to PATH"
   - Choose "Install for all users"
4. Restart your command prompt

### 4. Virtual Environment Creation Fails

**Error message:**
```
Error: Command '['python', '-m', 'venv', 'ncmenv']' returned non-zero exit status
```

**Solutions:**
1. Upgrade virtualenv:
```bash
python -m pip install --upgrade virtualenv
```

2. Create venv manually:
```bash
python -m virtualenv ncmenv
```

### 5. Pip Installation Errors

**Error message:**
```
ERROR: Could not install packages due to an OSError
```

**Solutions:**
1. Run command prompt as Administrator
2. Try installing with `--user` flag:
```bash
python -m pip install --user package_name
```

### 6. spaCy Model Download Fails

**Error message:**
```
[E050] Can't find model 'en_core_web_sm'
```

**Solutions:**
1. Install manually:
```bash
python -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.2.0/en_core_web_sm-3.2.0.tar.gz
```

### 7. Torch Installation Issues

**Error message:**
```
ERROR: Could not find a version that satisfies the requirement torch
```

**Solutions:**
1. Install CPU-only version:
```bash
python -m pip install torch==1.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
```

### 8. Permission Errors

**Error message:**
```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

**Solutions:**
1. Run as Administrator
2. Check folder permissions
3. Use `--user` flag:
```bash
python -m pip install --user -r requirements.txt
```

## General Troubleshooting Steps

1. Always run Command Prompt as Administrator
2. Make sure you have:
   - Python 3.8 or 3.9 (64-bit preferred)
   - Visual C++ Build Tools
   - Active internet connection
3. Clear pip cache if needed:
```bash
python -m pip cache purge
```

4. If all else fails, try clean setup:
```bash
rd /s /q ncmenv
python -m pip install --upgrade pip setuptools wheel
python -m venv ncmenv
call ncmenv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
```
