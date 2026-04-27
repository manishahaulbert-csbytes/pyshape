#!/usr/bin/env python3
"""
Monorepo setup script - sets up the development environment
Usage: python scripts/setup.py
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, cwd=None):
    """Run a shell command and return the result."""
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    if result.stderr and result.returncode != 0:
        print(result.stderr, file=sys.stderr)
    
    return result.returncode == 0


def check_python_version():
    """Check if Python version is adequate."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")


def install_build_tools():
    """Install build tools."""
    print("\n📦 Installing build tools...")
    tools = ["build", "twine", "wheel"]
    
    for tool in tools:
        success = run_command([sys.executable, "-m", "pip", "install", tool])
        if not success:
            print(f"❌ Failed to install {tool}")
            return False
    
    return True


def install_monorepo_dependencies(monorepo_root):
    """Install monorepo development dependencies."""
    print("\n📦 Installing monorepo dependencies...")
    
    # Install root dependencies
    success = run_command([
        sys.executable, "-m", "pip", "install", "-e", ".[dev]"
    ], cwd=monorepo_root)
    
    return success


def install_packages_in_dev_mode(monorepo_root):
    """Install all packages in development mode."""
    print("\n📦 Installing packages in development mode...")
    
    packages_dir = monorepo_root / "packages"
    success = True
    
    for package_dir in packages_dir.iterdir():
        if package_dir.is_dir() and (package_dir / "pyproject.toml").exists():
            print(f"Installing {package_dir.name}...")
            success &= run_command([
                sys.executable, "-m", "pip", "install", "-e", "."
            ], cwd=package_dir)
    
    return success


def run_initial_tests(monorepo_root):
    """Run tests to verify setup."""
    print("\n🧪 Running initial tests to verify setup...")
    
    success = run_command([
        sys.executable, "-m", "pytest", 
        "packages/*/tests",
        "--verbose",
        "-x"  # Stop on first failure
    ], cwd=monorepo_root)
    
    return success


def create_vscode_settings(monorepo_root):
    """Create VS Code settings for the monorepo."""
    vscode_dir = monorepo_root / ".vscode"
    vscode_dir.mkdir(exist_ok=True)
    
    settings = {
        "python.defaultInterpreterPath": "./venv/bin/python",
        "python.testing.pytestEnabled": True,
        "python.testing.pytestArgs": [
            "packages/*/tests"
        ],
        "python.formatting.provider": "black",
        "python.linting.enabled": True,
        "python.linting.flake8Enabled": True,
        "files.exclude": {
            "**/__pycache__": True,
            "**/*.pyc": True,
            "**/.pytest_cache": True,
            "**/dist": True,
            "**/*.egg-info": True
        }
    }
    
    import json
    with open(vscode_dir / "settings.json", "w") as f:
        json.dump(settings, f, indent=2)
    
    print("✅ Created VS Code settings")


def main():
    """Main setup function."""
    print("🚀 Setting up PyShape Monorepo Development Environment")
    print("=" * 60)
    
    # Get monorepo root
    script_dir = Path(__file__).parent
    monorepo_root = script_dir.parent
    
    # Change to monorepo root
    os.chdir(monorepo_root)
    
    # Check Python version
    check_python_version()
    
    # Install build tools
    if not install_build_tools():
        print("\n❌ Failed to install build tools!")
        sys.exit(1)
    
    # Install monorepo dependencies
    if not install_monorepo_dependencies(monorepo_root):
        print("\n❌ Failed to install monorepo dependencies!")
        sys.exit(1)
    
    # Install packages in development mode
    if not install_packages_in_dev_mode(monorepo_root):
        print("\n❌ Failed to install packages in development mode!")
        sys.exit(1)
    
    # Create VS Code settings
    create_vscode_settings(monorepo_root)
    
    # Run initial tests
    if not run_initial_tests(monorepo_root):
        print("\n⚠️  Some tests failed, but setup is complete")
        print("   You may need to fix test issues manually")
    else:
        print("\n✅ All tests passed!")
    
    print("\n" + "=" * 60)
    print("🎉 Setup complete! You can now:")
    print("   • Run tests: python scripts/test_runner.py")
    print("   • Build packages: python scripts/build.py")
    print("   • Test specific package: python scripts/test_runner.py <package_name>")
    print("   • List packages: python scripts/test_runner.py --list")


if __name__ == "__main__":
    main()