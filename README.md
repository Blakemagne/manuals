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

- Table of contents generation
- Enhanced option/flag formatting
- Syntax-highlighted code blocks
- Cross-reference linking
- Mobile-responsive HTML output

## Usage

```bash
# Steal a manual page directly from man
man ssh | fip
fop > og_man/ssh.md

# Format to sexy markdown
python3 sexy_formatter.py

# Generate HTML (optional)
cd public && ./main.sh
```

---

*Making shell documentation sexy, one manual at a time* ✨