#!/usr/bin/env python3
"""
Monorepo build script - builds all packages or specific packages
Usage: python scripts/build.py [package_name]
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


def build_package(package_name, monorepo_root):
    """Build a specific package."""
    package_dir = monorepo_root / "packages" / package_name
    
    if not package_dir.exists():
        print(f"Package '{package_name}' not found!")
        return False
    
    print(f"\n{'='*60}")
    print(f"Building package: {package_name}")
    print(f"{'='*60}")
    
    # Clean previous builds
    dist_dir = package_dir / "dist"
    if dist_dir.exists():
        import shutil
        shutil.rmtree(dist_dir)
    
    # Build the package
    success = run_command([
        sys.executable, "-m", "build"
    ], cwd=package_dir)
    
    if success:
        print(f"✅ Successfully built {package_name}")
    else:
        print(f"❌ Failed to build {package_name}")
    
    return success


def install_package_in_dev_mode(package_name, monorepo_root):
    """Install a package in development mode."""
    package_dir = monorepo_root / "packages" / package_name
    
    print(f"Installing {package_name} in development mode...")
    return run_command([
        sys.executable, "-m", "pip", "install", "-e", "."
    ], cwd=package_dir)


def main():
    parser = argparse.ArgumentParser(description="Build monorepo packages")
    parser.add_argument("package", nargs="?", help="Package name to build (optional)")
    parser.add_argument("--list", action="store_true", help="List available packages")
    parser.add_argument("--dev-install", action="store_true", help="Install packages in development mode")
    
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
    
    packages_to_build = []
    
    if args.package:
        # Build specific package
        packages_to_build = [args.package]
    else:
        # Build all packages
        packages_to_build = get_packages(monorepo_root)
    
    success = True
    
    for package_name in packages_to_build:
        if args.dev_install:
            success &= install_package_in_dev_mode(package_name, monorepo_root)
        else:
            success &= build_package(package_name, monorepo_root)
    
    if success:
        if args.dev_install:
            print("\n✅ All packages installed in development mode!")
        else:
            print("\n✅ All packages built successfully!")
    else:
        if args.dev_install:
            print("\n❌ Some packages failed to install!")
        else:
            print("\n❌ Some packages failed to build!")
        sys.exit(1)


if __name__ == "__main__":
    main()