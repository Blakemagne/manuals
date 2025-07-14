#!/usr/bin/env python3

# Test the exact Synopsis issue
synopsis_text = """## Synopsis {#synopsis}

```
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
```

"""

print("Original text:")
print(repr(synopsis_text))
print()

# Manually process to see what happens
lines = synopsis_text.split('\n')
print("Lines:")
for i, line in enumerate(lines):
    print(f"{i:2}: {repr(line)}")
print()

# Test simple split on double newlines
simple_blocks = synopsis_text.split('\n\n')
print("Simple split on \\n\\n:")
for i, block in enumerate(simple_blocks):
    if block.strip():
        print(f"Block {i}: {repr(block)}")
print()

# What we need: The code block should be from line 2 to line 18
print("Expected code block (lines 2-18):")
expected_code = '\n'.join(lines[2:19])  # lines 2-18 inclusive
print(repr(expected_code))
print()

# Test if this would be detected as code
code_lines = expected_code.split('\n')
print(f"Expected code - first line: {repr(code_lines[0])}")
print(f"Expected code - last line: {repr(code_lines[-1])}")
print(f"Would be detected as code: {len(code_lines) > 1 and code_lines[0].startswith('```') and code_lines[-1].startswith('```')}")