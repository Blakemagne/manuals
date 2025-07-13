#!/usr/bin/env python3
"""
Sexy Pipeline - Complete workflow from stolen manual to deployed HTML
Usage: python3 sexy_pipeline.py [command_name]
"""

import os
import sys
import subprocess
from pathlib import Path
import shutil

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {description} failed")
        print(f"Command: {cmd}")
        print(f"Error: {result.stderr}")
        return False
    return True

def main():
    """Complete pipeline from stolen manual to deployed HTML"""
    
    # Check if we're in the right directory
    if not Path("sexy_formatter.py").exists():
        print("❌ Error: Run this script from the manuals root directory")
        sys.exit(1)
    
    # Create directories if they don't exist
    Path("og_man").mkdir(exist_ok=True)
    Path("sexy_md").mkdir(exist_ok=True)
    Path("public/content").mkdir(parents=True, exist_ok=True)
    
    print("🏴‍☠️ Starting Sexy Pipeline...")
    print("=" * 50)
    
    # Step 1: Format all manuals in og_man/ to sexy markdown
    if not run_command("python3 sexy_formatter.py", "Formatting manuals to sexy markdown"):
        sys.exit(1)
    
    # Step 2: Copy all sexy markdown files to site content
    print("🔄 Copying sexy markdown to site content...")
    sexy_files = list(Path("sexy_md").glob("sexy_*.md"))
    if not sexy_files:
        print("❌ Error: No sexy markdown files found in sexy_md/")
        sys.exit(1)
    
    for file in sexy_files:
        shutil.copy2(file, "public/content/")
    print(f"✅ Copied {len(sexy_files)} sexy markdown files")
    
    # Step 3: Generate HTML
    print("🔄 Generating HTML...")
    original_dir = os.getcwd()
    try:
        os.chdir("public")
        if not run_command("python3 src/main.py", "Generating HTML"):
            sys.exit(1)
    finally:
        os.chdir(original_dir)
    
    # Step 4: Count final files
    docs_files = list(Path("docs").glob("*.html"))
    print(f"✅ Generated {len(docs_files)} HTML files")
    
    print("=" * 50)
    print("🎉 Sexy Pipeline Complete!")
    print(f"📊 Summary:")
    print(f"   • {len(sexy_files)} sexy markdown files processed")
    print(f"   • {len(docs_files)} HTML files generated")
    print(f"   • Ready for deployment to GitHub Pages")
    print("")
    print("🚀 Next steps:")
    print("   git add docs/ && git commit -m 'Update manuals' && git push")

if __name__ == "__main__":
    main()