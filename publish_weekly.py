import os
import re
import datetime
import json
import shutil
import random

# Configuration
DRAFTS_DIR = "insights/drafts"
POSTS_DIR = "insights/posts"
INDEX_PATH = "insights/index.html"
BATCH_SIZE = 5

def publish_weekly_batch():
    print(f"--- Running Weekly Publisher (Batch Size: {BATCH_SIZE}) ---")
    
    # 1. Get List of Drafts
    if not os.path.exists(DRAFTS_DIR):
        print("No drafts directory found.")
        return

    files = [f for f in os.listdir(DRAFTS_DIR) if f.endswith(".html")]
    
    if not files:
        print("No drafts found in backlog! Time to generate more.")
        return
        
    # Take top N
    to_publish = files[:BATCH_SIZE]
    print(f"Publishing: {to_publish}")
    
    published_cards_html = ""
    current_date = datetime.datetime.now().strftime("%b %d")
    
    for filename in to_publish:
        draft_path = os.path.join(DRAFTS_DIR, filename)
        live_path = os.path.join(POSTS_DIR, filename)
        
        # Read content to extract metadata
        with open(draft_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract Metadata JSON we injected
        # Look for <!-- META_JSON ... -->
        match = re.search(r'META_JSON\s*({.*?})', content, re.DOTALL)
        if match:
            meta = json.loads(match.group(1))
            title = meta.get("title", "Untitled")
            category = meta.get("category", "General")
            excerpt = meta.get("excerpt", "Click to read more.")
        else:
            # Fallback if manual drafted
            print(f"Warning: No metadata found for {filename}, using defaults.")
            title = filename.replace("-", " ").replace(".html", "").title()
            category = "INSIGHTS"
            excerpt = "Read our latest strategic insight."

        # Assign random Hero Image for Thumb
        img_num = random.randint(1, 3) # Assuming we have img1-3 placeholders or specific thumbs
        # Ideally we map categories to thumbs, but random is okay for automation MVP
        
        # Build Card HTML
        card_html = f'''
        <!-- Article: {title} -->
        <a href="posts/{filename}" class="insight-card" data-category="{category.lower()}">
            <div class="insight-thumb-wrapper">
                <img src="../assets/images/hero/img{img_num}.webp" alt="{title}" class="insight-thumb">
            </div>
            <div class="insight-content">
                <span class="insight-tag">{category}</span>
                <h2 class="insight-headline">{title}</h2>
                <p class="insight-excerpt">{excerpt}</p>
                <div class="insight-meta">
                    <div class="insight-author-img" style="background-image: url('../assets/images/hero/img1.webp'); background-size: cover;"></div>
                    <div class="insight-author-text">
                        Reuben Hester • {current_date}
                    </div>
                </div>
            </div>
        </a>
        '''
        published_cards_html += card_html + "\n"
        
        # Move File
        shutil.move(draft_path, live_path)
        print(f"Moved {filename} to Live.")

    # 2. Update Index HTML
    update_index_grid(published_cards_html)
    
    print("\n✅ Batch Publish Complete!")

def update_index_grid(new_html):
    try:
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            index_content = f.read()
            
        # Find Marker
        marker = '<main class="insights-grid-container" id="articles-grid" style="position: relative; z-index: 5;">'
        
        if marker in index_content:
            parts = index_content.split(marker)
            # parts[0] is header
            # parts[1] is grid content
            
            updated_content = parts[0] + marker + "\n" + new_html + parts[1]
            
            with open(INDEX_PATH, "w", encoding="utf-8") as f:
                f.write(updated_content)
        else:
            print("Error: Could not find grid marker in index.html")
            
    except FileNotFoundError:
        print(f"Error reading {INDEX_PATH}")

if __name__ == "__main__":
    publish_weekly_batch()
