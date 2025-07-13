#!/usr/bin/env python3
"""
Auto-steal system that detects missing manual references and automatically steals them
"""

import os
import re
import subprocess
import sys
from pathlib import Path


def find_manual_references(content):
    """Find all manual references like command(1) in content"""
    pattern = r'\b([a-zA-Z][\w-]+)\((\d+[a-zA-Z]*)\)'
    matches = re.findall(pattern, content)
    return [(cmd, section) for cmd, section in matches]


def get_existing_manuals():
    """Get list of manual pages we already have"""
    existing = set()
    
    # Check og_man directory
    og_dir = Path("og_man")
    if og_dir.exists():
        for file in og_dir.glob("*.md"):
            existing.add(file.stem)
    
    # Check public/content directory
    content_dir = Path("public/content")
    if content_dir.exists():
        for file in content_dir.glob("*.md"):
            if file.stem != "index":
                existing.add(file.stem.replace("_sexy", ""))
    
    return existing


def manual_exists_on_system(command):
    """Check if a manual page exists on the system"""
    try:
        result = subprocess.run(['man', command], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def steal_manual(command):
    """Steal a manual page using the man command"""
    try:
        print(f"🏴‍☠️ Stealing {command} manual...")
        
        # Use man to get the manual content
        result = subprocess.run(['man', command], 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        
        if result.returncode == 0:
            # Save to og_man directory
            og_dir = Path("og_man")
            og_dir.mkdir(exist_ok=True)
            
            output_file = og_dir / f"{command}.md"
            with open(output_file, 'w') as f:
                f.write(result.stdout)
            
            print(f"✅ Stolen {command} manual ({len(result.stdout)} chars)")
            return True
        else:
            print(f"❌ Failed to steal {command}: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏱️ Timeout stealing {command}")
        return False
    except Exception as e:
        print(f"💥 Error stealing {command}: {e}")
        return False


def scan_for_missing_manuals():
    """Scan all existing manuals for references to missing manuals"""
    print("🔍 Scanning for missing manual references...")
    
    existing_manuals = get_existing_manuals()
    all_references = set()
    
    # Scan sexy_md files
    sexy_dir = Path("sexy_md")
    if sexy_dir.exists():
        for file in sexy_dir.glob("*.md"):
            try:
                content = file.read_text()
                refs = find_manual_references(content)
                all_references.update(cmd for cmd, section in refs)
            except Exception as e:
                print(f"⚠️ Error reading {file}: {e}")
    
    # Find missing manuals
    missing = all_references - existing_manuals
    
    print(f"📊 Found {len(all_references)} total references")
    print(f"✅ Have {len(existing_manuals)} manuals")
    print(f"❌ Missing {len(missing)} manuals")
    
    return missing


def auto_steal_missing():
    """Automatically steal missing manuals"""
    missing = scan_for_missing_manuals()
    
    if not missing:
        print("🎉 No missing manuals found!")
        return []
    
    print(f"\n🎯 Attempting to steal {len(missing)} missing manuals...")
    
    stolen = []
    failed = []
    
    for command in missing:
        if manual_exists_on_system(command):
            if steal_manual(command):
                stolen.append(command)
            else:
                failed.append(command)
        else:
            print(f"📋 {command} manual not available on system")
            failed.append(command)
    
    print(f"\n📈 Results:")
    print(f"✅ Successfully stolen: {len(stolen)}")
    print(f"❌ Failed: {len(failed)}")
    
    if stolen:
        print(f"\n🔄 Now run: python3 sexy_formatter.py")
        print("To format the newly stolen manuals!")
    
    return stolen


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--scan":
            scan_for_missing_manuals()
        elif sys.argv[1] == "--steal":
            if len(sys.argv) > 2:
                command = sys.argv[2]
                steal_manual(command)
            else:
                auto_steal_missing()
    else:
        auto_steal_missing()


if __name__ == "__main__":
    main()