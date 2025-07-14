#!/usr/bin/env python3
"""
Sexy Manual Formatter - Transform boring manual pages into beautiful markdown
"""

import re
import os
import sys
from pathlib import Path


class SexyFormatter:
    def __init__(self):
        self.sections = []
        self.toc_entries = []
        
    def format_manual(self, input_file, output_file):
        """Main formatting function"""
        with open(input_file, 'r') as f:
            content = f.read()
        
        # Process the content
        sexy_content = self.make_it_sexy(content)
        
        # Write the output
        with open(output_file, 'w') as f:
            f.write(sexy_content)
            
    def make_it_sexy(self, content):
        """Apply all formatting transformations"""
        lines = content.split('\n')
        result = []
        
        # Add header
        result.extend(self.add_header(lines))
        
        # Skip the first line if it looks like a manual header
        start_index = 0
        if lines and lines[0].strip().endswith('Manual') and '(' in lines[0]:
            start_index = 1
        
        # Process line by line
        i = start_index
        while i < len(lines):
            line = lines[i]
            
            # Check for section headers
            if self.is_section_header(line):
                section_lines, skip = self.format_section_header(lines, i)
                result.extend(section_lines)
                i += skip
                continue
                
            # Check for options/flags
            if self.is_option_line(line):
                option_lines, skip = self.format_option(lines, i)
                result.extend(option_lines)
                i += skip
                continue
                
            # Check for code blocks
            if self.is_code_block(line, lines, i):
                code_lines, skip = self.format_code_block(lines, i)
                result.extend(code_lines)
                i += skip
                continue
                
            # Check for lists
            if self.is_list_item(line):
                list_lines, skip = self.format_list(lines, i)
                result.extend(list_lines)
                i += skip
                continue
                
            # Format cross-references
            line = self.format_cross_references(line)
            
            # Default: add the line as-is
            result.append(line)
            i += 1
            
        # Add table of contents after processing
        toc = self.generate_toc()
        
        # Insert TOC after header
        header_end = next((i for i, line in enumerate(result) if line.startswith('## ')), 10)
        result = result[:header_end] + toc + [''] + result[header_end:]
        
        return '\n'.join(result)
    
    def add_header(self, lines):
        """Add a sexy header to the document"""
        # Extract command name from first line or filename
        command_name = "Manual"
        for line in lines[:10]:
            if line.strip() and not line.startswith('#'):
                # Try to extract command name from NAME section
                if 'NAME' in lines[0:20]:
                    for i, l in enumerate(lines[:20]):
                        if 'NAME' in l:
                            # Look for the next non-empty line
                            for j in range(i+1, min(i+5, len(lines))):
                                if lines[j].strip():
                                    command_name = lines[j].split()[0].upper()
                                    break
                            break
                break
        
        header = [
            f"# 📚 {command_name} Manual",
            "",
            "> *Beautiful, readable documentation for command-line tools*",
            "",
            "---",
            ""
        ]
        return header
    
    def is_section_header(self, line):
        """Check if line is a section header (all caps)"""
        stripped = line.strip()
        if not stripped:
            return False
        # Check if it's all caps and at least 3 characters
        return stripped.isupper() and len(stripped) >= 3 and not stripped.startswith('-')
    
    def format_section_header(self, lines, index):
        """Format a section header"""
        header = lines[index].strip()
        
        # Skip if it's actually an option or flag
        if header.startswith('-'):
            return [lines[index]], 1
            
        # Add to TOC
        anchor = header.lower().replace(' ', '-').replace('/', '-')
        self.toc_entries.append((header, anchor))
        
        # Determine header level based on indentation or context
        level = "##"
        if header in ["NAME", "SYNOPSIS", "DESCRIPTION", "OPTIONS", "EXAMPLES", "SEE ALSO"]:
            level = "##"
        else:
            level = "###"
            
        formatted = [
            "",
            f"{level} {header.title()} {{#{anchor}}}",
            ""
        ]
        
        return formatted, 1
    
    def is_option_line(self, line):
        """Check if line starts with an option/flag"""
        stripped = line.strip()
        # Match lines that start with - or -- followed by letters
        return bool(re.match(r'^-{1,2}[a-zA-Z]', stripped))
    
    def format_option(self, lines, index):
        """Format an option and its description"""
        result = []
        line = lines[index]
        
        # Extract the option part
        option_match = re.match(r'^(\s*)(-{1,2}[a-zA-Z][a-zA-Z0-9-]*(?:\s+[A-Za-z_][A-Za-z0-9_-]*)?)', line)
        if not option_match:
            return [line], 1
            
        indent = option_match.group(1)
        option = option_match.group(2)
        
        # Get the rest of the line (description start)
        desc_start = line[len(option_match.group(0)):]
        
        # Format the option - use just code formatting, not bold+code
        result.append(f"{indent}`{option}`{desc_start}")
        
        # Collect continuation lines (indented more than the option)
        i = index + 1
        base_indent_len = len(indent)
        while i < len(lines):
            next_line = lines[i]
            if not next_line.strip():
                result.append(next_line)
                i += 1
                continue
                
            # Check if it's a continuation (more indented)
            next_indent = len(next_line) - len(next_line.lstrip())
            if next_indent > base_indent_len and not self.is_option_line(next_line):
                result.append(next_line)
                i += 1
            else:
                break
                
        return result, i - index
    
    def is_code_block(self, line, lines, index):
        """Check if this starts a code block"""
        stripped = line.strip()
        # Shell commands often start with $ or are indented significantly
        return (stripped.startswith('$') or 
                (len(line) - len(line.lstrip()) >= 6 and stripped and 
                 not self.is_option_line(line) and
                 not self.is_list_item(line)))
    
    def format_code_block(self, lines, index):
        """Format a code block with syntax highlighting"""
        result = []
        code_lines = []
        
        # Determine if it's a shell command
        is_shell = lines[index].strip().startswith('$')
        
        # Collect all code lines
        i = index
        base_indent = len(lines[index]) - len(lines[index].lstrip())
        
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                if i + 1 < len(lines) and self.is_code_block(lines[i + 1], lines, i + 1):
                    code_lines.append("")
                    i += 1
                    continue
                else:
                    break
                    
            current_indent = len(line) - len(line.lstrip())
            if current_indent >= base_indent or line.strip().startswith('$'):
                # Remove common indentation
                if line.strip():
                    code_lines.append(line[base_indent:] if not line.strip().startswith('$') else line.strip())
                else:
                    code_lines.append("")
                i += 1
            else:
                break
        
        # Add code block
        result.append("```bash" if is_shell else "```")
        result.extend(code_lines)
        result.append("```")
        result.append("")
        
        return result, i - index
    
    def is_list_item(self, line):
        """Check if line is a list item"""
        stripped = line.strip()
        # Numbered list or bullet list
        return bool(re.match(r'^\d+\.|^-\s+|^•|^\*\s+', stripped))
    
    def format_list(self, lines, index):
        """Format list items"""
        result = []
        i = index
        
        # Determine list type and base indentation
        first_line = lines[index]
        base_indent = len(first_line) - len(first_line.lstrip())
        
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                result.append(line)
                i += 1
                continue
                
            if self.is_list_item(line):
                # Format the list item
                stripped = line.strip()
                # Keep the list marker as-is but ensure proper spacing
                if re.match(r'^\d+\.', stripped):
                    # Numbered list - ensure space after period
                    formatted = re.sub(r'^(\d+\.)(\S)', r'\1 \2', stripped)
                else:
                    formatted = stripped
                    
                result.append(' ' * base_indent + formatted)
                i += 1
            else:
                # Check if it's a continuation of the list item
                current_indent = len(line) - len(line.lstrip())
                if current_indent > base_indent:
                    result.append(line)
                    i += 1
                else:
                    break
                    
        return result, i - index
    
    def format_cross_references(self, line):
        """Convert cross-references to links and track missing manuals"""
        # Pattern for command(section) references
        pattern = r'\b([a-zA-Z][\w-]+)\((\d+[a-zA-Z]*)\)'
        
        def replace_ref(match):
            cmd = match.group(1)
            section = match.group(2)
            # Track this reference for missing manual detection
            self.track_manual_reference(cmd)
            # Create a link to a potential manual page
            return f"[{cmd}({section})]({cmd}.html)"
        
        return re.sub(pattern, replace_ref, line)
    
    def track_manual_reference(self, command):
        """Track manual references for auto-stealing"""
        if not hasattr(self, 'referenced_manuals'):
            self.referenced_manuals = set()
        self.referenced_manuals.add(command)
    
    def save_reference_list(self):
        """Save list of referenced manuals for auto-stealing"""
        if hasattr(self, 'referenced_manuals'):
            with open('.manual_references.txt', 'w') as f:
                for manual in sorted(self.referenced_manuals):
                    f.write(f"{manual}\n")
            print(f"📝 Tracked {len(self.referenced_manuals)} manual references")
    
    def generate_toc(self):
        """Generate table of contents"""
        if not self.toc_entries:
            return []
            
        toc = [
            "## 📑 Table of Contents",
            ""
        ]
        
        for title, anchor in self.toc_entries:
            # Determine indentation based on header level
            if title in ["NAME", "SYNOPSIS", "DESCRIPTION", "OPTIONS", "EXAMPLES", "SEE ALSO", "AUTHORS", "FILES", "ENVIRONMENT"]:
                toc.append(f"- [{title.title()}](#{anchor})")
            else:
                toc.append(f"  - [{title.title()}](#{anchor})")
                
        toc.append("")
        return toc


def main():
    """Process all files in og_man/ directory"""
    og_dir = Path("og_man")
    sexy_dir = Path("sexy_md")
    
    if not og_dir.exists():
        print("Error: og_man/ directory not found!")
        sys.exit(1)
        
    formatter = SexyFormatter()
    
    # Process each .md file in og_man/
    for input_file in og_dir.glob("*.md"):
        output_name = f"sexy_{input_file.name}"
        output_file = sexy_dir / output_name
        
        print(f"Processing {input_file.name} -> {output_name}")
        formatter.format_manual(input_file, output_file)
    
    # Save reference list for auto-stealing
    formatter.save_reference_list()
        
    print("\n✨ Sexy formatting complete!")
    print("💡 Run 'python3 auto_steal.py' to steal missing referenced manuals!")


if __name__ == "__main__":
    main()