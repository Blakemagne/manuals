#!/usr/bin/env python3
"""
Complete workflow script to add a new manual to the sexy manuals site
"""

import os
import sys
import re
from pathlib import Path


def simplify_markdown(content, manual_name):
    """
    Convert complex sexy markdown to simple markdown that the parser can handle
    """
    lines = content.split('\n')
    result = []
    
    # Skip the sexy header stuff, create simple title
    title = manual_name.upper() + " Manual"
    result.append(f"# {title}")
    result.append("")
    
    # Extract a simple description from the content
    in_description = False
    description_found = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and complex formatting
        if not line or line.startswith('📚') or line.startswith('> *') or line.startswith('---'):
            i += 1
            continue
            
        # Look for the actual manual content (skip TOC)
        if line.startswith('## 📑 Table of Contents'):
            # Skip entire TOC section
            while i < len(lines) and not lines[i].strip().startswith('##'):
                i += 1
            continue
            
        # Start processing real sections
        if line.startswith('## ') and not '📑' in line:
            # Clean up section headers
            clean_header = re.sub(r'\{#.*?\}', '', line)  # Remove anchors
            clean_header = clean_header.replace('##', '##').strip()
            result.append(clean_header)
            result.append("")
            i += 1
            continue
            
        # Handle options with complex formatting
        if line.startswith('**`-') and line.endswith('`**'):
            # Extract the option and clean it up
            option_match = re.search(r'\*\*`([^`]+)`\*\*(.+)', line)
            if option_match:
                option = option_match.group(1)
                desc = option_match.group(2).strip()
                result.append(f"**{option}** {desc}")
            else:
                result.append(line)
            result.append("")
            i += 1
            continue
            
        # Handle regular content, but escape problematic characters
        if line:
            # Escape standalone underscores in file paths
            line = re.sub(r'~/\.(\w+)', r'**~/.\\1**', line)
            line = re.sub(r'/etc/(\w+)', r'**/etc/\\1**', line)
            
            # Fix unmatched quotes
            if line.count('"') % 2 == 1:
                line = line.replace('"', '`"`')
                
            result.append(line)
            
        i += 1
        
    return '\n'.join(result)


def update_homepage(manual_name, description="Command-line tool"):
    """
    Add the new manual to the homepage navigation
    """
    index_file = Path("public/content/index.md")
    
    if not index_file.exists():
        print(f"Error: {index_file} not found!")
        return False
        
    content = index_file.read_text()
    
    # Find the Available Manuals section
    new_link = f"- [{manual_name.upper()} - {description}](./{manual_name.lower()}.html) - {description}"
    
    # Look for the pattern and add our link
    pattern = r'(## Available Manuals.*?\n)(.*?)(\n## )'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        before = match.group(1)
        existing_links = match.group(2)
        after = match.group(3)
        
        # Add our new link
        updated_links = existing_links.rstrip() + '\n' + new_link
        updated_content = before + updated_links + after
        
        index_file.write_text(updated_content)
        print(f"✅ Added {manual_name} to homepage")
        return True
    else:
        print("⚠️  Could not find Available Manuals section to update")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 add_manual.py <manual_name>")
        print("Example: python3 add_manual.py git")
        sys.exit(1)
        
    manual_name = sys.argv[1].lower()
    
    print(f"🚀 Adding {manual_name} manual to sexy manuals site...")
    
    # Step 1: Check if sexy markdown exists
    sexy_file = Path(f"sexy_md/sexy_{manual_name}.md")
    if not sexy_file.exists():
        print(f"❌ {sexy_file} not found!")
        print(f"Please run: python3 sexy_formatter.py first")
        sys.exit(1)
        
    # Step 2: Convert sexy markdown to simple markdown
    print(f"📝 Converting {sexy_file} to simple format...")
    sexy_content = sexy_file.read_text()
    simple_content = simplify_markdown(sexy_content, manual_name)
    
    # Step 3: Write to content directory
    content_file = Path(f"public/content/{manual_name}.md")
    content_file.write_text(simple_content)
    print(f"✅ Created {content_file}")
    
    # Step 4: Update homepage
    print("🔗 Updating homepage navigation...")
    update_homepage(manual_name)
    
    # Step 5: Generate site
    print("🏗️  Generating HTML site...")
    os.chdir("public")
    result = os.system("python3 src/main.py")
    os.chdir("..")
    
    if result == 0:
        print(f"""
🎉 SUCCESS! {manual_name.upper()} manual added!

Your site now includes:
- /{manual_name}.html - The manual page
- Updated homepage with navigation link
- All files in docs/ ready for GitHub Pages

Next: Commit and push to deploy!
        """)
    else:
        print("❌ Error generating site. Check the markdown formatting.")


if __name__ == "__main__":
    main()