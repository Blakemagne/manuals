# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This project aims to make shell manuals sexy! We're building a system that transforms traditional Unix/Linux manual pages into beautifully formatted markdown and eventually into stunning HTML pages using a static site generator.

## Project Goal

Transform boring, hard-to-read manual pages into visually appealing, easy-to-navigate documentation that developers will actually want to read.

## Repository Structure (Current & Planned)

```
manuals/
├── og_man/         # Original manual pages pasted here - TO BE CREATED
├── sexy_md/        # Enhanced markdown versions (sexy_ssh.md, sexy_tmux.md, etc.) - TO BE CREATED  
├── sexy_html/      # Generated HTML documentation - TO BE CREATED
├── ssh.md          # Current markdown copy of ssh manual
└── tmux.md         # Current markdown copy of tmux manual
```

## Processing Pipeline

1. **Input**: Original manual pages are pasted into `og_man/`
2. **Conversion**: Automated formatting creates enhanced "sexy" markdown versions in `sexy_md/`
   - Files will be named with `sexy_` prefix (e.g., `sexy_ssh.md`, `sexy_tmux.md`)
3. **Generation**: Static site generator creates beautiful HTML pages in `sexy_html/`

## Current Status

The existing `ssh.md` and `tmux.md` files are direct markdown copies of the original manuals. The enhanced "sexy" versions will include improved formatting, better navigation, syntax highlighting, and visual enhancements.

## Working with Manual Pages

### Format Convention
Manual pages follow the traditional Unix manual page structure:
- **NAME**: Command name and brief description
- **SYNOPSIS**: Command syntax
- **DESCRIPTION**: Detailed explanation
- **OPTIONS**: Command-line options and flags
- **EXAMPLES**: Usage examples (if provided)
- **ENVIRONMENT**: Environment variables
- **FILES**: Related configuration files
- **SEE ALSO**: Related commands and documentation

### Adding New Manual Pages
When adding new manual pages to this repository:
1. Maintain the standard manual page section structure
2. Use consistent markdown formatting
3. Preserve all technical details and options from the original manual
4. Keep the filename simple: `command.md` (e.g., `ssh.md`, `tmux.md`)

### Common Tasks

To search within manual pages:
```bash
# Search for specific option or keyword
grep -i "keyword" *.md

# Find all occurrences of a command flag
grep -E "^\s*-[a-zA-Z]" ssh.md
```

To view a manual page:
```bash
# Using less for pagination
less tmux.md

# Using your preferred markdown viewer
# (varies by system/editor)
```

## Important Notes

- This is a documentation-only repository - no executable code or scripts
- Manual pages are for reference and should not be modified unless updating to newer versions
- When referencing content, include the specific section (e.g., "See SSH OPTIONS section")