# 📚 Sexy Shell Manuals

Transform boring Unix/Linux manual pages into beautiful, readable documentation.

## System Design

```
og_man/           →    sexy_md/           →    sexy_html/
(raw manuals)          (enhanced markdown)     (beautiful HTML)
```

### Pipeline

1. **Input**: Place raw manual pages in `og_man/`
2. **Format**: Run `python3 sexy_formatter.py` to create enhanced markdown in `sexy_md/`
3. **Generate**: Use static site generator in `public/` to create HTML in `sexy_html/`

### Components

- **`sexy_formatter.py`** - Autoformats manual pages with modern markdown
- **`public/`** - Static site generator for HTML output
- **`CLAUDE.md`** - Instructions for AI assistants working on this project

### Features

- **🏠 Home navigation** - Every manual has a home button
- **🔗 Smart cross-references** - Manual references become clickable links
- **🤖 Auto-detection** - System finds missing referenced manuals
- **🏴‍☠️ Auto-stealing** - Automatically steals missing manuals
- **📑 Table of contents** - Generated navigation for every manual
- **🎨 Enhanced formatting** - Options and flags styled for readability
- **💻 Syntax highlighting** - Code examples that actually look good
- **📱 Mobile-responsive** - Beautiful on any device
- **⚡ Professional parser** - Handles complex markdown without breaking

## Complete Workflow

### One-Command Pipeline

```bash
# Complete pipeline: stolen manual → deployed HTML
python3 sexy_pipeline.py
```

This single command runs the entire workflow:
1. Formats all manuals in `og_man/` to sexy markdown
2. Auto-steals missing referenced manuals
3. Copies sexy markdown to site content
4. Generates HTML with static site generator
5. Reports completion and next steps

### Manual Process (if needed)

```bash
# 1. Steal a manual page directly from man
man git | fip
fop > og_man/git.md

# 2. Run complete pipeline
python3 sexy_pipeline.py

# 3. Deploy to GitHub Pages
git add docs/ && git commit -m "Add git manual" && git push
```

### Advanced Features

```bash
# Scan for missing manual references
python3 auto_steal.py --scan

# Steal a specific manual
python3 auto_steal.py --steal ssh-agent

# Auto-steal all missing referenced manuals
python3 auto_steal.py
```

---

*Making shell documentation sexy, one manual at a time* ✨