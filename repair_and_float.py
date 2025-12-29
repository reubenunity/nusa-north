import os
import re

POSTS_DIR = "insights/posts"

def repair_posts():
    print("--- Repairing Blog Posts ---")
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
    
    # Regex to find the Hero Image tag specifically
    img_pattern = re.compile(r'<img[^>]+class="single-hero-img"[^>]*>')
    
    for filename in files:
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        print(f"Processing {filename}...")
        
        # 1. Extract the Image Tag
        img_match = img_pattern.search(content)
        if not img_match:
            print(f"  Warning: No hero image found in {filename}")
            continue
            
        img_tag = img_match.group(0)
        
        # 2. Clean up the file
        # Remove the known SED artifacts and the image itself from its current location
        clean_content = content
        clean_content = clean_content.replace('<!-- moved hero -->', '')
        clean_content = clean_content.replace(img_tag, '') 
        
        # Clean up loose closing divs that might have been left behind
        # This is risky, but we know the hero div had a closing </div>
        # and we saw in the view_file that there is a loose </div> before single-post-content
        # Pattern: </div>\s*<div class="single-post-content">
        # Or just remove the specific loose div if we can identify it.
        # Let's try to strip empty divs? No.
        
        # Heuristic: If we see `</div>` followed immediately by `<div class="single-post-content">`, it's likely the ghost of the hero div.
        clean_content = re.sub(r'</div>\s*<div class="single-post-content">', '<div class="single-post-content">', clean_content)
        
        # Also remove the `</div>` that might be left inside content if I manually moved it before?
        
        # 3. Construct Correct Hero Block
        new_hero_block = f'\n            <div class="single-post-hero">\n                {img_tag}\n            </div>'
        
        # 4. Insert into Content
        if '<div class="single-post-content">' in clean_content:
            # Check if it already has a hero block inside?
            # If so, we might be duplicating. But we removed the img tag globally, so the old block is empty or gone.
            
            clean_content = clean_content.replace(
                '<div class="single-post-content">', 
                f'<div class="single-post-content">{new_hero_block}',
                1
            )
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(clean_content)
            print(f"  ✅ Repaired & Floated")
        else:
            print(f"  Error: No content div found")

if __name__ == "__main__":
    repair_posts()
