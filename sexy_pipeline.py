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
    
    # Step 2: Auto-steal missing referenced manuals (with timeout)
    print("🔄 Auto-stealing missing referenced manuals...")
    try:
        result = subprocess.run("python3 auto_steal.py", shell=True, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("✅ Auto-steal completed")
        else:
            print("⚠️  Warning: Auto-steal had issues, continuing anyway...")
    except subprocess.TimeoutExpired:
        print("⚠️  Warning: Auto-steal timed out (60s), continuing anyway...")
    except Exception as e:
        print(f"⚠️  Warning: Auto-steal failed ({e}), continuing anyway...")
    
    # Step 3: Copy all sexy markdown files to site content
    print("🔄 Copying sexy markdown to site content...")
    sexy_files = list(Path("sexy_md").glob("sexy_*.md"))
    if not sexy_files:
        print("❌ Error: No sexy markdown files found in sexy_md/")
        sys.exit(1)
    
    for file in sexy_files:
        shutil.copy2(file, "public/content/")
    print(f"✅ Copied {len(sexy_files)} sexy markdown files")
    
    # Step 4: Generate HTML with static site generator
    print("🔄 Generating HTML with static site generator...")
    original_dir = os.getcwd()
    try:
        os.chdir("public")
        if not run_command("python3 src/main.py", "Generating HTML"):
            sys.exit(1)
    finally:
        os.chdir(original_dir)
    
    # Step 5: Organize manuals into categories
    if not run_command("python3 organize_manuals.py", "Organizing manuals by category"):
        print("⚠️  Warning: Organization failed, continuing...")
    
    # Step 6: Regenerate HTML with organized structure
    print("🔄 Regenerating HTML with organized structure...")
    try:
        os.chdir("public")
        if not run_command("python3 src/main.py", "Regenerating organized HTML"):
            sys.exit(1)
    finally:
        os.chdir(original_dir)
    
    # Step 7: Count final files and categories
    docs_files = list(Path("docs").rglob("*.html"))
    docs_dir = Path("docs")
    categories = len([d for d in docs_dir.iterdir() if d.is_dir() and d.name not in ['.git', '__pycache__']]) if docs_dir.exists() else 0
    
    # Also count from the organize_manuals output if available
    if categories == 0:
        # Fallback: count unique category prefixes in organized files
        category_dirs = set()
        for html_file in docs_files:
            if '/' in str(html_file.relative_to(docs_dir)):
                category = str(html_file.relative_to(docs_dir)).split('/')[0]
                if category != 'docs':
                    category_dirs.add(category)
        categories = len(category_dirs)
    
    print(f"✅ Generated {len(docs_files)} HTML files organized into {categories} categories")
    
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