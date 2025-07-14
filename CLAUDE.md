# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the Sexy Shell Manuals project.

## Project Overview

**Sexy Shell Manuals** transforms boring Unix/Linux manual pages into beautiful, readable documentation with enhanced formatting, better navigation, and modern styling.

**Goal**: Make shell documentation sexy through automated pipeline from manual stealing to deployed HTML.

## Core Workflow

### Complete Pipeline
```bash
# One command: stolen manual → deployed HTML
python3 sexy_pipeline.py
```

### Manual Stealing Workflow  
```bash
# Use fip/fop to steal manuals (respectful way)
man ssh | fip
fop > og_man/ssh.md
```

## Architecture Components

### 📁 Directory Structure
- **`og_man/`** - Raw manual pages (input)
- **`sexy_md/`** - Enhanced markdown (intermediate) 
- **`public/`** - Static site generator
- **`docs/`** - Generated HTML site (GitHub Pages output)

### 🔧 Core Scripts
- **`sexy_formatter.py`** - Converts raw manuals to enhanced markdown
- **`sexy_pipeline.py`** - Orchestrates complete workflow
- **`public/src/main.py`** - Static site generator entry point
- **`public/src/gencontent.py`** - HTML generation logic

### 🎨 Styling System
- **Vercel-inspired dark theme** with gradient backgrounds
- **Card-based layouts** for category organization
- **Professional typography** with system fonts
- **Mobile-responsive design** with breakpoints
- **Manual-specific styling** with `.manual-content` class

## Key Features

### ✅ Current Features
- 🏠 **Smart navigation** - Home button on every page
- 🔗 **Cross-reference links** - Manual references become clickable
- 📑 **Auto table of contents** - Generated navigation with anchors
- 🎯 **Enhanced typography** - Professional code blocks and formatting
- 📱 **Mobile responsive** - Beautiful on any device
- 🏴‍☠️ **Manual stealing** - fip/fop workflow for acquiring manuals

### 🎨 Design Philosophy
Transform from ugly traditional manual format:
```
SSH(1)                    General Commands Manual                   SSH(1)
NAME
     ssh — OpenSSH remote login client
```

To beautiful modern documentation:
```markdown
# 📚 SSH Manual
> *Beautiful, readable documentation for command-line tools*

## Name
ssh — OpenSSH remote login client
```

## Development Commands

### Generate HTML from Current Content
```bash
# From public/ directory
python3 src/main.py
```

### Complete Pipeline
```bash
# From project root
python3 sexy_pipeline.py
```

### Manual Content Generation
```bash
# Format raw manuals to sexy markdown
python3 sexy_formatter.py
```

## Important Notes

### File Organization
- Manual pages automatically organized into categories (Network, Shell, etc.)
- Category pages generated with proper navigation
- Manual content wrapped in `.manual-content` class for styling

### CSS Structure
- **Base styles** for homepage layout
- **Manual-specific styles** for content formatting  
- **Category card layouts** with hover effects
- **Responsive typography** for all device sizes

### Deployment
- HTML output goes to `docs/` directory
- GitHub Pages serves from `docs/`
- CSS and navigation use relative paths for subdirectories

## Development Workflow

1. **Add new manuals** to `og_man/` directory
2. **Run sexy_pipeline.py** to process everything
3. **Check output** in `docs/` directory
4. **Commit and push** to deploy via GitHub Pages

### fip/fop Usage
- **fip** = "file in place" (pipe manual content)
- **fop** = "file out place" (output to file)
- This is the respectful way to steal manuals

## Code Style

- **Simple, focused scripts** - Each component has single responsibility
- **Professional markdown parsing** - Handles complex formatting without breaking
- **Modern CSS patterns** - Uses CSS Grid, Flexbox, and custom properties
- **Consistent naming** - `sexy_*.md` for formatted manuals, clear component names

## Testing

- **Visual testing** - Check generated HTML in browser
- **Manual testing** - Verify links work, navigation functions
- **Responsive testing** - Check mobile layouts
- **No formal test framework** - Simple validation scripts only