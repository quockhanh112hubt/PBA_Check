"""
Build script for PBA Function Checker
Builds Main.py into standalone executable
"""
import subprocess
import sys
import os
import shutil

def clean_build_folders():
    """Clean previous build folders"""
    print("\n[1/4] Cleaning previous build...")
    folders = ['build', 'dist', '__pycache__']
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"      Removed {folder}/")
    print("      Done!")

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    print("\n[2/4] Checking PyInstaller...")
    try:
        import PyInstaller
        print("      PyInstaller found!")
        return True
    except ImportError:
        print("      PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("      Installed!")
        return True

def build_executable():
    """Build executable using PyInstaller"""
    print("\n[3/4] Building executable...")
    try:
        subprocess.check_call([
            sys.executable, 
            "-m", 
            "PyInstaller", 
            "Main.spec", 
            "--clean", 
            "--noconfirm"
        ])
        print("      Done!")
        return True
    except subprocess.CalledProcessError:
        print("      BUILD FAILED!")
        return False

def copy_additional_files():
    """Copy additional required files to dist folder"""
    print("\n[4/4] Copying additional files...")
    
    if not os.path.exists('dist/PBA_Function_Checker.exe'):
        print("      ERROR: PBA_Function_Checker.exe not found!")
        return False
    
    # Copy folders
    folders = ['Resource', 'Logo']
    for folder in folders:
        if os.path.exists(folder):
            dest = f'dist/{folder}'
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(folder, dest)
            print(f"      Copied {folder}/")
    
    # Copy files
    files = ['config.json', 'version.txt']
    for file in files:
        if os.path.exists(file):
            shutil.copy2(file, 'dist/')
            print(f"      Copied {file}")
    
    print("      Done!")
    return True

def main():
    """Main build process"""
    print("=" * 50)
    print("  PBA Function Checker - Build Script")
    print("=" * 50)
    
    # Step 1: Clean
    clean_build_folders()
    
    # Step 2: Check PyInstaller
    if not check_pyinstaller():
        print("\nBUILD FAILED!")
        return False
    
    # Step 3: Build
    if not build_executable():
        print("\nBUILD FAILED!")
        return False
    
    # Step 4: Copy files
    if not copy_additional_files():
        print("\nBUILD FAILED!")
        return False
    
    # Success!
    print("\n" + "=" * 50)
    print("  BUILD SUCCESSFUL!")
    print("=" * 50)
    print("\n  Output: dist/PBA_Function_Checker.exe")
    print("\n  Files included:")
    print("  - PBA_Function_Checker.exe")
    print("  - config.json")
    print("  - version.txt")
    print("  - Resource folder")
    print("  - Logo folder")
    print("\n" + "=" * 50)
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
