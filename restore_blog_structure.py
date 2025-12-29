import os
import re

POSTS_DIR = "insights/posts"

def restore_posts():
    print("--- Restoring Blog Posts ---")
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
    
    # Matches <img ... class="single-hero-img" ... > across lines
    img_pattern = re.compile(r'<img[^>]*class="single-hero-img"[^>]*>', re.DOTALL)
    
    for filename in files:
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        print(f"Processing {filename}...")
        new_content = content
        
        # 1. Restore the Content Div (Revert the bad sed replacement)
        if '<!-- removed div close -->' in new_content:
            # The sed replaced: </div>\n\n        <div class="single-post-content">
            # We want to put back the content div openness, but maybe keep the hero outside closing?
            # Actually, standard structure was:
            # <div class="single-post-hero">...</div>
            # <div class="single-post-content">
            
            # If we restore it, we get back two separate divs.
            # Then we need to move hero INTO content.
            
            # Let's restore the DIV structure first.
            new_content = new_content.replace(
                '<!-- removed div close -->', 
                '</div>\n\n        <div class="single-post-content">'
            )
            print("  Restored Content Div")
            
        # 2. Fix the Hero Comment (Revert the bad sed replacement)
        if '<!-- moved hero -->' in new_content:
            # The sed replaced: <div class="single-post-hero">
            # We want to put it back so we have valid HTML to parse, OR just remove it if we plan to move the img.
            # Let's remove it and the closing div to "free" the image, then wrap it properly later.
            
            # If we have <!-- moved hero --> ... [img] ... </div>
            # We should strip the comment and the closing div.
            
            # Find the comment
            new_content = new_content.replace('<!-- moved hero -->', '')
            
            # We also likely have a loose </div> after the image.
            # Since we restored the content div above (step 1), we have:
            # [img] </div> <div class="single-post-content">
            # We can remove that specific sequence.
            
            new_content = re.sub(
                r'</div>\s*<div class="single-post-content">', 
                '<div class="single-post-content">', 
                new_content, 
                flags=re.DOTALL
            )
            print("  Cleaned Hero Wrapper")

        # 3. Locate and Move Image
        # Now we should have: [img] ... <div class="single-post-content">
        # We want: <div class="single-post-content"> <div class="single-post-hero">[img]</div> ...
        
        img_match = img_pattern.search(new_content)
        if img_match:
            img_tag = img_match.group(0)
            
            # Check if image is already inside content?
            # Find index of content start
            content_start_idx = new_content.find('<div class="single-post-content">')
            img_idx = new_content.find('class="single-hero-img"') # approximate
            
            if content_start_idx != -1 and img_idx > content_start_idx:
                print("  Image already inside content. Skipping move.")
            else:
                # Remove image from current spot
                new_content = new_content.replace(img_tag, '', 1)
                
                # Wrap it new div
                new_hero_block = f'<div class="single-post-hero">\n                {img_tag}\n            </div>'
                
                # Insert at start of content
                if '<div class="single-post-content">' in new_content:
                    new_content = new_content.replace(
                        '<div class="single-post-content">',
                        f'<div class="single-post-content">\n            {new_hero_block}',
                        1
                    )
                    print("  Moved Image to Content")
                else:
                    print("  Error: Could not find content div to insert image")
                    
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
        else:
            print("  Warning: No image found to move")

if __name__ == "__main__":
    restore_posts()
