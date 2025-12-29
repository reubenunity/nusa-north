import os
import re

POSTS_DIR = "insights/posts"

def final_repair():
    print("--- Final Repair of Blog Posts ---")
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
    
    # Pattern to find the corrupted image tag: src="..." followed by <!-- moved img -->
    # Example: <img src="../../assets/images/..." \n <!-- moved img -->
    corrupt_pattern = re.compile(r'<img\s+src="([^"]+)"[^<]*<!-- moved img -->', re.DOTALL)
    
    for filename in files:
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        print(f"Processing {filename}...")
        new_content = content
        
        # 1. Inspect for Corruption
        match = corrupt_pattern.search(new_content)
        
        if match:
            src = match.group(1)
            full_match = match.group(0)
            print(f"  Found corrupt tag with src: {src}")
            
            # 2. Reconstruct Valid Tag
            # We'll use the filename as a basic Alt text
            alt_text = filename.replace(".html", "").replace("-", " ").title()
            valid_img_tag = f'<img src="{src}" alt="{alt_text}" class="single-hero-img">'
            
            # 3. Replace corrupt tag with nothing (we will insert new one correctly)
            new_content = new_content.replace(full_match, "")
            
            # 4. Clean up artifacts (comments, div closure)
            new_content = new_content.replace('<!-- moved hero -->', '')
            
            # The structure was:
            # <!-- moved hero -->
            #     [corrupt img]
            # </div>
            # <div class="single-post-content"> (maybe?)
            
            # We need to remove the </div> that followed the image.
            # In `educational-quiet-luxury.html`, the `</div>` is right after the corrupt img.
            # We can replace `</div>\s*<div class="single-post-content">` if it exists nearby?
            # Or just remove the FIRST closing div after where the image was? 
            # This is risky.
            
            # Let's see: `new_content` now has the image removed.
            # It likely has `    \n            </div>` left over.
            
            # 5. Insert New Hero inside Content
            hero_block = f'<div class="single-post-hero">\n                {valid_img_tag}\n            </div>'
            
            # If the file already has `single-post-content`, we insert at start.
            if '<div class="single-post-content">' in new_content:
                # But wait, did we fix the `<!-- removed div close -->` issue?
                # The previous `restore_blog_structure.py` MIGHT have fixed `video-roi.html`.
                # If `quiet-luxury.html` didn't have that issue, `single-post-content` is present.
                pass
            
            # Reconstruct content div if it was lost
            if '<!-- removed div close -->' in new_content:
                new_content = new_content.replace('<!-- removed div close -->', '</div>\n\n<div class="single-post-content">')
            
            # Now insert hero
            if '<div class="single-post-content">' in new_content:
                 new_content = new_content.replace(
                    '<div class="single-post-content">', 
                    f'<div class="single-post-content">\n            {hero_block}', 
                    1
                )
                 
                 # Now clean up loose div?
                 # If we see `</div>` right before `class="single-post-content"`, we might want to keep it?
                 # No, the Hero div was a sibling. So `</div>` closed the Hero sibling.
                 # But we removed the Hero opening. So that `</div>` is now closing... `single-post-container`? No.
                 # The Hero div was inside `single-post-container`.
                 # So `single-post-container` > `Header` + `Hero` + `Content`.
                 # If we remove Hero Opening, but keep Hero Closing, and then start Content...
                 # It means `single-post-container` closes at the Hero Closing!
                 # Then `Content` is OUTSIDE the container.
                 # THAT is why the background breaks or layout breaks.
                 
                 # So we MUST remove the loose `</div>`.
                 # Strategy: Replace `</div>\s*<div class="single-post-content">` with `<div class="single-post-content">`.
                 # AND replace `</div>\s*<div class="single-post-hero">` (our new block) is not relevant yet.
                 
                 # Wait, we just inserted the hero block.
                 # So we have `... </div>` (loose) `... <div class="single-post-content"> {hero} ...`
                 # So we find the loose div before our replacement.
                 
                 # Let's do a blind replace of `</div>\s*<div class="single-post-content">` -> `<div class="single-post-content">` 
                 # BEFORE we insert the hero block.
                 
                 # Undo insertion logic for a second
                 pass
                 
            # Correct order:
            # A. Clean up loose div
            new_content = re.sub(r'</div>\s*<div class="single-post-content">', '<div class="single-post-content">', new_content, flags=re.DOTALL)
            
            # B. Insert Hero
            new_content = new_content.replace(
                '<div class="single-post-content">',
                f'<div class="single-post-content">\n            {hero_block}',
                1
            )
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("  ✅ Fixed Corrupt Image & Layout")
            
        else:
            # If not corrupt, check if we need to fix layout for non-corrupt files
            if '<!-- removed div close -->' in new_content:
                 new_content = new_content.replace('<!-- removed div close -->', '</div>\n\n<div class="single-post-content">')
                 with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                 print("  Restored div structure")

if __name__ == "__main__":
    final_repair()
