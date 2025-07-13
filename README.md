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

## Complete Workflow

### Adding a New Manual

```bash
# 1. Steal a manual page directly from man
man git | fip
fop > og_man/git.md

# 2. Format to sexy markdown
python3 sexy_formatter.py

# 3. Add to website (automated)
python3 add_manual.py git

# 4. Deploy to GitHub Pages
git add docs/ && git commit -m "Add git manual" && git push
```

### Manual Steps (if automation fails)

```bash
# If add_manual.py doesn't work, do this manually:

# 1-2. Same as above (steal and format)

# 3. Create simple version for site
cp sexy_md/sexy_git.md public/content/git.md
# Edit git.md to remove complex formatting

# 4. Update homepage
# Edit public/content/index.md to add link

# 5. Generate HTML
cd public && python3 src/main.py

# 6. Deploy
git add docs/ && git commit -m "Add git manual" && git push
```

---

*Making shell documentation sexy, one manual at a time* ✨