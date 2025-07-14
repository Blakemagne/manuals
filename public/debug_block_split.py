#!/usr/bin/env python3
import sys
sys.path.append('src')

# Read the actual SSH file and test the block splitting
with open('content/network/sexy_ssh.md', 'r') as f:
    content = f.read()

# Find the Synopsis section
lines = content.split('\n')
synopsis_start = None
synopsis_end = None

for i, line in enumerate(lines):
    if line.strip() == '## Synopsis {#synopsis}':
        synopsis_start = i
    elif synopsis_start is not None and line.strip().startswith('## ') and i > synopsis_start:
        synopsis_end = i
        break

if synopsis_start is not None:
    # Extract just the Synopsis section with surrounding context
    start_idx = synopsis_start
    end_idx = synopsis_end if synopsis_end else len(lines)
    synopsis_section = '\n'.join(lines[start_idx:end_idx])
    
    print("Synopsis section:")
    print(repr(synopsis_section))
    print()
    
    # Import the new function
    from markdown_blocks import markdown_to_blocks
    
    blocks = markdown_to_blocks(synopsis_section)
    
    print(f"Number of blocks: {len(blocks)}")
    for i, block in enumerate(blocks):
        print(f"\nBlock {i}:")
        print(repr(block))
        
        # Test if it's a code block
        lines = block.split("\n")
        is_code = len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```")
        print(f"Is code block: {is_code}")
        
        if len(lines) > 1:
            print(f"First line: {repr(lines[0])}")
            print(f"Last line: {repr(lines[-1])}")