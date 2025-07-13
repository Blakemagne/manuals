"""
Custom homepage generator to create card-based layout
"""

import re
from pathlib import Path

def create_homepage_html(categorized_files):
    """Create homepage HTML with proper card layout"""
    
    # Build the cards HTML
    cards_html = '<div class="category-grid">\n'
    
    category_icons = {
        'system': '⚙️',
        'files': '📁', 
        'editors': '✏️',
        'network': '🌐',
        'development': '💻',
        'shell': '🐚',
        'archive': '📦',
        'media': '🎬',
        'documentation': '📖',
        'security': '🔒',
        'database': '🗄️',
        'monitoring': '📊',
        'virtualization': '🐳',
        'package': '📦'
    }
    
    for category, files in sorted(categorized_files.items()):
        from organize_manuals import MANUAL_CATEGORIES
        
        if category in MANUAL_CATEGORIES:
            description = MANUAL_CATEGORIES[category]['description']
            icon = category_icons.get(category, '📚')
        else:
            description = "Miscellaneous Tools"
            icon = '📚'
            
        cards_html += f'''  <div class="category-card">
    <h3><a href="./{category}/index.html">{icon} {description}</a></h3>
    <p>{len(files)} manuals available</p>
  </div>
'''
    
    cards_html += '</div>\n'
    
    # Create the full homepage HTML
    homepage_html = f'''<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sexy Shell Manuals</title>
    <link href="./index.css" rel="stylesheet">
</head>

<body>
    <header class="nav-header">
        <a href="./index.html" class="home-button">🏠 Home</a>
    </header>
    <article>
        <h1>Sexy Shell Manuals</h1>
        
        <p>Beautiful, readable documentation for command-line tools organized by category.</p>
        <p>Making shell documentation sexy, one manual at a time.</p>
        
        <h2>Browse by Category</h2>
        
        {cards_html}
        
        <div class="stats">
            <strong>{sum(len(files) for files in categorized_files.values())} manuals available!</strong>
        </div>
        
        <h2>About This Project</h2>
        
        <p>Transform boring Unix/Linux manual pages into beautiful, readable documentation with enhanced formatting, better navigation, and modern styling.</p>
        
        <h2>How It Works</h2>
        
        <p>We take traditional manual pages and make them sexy:</p>
        
        <ol>
            <li><strong>Steal</strong> a manual page using fip/fop</li>
            <li><strong>Format</strong> to enhanced markdown with our sexy formatter</li>
            <li><strong>Generate</strong> beautiful HTML with our static site generator</li>
            <li><strong>Organize</strong> into logical categories for easy browsing</li>
        </ol>
        
        <p>No more ugly, hard-to-navigate shell manuals!</p>
        
        <h2>Features</h2>
        
        <ul>
            <li>🎨 <strong>Vercel-inspired design</strong> - Modern, clean interface</li>
            <li>🌙 <strong>Dark theme optimized</strong> for readability</li>
            <li>📱 <strong>Mobile-responsive</strong> - Beautiful on any device</li>
            <li>⚡ <strong>Fast, lightweight</strong> pages</li>
            <li>🔗 <strong>Smart cross-references</strong> - Manual links that actually work</li>
            <li>🏠 <strong>Easy navigation</strong> - Home button on every page</li>
            <li>📁 <strong>Intelligent categorization</strong> by functionality</li>
        </ul>
        
        <hr>
        
        <p><em>This site was generated from markdown using a custom static site generator.</em></p>
    </article>
</body>

</html>'''
    
    return homepage_html

def save_custom_homepage(categorized_files, output_path):
    """Save the custom homepage HTML"""
    html = create_homepage_html(categorized_files)
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"✅ Created custom homepage: {output_path}")