import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Check if this is a manual page (sexy_*.md files)
    filename = Path(from_path).name
    if filename.startswith('sexy_'):
        html = f'<div class="manual-content">{html}</div>'

    title = extract_title(markdown_content)
    
    # Determine relative path depth for CSS and home links
    dest_path_obj = Path(dest_path)
    # Count how deep we are from the docs root
    relative_depth = len(dest_path_obj.relative_to(Path(dest_path_obj.parts[0])).parts) - 1
    
    if relative_depth > 0:
        # We're in a subdirectory, so use ../
        css_path = "../index.css"
        home_path = "../index.html"
    else:
        # We're in the root, use relative paths
        css_path = "./index.css"
        home_path = "./index.html"
    
    # Replace template variables
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("./index.css", css_path)
    template = template.replace("./index.html", home_path)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
