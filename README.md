# 📚 Sexy Shell Manuals

> Transform boring Unix/Linux manual pages into beautiful, readable documentation with enhanced formatting, better navigation, and modern styling.

🔗 **[Live Demo](https://blakemagne.github.io/manuals/)** | 🎯 **Goal**: Make shell documentation sexy

## 🏗️ System Architecture

```mermaid
graph LR
    A[📋 fip/fop<br/>Manual Stealing] --> B[📁 og_man/<br/>Raw Manuals]
    B --> C[⚡ sexy_formatter.py<br/>Enhanced Markdown]
    C --> D[📝 sexy_md/<br/>Formatted Files]
    D --> E[🏗️ public/src/<br/>Static Site Generator]
    E --> F[🌐 docs/<br/>Beautiful HTML]
    F --> G[🚀 GitHub Pages<br/>Live Site]
    
    style A fill:#ff6b6b,stroke:#ff5252,color:#fff
    style B fill:#4ecdc4,stroke:#26a69a,color:#fff
    style C fill:#45b7d1,stroke:#2196f3,color:#fff
    style D fill:#96ceb4,stroke:#4caf50,color:#fff
    style E fill:#feca57,stroke:#ff9800,color:#fff
    style F fill:#ff9ff3,stroke:#e91e63,color:#fff
    style G fill:#54a0ff,stroke:#3f51b5,color:#fff
```

### 📦 Core Components

| Component | Purpose | Input | Output |
|-----------|---------|-------|--------|
| **`fip/fop`** | Manual stealing workflow | `man command` | Raw manual text |
| **`sexy_formatter.py`** | Markdown enhancement | Raw manual → `og_man/` | Enhanced markdown → `sexy_md/` |
| **`public/src/`** | Static site generator | Markdown files | HTML + CSS + Navigation |
| **`sexy_pipeline.py`** | Orchestration | Manual files | Complete deployment |

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🎨 **Vercel-inspired Design** | Modern dark theme with card layouts | ✅ Active |
| 🏠 **Smart Navigation** | Home button on every page + category organization | ✅ Active |
| 🔗 **Cross-reference Links** | Manual references become clickable links | ✅ Active |
| 📑 **Auto Table of Contents** | Generated navigation for every manual | ✅ Active |
| 🎯 **Enhanced Typography** | Professional code blocks, syntax highlighting | ✅ Active |
| 📱 **Mobile Responsive** | Beautiful on any device size | ✅ Active |
| ⚡ **Professional Parser** | Handles complex markdown without breaking | ✅ Active |
| 🏴‍☠️ **Manual Stealing** | `fip/fop` workflow for acquiring manuals | ✅ Active |

## 🚀 Quick Start

### One-Command Pipeline

```bash
# Complete workflow: stolen manual → deployed HTML
python3 sexy_pipeline.py
```

**What this does:**
1. 📝 Formats all manuals in `og_man/` to enhanced markdown
2. 📋 Copies formatted files to site content
3. 🏗️ Generates beautiful HTML with navigation
4. 📊 Reports completion stats
5. 🚀 Ready for GitHub Pages deployment

### Manual Workflow

```bash
# 1. Steal a manual page using fip/fop
man ssh | fip
fop > og_man/ssh.md

# 2. Run the complete pipeline
python3 sexy_pipeline.py

# 3. Deploy to GitHub Pages
git add docs/ && git commit -m "Add SSH manual" && git push
```

## 📁 Project Structure

```
manuals/
├── 📋 og_man/                    # Raw manual pages (input)
├── 📝 sexy_md/                  # Enhanced markdown (intermediate)
├── 🏗️ public/                   # Static site generator
│   ├── src/                     # Generation scripts
│   ├── static/                  # CSS and assets
│   ├── content/                 # Organized markdown content
│   └── template.html            # HTML template
├── 🌐 docs/                     # Generated HTML site (output)
├── ⚡ sexy_formatter.py          # Markdown enhancement engine
├── 🚀 sexy_pipeline.py          # Complete workflow orchestrator
└── 📚 CLAUDE.md                 # AI assistant instructions
```

## 🎯 Design Philosophy

### From This...
```
SSH(1)                    General Commands Manual                   SSH(1)

NAME
     ssh — OpenSSH remote login client

SYNOPSIS
     ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]...
```

### To This...
```markdown
# 📚 SSH Manual
> *Beautiful, readable documentation for command-line tools*

## Name
```
ssh — OpenSSH remote login client
```

## Synopsis
```bash
ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]...
```
```

**Key Improvements:**
- 🎨 Modern Vercel-inspired dark theme
- 📱 Mobile-responsive design with card layouts  
- 🔗 Clickable cross-references between manuals
- 📑 Auto-generated table of contents with anchors
- 💻 Proper syntax highlighting for code blocks
- 🏠 Consistent navigation with home buttons
- ⚡ Professional typography and spacing

## 🛠️ Advanced Usage

### Manual Organization
Manuals are automatically organized into logical categories:
- 🌐 **Network Tools** - ssh, curl, wget, etc.
- 🐚 **Shell Tools** - tmux, bash, zsh, etc.
- 📁 **File Systems** - ls, find, grep, etc.
- 🔧 **System Admin** - systemctl, crontab, etc.

### Custom Styling
The CSS uses a Vercel-inspired design system:
- **Dark gradient backgrounds** for visual depth
- **Card-based layouts** for better content organization
- **Professional typography** with system fonts
- **Hover effects** and smooth transitions
- **Responsive breakpoints** for all device sizes

---

✨ *Making shell documentation sexy, one manual at a time*