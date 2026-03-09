import os
import json
import re

def parse_frontmatter(content):
    """Simple parser for YAML frontmatter and Markdown body."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return None, content
    
    yaml_text = match.group(1)
    body = match.group(2)
    metadata = {}
    
    for line in yaml_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            
            # Type conversion for common fields
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            
            metadata[key] = value
            
    return metadata, body

def generate():
    guides_list = []
    # Get all .md files in the current directory
    files = [f for f in os.listdir('.') if f.endswith('.md')]
    
    for filename in files:
        file_path = filename
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            metadata, _ = parse_frontmatter(content)
            
            if metadata:
                # Use filename as ID if not specified
                if 'id' not in metadata:
                    metadata['id'] = filename[:-3]
                guides_list.append(metadata)
            else:
                print(f"Skipping {filename}: No frontmatter found.")

    # Sort: Pinned first, then by title
    guides_list.sort(key=lambda x: (not x.get('pinned', False), x.get('title', '')))

    with open('guides.json', 'w', encoding='utf-8') as f:
        json.dump(guides_list, f, indent=2)
        print(f"Successfully updated guides.json with {len(guides_list)} entries.")

if __name__ == "__main__":
    generate()
