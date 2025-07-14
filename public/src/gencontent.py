import os
import re
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
    toc_list = ""
    if filename.startswith('sexy_'):
        html, toc_list = extract_toc_for_header(html)
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
    
    # Create header TOC and script if this is a manual page
    header_toc = ""
    script = ""
    if toc_list:
        header_toc = f'''<div class="header-toc">
            <button class="toc-button" onclick="toggleHeaderTOC()">
                📑 Contents
                <div class="header-hamburger" id="headerHamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="header-toc-dropdown" id="headerTocDropdown">
                <h3>📑 Table of Contents</h3>
                {toc_list}
            </div>
        </div>'''
        
        script = '''<script>
function toggleHeaderTOC() {
    const dropdown = document.getElementById('headerTocDropdown');
    const hamburger = document.getElementById('headerHamburger');
    
    dropdown.classList.toggle('open');
    hamburger.classList.toggle('active');
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const headerToc = document.querySelector('.header-toc');
    const dropdown = document.getElementById('headerTocDropdown');
    const hamburger = document.getElementById('headerHamburger');
    
    if (headerToc && !headerToc.contains(event.target)) {
        dropdown.classList.remove('open');
        hamburger.classList.remove('active');
    }
});
</script>'''

    # Replace template variables
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("{{ HeaderTOC }}", header_toc)
    template = template.replace("{{ Script }}", script)
    template = template.replace("./index.css", css_path)
    template = template.replace("./index.html", home_path)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_toc_for_header(html):
    """Extract TOC list from content and return both modified html and toc list"""
    # Pattern to match the TOC section: h2 with "Table of Contents" followed by a ul
    pattern = r'(<h2[^>]*>📑 Table of Contents</h2>)\s*(<ul>.*?</ul>)'
    
    toc_list = ""
    
    def extract_toc(match):
        nonlocal toc_list
        toc_list = match.group(2)  # Extract the ul element
        return ""  # Remove the TOC from content
    
    # Remove TOC from content and extract it
    modified_html = re.sub(pattern, extract_toc, html, flags=re.DOTALL)
    
    return modified_html, toc_list


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
