import re

from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Enhanced delimiter parser that handles real-world text with unmatched delimiters
    """
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Use regex to find proper markdown formatting pairs
        if delimiter == "**":
            new_nodes.extend(_parse_bold_nodes(old_node.text))
        elif delimiter == "_":
            new_nodes.extend(_parse_italic_nodes(old_node.text))
        elif delimiter == "`":
            new_nodes.extend(_parse_code_nodes(old_node.text))
        else:
            # Fallback to old behavior for other delimiters
            new_nodes.extend(_parse_simple_delimiter(old_node.text, delimiter, text_type))
    return new_nodes


def _parse_bold_nodes(text):
    """Parse **bold** text while ignoring single asterisks"""
    nodes = []
    pattern = r'\*\*(.*?)\*\*'
    last_end = 0
    
    for match in re.finditer(pattern, text):
        # Add text before the match
        if match.start() > last_end:
            nodes.append(TextNode(text[last_end:match.start()], TextType.TEXT))
        
        # Add the bold text
        bold_text = match.group(1)
        if bold_text:  # Don't create empty nodes
            nodes.append(TextNode(bold_text, TextType.BOLD))
        
        last_end = match.end()
    
    # Add remaining text
    if last_end < len(text):
        nodes.append(TextNode(text[last_end:], TextType.TEXT))
    
    # If no matches found, return the original text
    if not nodes:
        nodes.append(TextNode(text, TextType.TEXT))
    
    return nodes


def _parse_italic_nodes(text):
    """Parse _italic_ text while ignoring underscores in filenames/paths"""
    nodes = []
    # More sophisticated pattern that avoids matching underscores in common contexts
    # Avoid matching underscores that are:
    # - Between word characters (likely_variable_names)
    # - In file paths (~/. or /etc/)
    # - In URLs or technical terms
    pattern = r'(?<!\w)_([^_\n]+?)_(?!\w)'
    last_end = 0
    
    for match in re.finditer(pattern, text):
        # Skip if this looks like a filename or path
        context_start = max(0, match.start() - 10)
        context = text[context_start:match.end() + 10]
        
        # Skip common false positives
        if any(skip in context.lower() for skip in ['~/.', '/etc/', '_config', '_log', 'ssh_', '.md']):
            continue
            
        # Add text before the match
        if match.start() > last_end:
            nodes.append(TextNode(text[last_end:match.start()], TextType.TEXT))
        
        # Add the italic text
        italic_text = match.group(1)
        if italic_text:
            nodes.append(TextNode(italic_text, TextType.ITALIC))
        
        last_end = match.end()
    
    # Add remaining text
    if last_end < len(text):
        nodes.append(TextNode(text[last_end:], TextType.TEXT))
    
    # If no matches found, return the original text
    if not nodes:
        nodes.append(TextNode(text, TextType.TEXT))
    
    return nodes


def _parse_code_nodes(text):
    """Parse `code` text while handling unmatched backticks gracefully"""
    nodes = []
    pattern = r'`([^`\n]*?)`'
    last_end = 0
    
    for match in re.finditer(pattern, text):
        # Add text before the match
        if match.start() > last_end:
            nodes.append(TextNode(text[last_end:match.start()], TextType.TEXT))
        
        # Add the code text
        code_text = match.group(1)
        if code_text:
            nodes.append(TextNode(code_text, TextType.CODE))
        
        last_end = match.end()
    
    # Add remaining text
    if last_end < len(text):
        nodes.append(TextNode(text[last_end:], TextType.TEXT))
    
    # If no matches found, return the original text
    if not nodes:
        nodes.append(TextNode(text, TextType.TEXT))
    
    return nodes


def _parse_simple_delimiter(text, delimiter, text_type):
    """Fallback parser for other delimiters - more forgiving than original"""
    nodes = []
    sections = text.split(delimiter)
    
    # If we don't have pairs, just return as plain text
    if len(sections) < 3 or len(sections) % 2 == 0:
        return [TextNode(text, TextType.TEXT)]
    
    for i in range(len(sections)):
        if sections[i] == "":
            continue
        if i % 2 == 0:
            nodes.append(TextNode(sections[i], TextType.TEXT))
        else:
            nodes.append(TextNode(sections[i], text_type))
    
    return nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches