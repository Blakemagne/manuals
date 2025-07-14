from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quite"
    OLIST = "ordered_list"
    ULIST = "unordered_list"
    RULE = "horizontal_rule"


def markdown_to_blocks(markdown):
    """Split markdown into blocks, preserving code blocks that contain empty lines."""
    # Use a simple approach: split on \n\n, then merge broken code blocks
    raw_blocks = markdown.split('\n\n')
    filtered_blocks = []
    
    for block in raw_blocks:
        stripped_block = block.strip()
        if stripped_block == '' or stripped_block == '#':
            continue
        filtered_blocks.append(stripped_block)
    
    # Now merge broken code blocks
    merged_blocks = []
    i = 0
    while i < len(filtered_blocks):
        block = filtered_blocks[i]
        
        # Check if this block starts with ``` but doesn't end with ```
        lines = block.split('\n')
        if (len(lines) > 0 and lines[0].strip().startswith('```') and 
            not any(line.strip().startswith('```') for line in lines[1:])):
            
            # This is a broken code block start, find the end
            merged_block = block
            j = i + 1
            
            while j < len(filtered_blocks):
                next_block = filtered_blocks[j]
                merged_block += '\n\n' + next_block
                
                # Check if this block ends with ```
                next_lines = next_block.split('\n')
                if any(line.strip().startswith('```') for line in next_lines):
                    # Found the end
                    break
                j += 1
            
            merged_blocks.append(merged_block)
            i = j + 1
        else:
            merged_blocks.append(block)
            i += 1
    
    return merged_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    block_stripped = block.strip()

    # Check for horizontal rules (---, ***, ___)
    if block_stripped in ["---", "***", "___"] or (len(block_stripped) >= 3 and all(c in "-*_" for c in block_stripped) and len(set(block_stripped)) == 1):
        return BlockType.RULE
        
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        import re
        for line in lines:
            # Allow lines that start with optional whitespace followed by "- "
            if not re.match(r'^\s*- ', line):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.RULE:
        return rule_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    import re
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :].strip()
    
    # Extract anchor if present (e.g., "Title {#anchor}")
    anchor_match = re.search(r'\{#([^}]+)\}', text)
    props = None
    if anchor_match:
        anchor = anchor_match.group(1)
        text = re.sub(r'\s*\{#[^}]+\}', '', text)  # Remove anchor from text
        props = {"id": anchor}
    
    children = text_to_children(text)
    return ParentNode(f"h{level}", children, props)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    # Remove first line if it's just ``` and last line if it's just ```
    lines = block.split('\n')
    if lines[0].strip() == '```':
        lines = lines[1:]
    if lines and lines[-1].strip() == '```':
        lines = lines[:-1]
    text = '\n'.join(lines)
    
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    import re
    items = block.split("\n")
    html_items = []
    for item in items:
        # Use regex to find and remove the list marker (optional whitespace + "- ")
        match = re.match(r'^(\s*)- (.*)$', item)
        if match:
            indentation, text = match.groups()
            children = text_to_children(text)
            # For now, we'll flatten the list structure and ignore indentation levels
            # A more complex implementation could create nested <ul> structures
            html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def rule_to_html_node(block):
    """Convert horizontal rule markdown to HTML hr tag"""
    from htmlnode import LeafNode
    return LeafNode("hr", "", None)