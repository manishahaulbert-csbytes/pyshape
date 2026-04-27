#!/usr/bin/env python3
"""
Monorepo test runner - runs tests for all packages or specific packages
Usage: python scripts/test_runner.py [package_name]
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_command(command, cwd=None):
    """Run a shell command and return the result."""
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    return result.returncode == 0


def get_packages(monorepo_root):
    """Get list of available packages."""
    packages_dir = monorepo_root / "packages"
    if not packages_dir.exists():
        return []
    
    packages = []
    for item in packages_dir.iterdir():
        if item.is_dir() and (item / "pyproject.toml").exists():
            packages.append(item.name)
    
    return packages


def run_package_tests(package_name, monorepo_root):
    """Run tests for a specific package."""
    package_dir = monorepo_root / "packages" / package_name
    
    if not package_dir.exists():
        print(f"Package '{package_name}' not found!")
        return False
    
    print(f"\n{'='*60}")
    print(f"Testing package: {package_name}")
    print(f"{'='*60}")
    
    # Run pytest for the specific package
    return run_command([
        sys.executable, "-m", "pytest", 
        f"packages/{package_name}/tests",
        "--verbose",
        f"--cov=packages/{package_name}/src",
        "--cov-report=term-missing"
    ], cwd=monorepo_root)


def run_all_tests(monorepo_root):
    """Run tests for all packages."""
    print(f"\n{'='*60}")
    print("Running tests for all packages")
    print(f"{'='*60}")
    
    # Run pytest for all packages
    return run_command([
        sys.executable, "-m", "pytest",
        "packages/*/tests",
        "--verbose",
        "--cov=packages",
        "--cov-report=term-missing",
        "--cov-report=xml"
    ], cwd=monorepo_root)


def main():
    parser = argparse.ArgumentParser(description="Run tests for monorepo packages")
    parser.add_argument("package", nargs="?", help="Package name to test (optional)")
    parser.add_argument("--list", action="store_true", help="List available packages")
    
    args = parser.parse_args()
    
    # Get monorepo root
    script_dir = Path(__file__).parent
    monorepo_root = script_dir.parent
    
    # List packages if requested
    if args.list:
        packages = get_packages(monorepo_root)
        print("Available packages:")
        for package in packages:
            print(f"  - {package}")
        return
    
    # Change to monorepo root
    os.chdir(monorepo_root)
    
    success = True
    
    if args.package:
        # Test specific package
        success = run_package_tests(args.package, monorepo_root)
    else:
        # Test all packages
        success = run_all_tests(monorepo_root)
    
    if success:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()