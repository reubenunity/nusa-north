import os
import re

POSTS_DIR = "insights/posts"

def fix_layout():
    print("--- Fixing Blog Post Layouts (Retry) ---")
    
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
    
    # improved regex to capture multi-line div content
    hero_pattern = re.compile(r'<div class="single-post-hero">.*?</div>', re.DOTALL)
    
    for filename in files:
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Check if already fixed (Naive check: Hero inside Content?)
        # A simple check is: does "single-post-hero" appear AFTER "single-post-content"?
        content_pos = content.find('<div class="single-post-content">')
        hero_pos = content.find('<div class="single-post-hero">')
        
        if content_pos != -1 and hero_pos != -1 and hero_pos > content_pos:
             print(f"Skipping {filename} (Already fixed)")
             continue
        
        # 2. Extract Hero
        match = hero_pattern.search(content)
        if not match:
             # It might be caused by inconsistent spacing or attributes.
             # Let's try finding it by simplistic sting searching if regex fails?
             print(f"Warning: No Hero Div found in {filename} with Regex")
             continue
             
        hero_html = match.group(0)
        
        # 3. Remove Hero
        new_content = content.replace(hero_html, "", 1) # Remove only first occurrence
        
        # 4. Inject Hero inside Content
        if '<div class="single-post-content">' in new_content:
            new_content = new_content.replace(
                '<div class="single-post-content">', 
                f'<div class="single-post-content">\n            {hero_html}',
                1
            )
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ Fixed {filename}")
        else:
             print(f"Error: Content div not found in {filename}")

if __name__ == "__main__":
    fix_layout()
