import subprocess
import sys
import os
import platform
import webbrowser

def check_cpp_buildtools():
    try:
        subprocess.run(["cl"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing: {command}")
        return False
    return True

def main():
    if not check_cpp_buildtools():
        print("Microsoft Visual C++ Build Tools not found!")
        print("Opening browser to download Visual C++ Build Tools...")
        webbrowser.open("https://visualstudio.microsoft.com/visual-cpp-build-tools/")
        input("Press Enter after installing Visual C++ Build Tools to continue...")
    
    commands = [
        "python -m pip install --upgrade pip",
        "pip install --upgrade wheel setuptools",
        
        # Install Flask and its dependencies first
        "pip install Flask==2.0.1 Werkzeug==2.0.3 flask-wtf==1.0.0",
        
        # Install base dependencies
        "pip install pydantic==1.8.2",
        "pip install typing-extensions>=3.7.4,<4.0.0",
        
        # Install torch CPU version
        "pip install torch==1.10.0+cpu torchvision==0.11.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html",
        
        # Clean install spaCy
        "pip uninstall spacy -y",
        "pip install spacy==3.2.0",
        
        # Download spaCy model
        "python -m spacy download en_core_web_sm",
        
        # Install remaining requirements
        "pip install -r requirements.txt"
    ]
    
    for cmd in commands:
        if not run_command(cmd):
            print("Installation failed.")
            print("Please ensure:")
            print("1. Visual C++ Build Tools are properly installed")
            print("2. You have an active internet connection")
            print("3. You have sufficient permissions")
            print(f"Failed command: {cmd}")
            sys.exit(1)

    print("Installation completed successfully!")

if __name__ == "__main__":
    # Verify we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not sys.base_prefix != sys.prefix:
        print("Error: Not running in a virtual environment!")
        print("Please run this script using activate_env.bat")
        sys.exit(1)
    main()
