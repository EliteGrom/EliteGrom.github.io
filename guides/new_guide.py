import os
import sys
import re
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def create_guide(title, category="Basics"):
    slug = slugify(title)
    filename = f"{slug}.md"
    
    if os.path.exists(filename):
        print(f"Error: {filename} already exists!")
        return

    # Mock date format based on your existing files (In-game years are ~1280 ahead)
    today = f"3312.{datetime.now().strftime('%m.%d')}"

    template = f"""---
id: {slug}
title: {title}
description: Write a short description here.
category: {category}
diff: Beginner
time: "~5 min"
up: "{today}"
icon: "🚀"
---

## Overview
Briefly explain what this guide covers.

## Section 1
Detailed steps go here.

> **Tip:** Use callouts for important notes!
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"Created new guide: {filename}")
    print("Don't forget to run 'python generate_guides.py' after editing!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python new_guide.py \"Guide Title\" [Category]")
    else:
        title = sys.argv[1]
        category = sys.argv[2] if len(sys.argv) > 2 else "Basics"
        create_guide(title, category)
