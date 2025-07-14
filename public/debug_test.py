#!/usr/bin/env python3
import sys
sys.path.append('src')

# Test the issue directly
def test_block_detection():
    # Simulate the exact SSH Synopsis pattern
    ssh_synopsis_block = """```
ssh [-46AaCfGgKkMNnqsTtVvXxYy] 
    [-B bind_interface] [-b bind_address] 
    [-c cipher_spec] [-D [bind_address:]port] 
    [-E log_file] [-e escape_char] 
    [-F configfile] [-I pkcs11] 
    [-i identity_file] [-J destination] 
    [-L address] [-l login_name] 
    [-m mac_spec] [-O ctl_cmd] 
    [-o option] [-P tag] [-p port] 
    [-R address] [-S ctl_path] 
    [-W host:port] [-w local_tun[:remote_tun]] 
    destination [command [argument ...]]

ssh [-Q query_option]
```"""

    # Simulate the tmux Synopsis pattern
    tmux_synopsis_block = """```
tmux   [-2CDlNuVv]   [-c  shell-command]  [-f  file]  [-L  socket-name]
     [-S socket-path] [-T features] [command [flags]]
```"""

    # Test the detection logic from markdown_blocks.py
    def is_code_block(block):
        lines = block.split("\n")
        return len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```")

    print("SSH Synopsis block:")
    ssh_lines = ssh_synopsis_block.split("\n")
    print(f"  Total lines: {len(ssh_lines)}")
    print(f"  First line: {repr(ssh_lines[0])}")
    print(f"  Last line: {repr(ssh_lines[-1])}")
    print(f"  Is code block: {is_code_block(ssh_synopsis_block)}")
    print()

    print("tmux Synopsis block:")
    tmux_lines = tmux_synopsis_block.split("\n")
    print(f"  Total lines: {len(tmux_lines)}")
    print(f"  First line: {repr(tmux_lines[0])}")
    print(f"  Last line: {repr(tmux_lines[-1])}")
    print(f"  Is code block: {is_code_block(tmux_synopsis_block)}")
    print()

    # Test what happens when we process as code
    if is_code_block(ssh_synopsis_block):
        print("SSH would be processed as CODE block")
        # Simulate code_to_html_node processing
        lines = ssh_synopsis_block.split('\n')
        if lines[0].strip() == '```':
            lines = lines[1:]
        if lines and lines[-1].strip() == '```':
            lines = lines[:-1]
        text = '\n'.join(lines)
        print(f"Extracted text: {repr(text)}")
    else:
        print("SSH would be processed as PARAGRAPH block")

if __name__ == "__main__":
    test_block_detection()