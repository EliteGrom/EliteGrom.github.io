# Yuri Grom — Guide Editor

A simple web-based tool to help write and format guides for the Yuri Grom website.

## How to use:
1. Open `index.html` in your browser.
2. Fill out the metadata fields (Title, ID, Category, etc.).
3. Write your guide in Markdown.
4. Download the generated `.md` file.
5. Upload the `.md` file to the `guides/` directory of the repository.
6. The GitHub Action will automatically update the `guides.json` file.

## Features:
- Real-time Markdown preview.
- Automatic "slug" generation for the ID.
- Pre-filled in-game date.
- Formatted YAML frontmatter generation.
- Styled to match the main website theme.
