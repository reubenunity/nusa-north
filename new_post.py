import os
import datetime
import re

# Configuration
TEMPLATE_PATH = "insights/template.html"
INDEX_PATH = "insights/index.html"
POSTS_DIR = "insights/posts"

def slugify(text):
    """Converts a title to a filename-safe slug."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

def create_new_post():
    print("\n--- Create New Insight Article ---")
    
    # 1. Gather Input
    title = input("Enter Article Title: ").strip()
    category = input("Enter Category (e.g. Strategy, SEO, Creative): ").strip().upper()
    excerpt = input("Enter Short Excerpt (for the card): ").strip()
    
    if not title:
        print("Error: Title is required.")
        return

    # 2. Generate Filename & Date
    slug = slugify(title)
    filename = f"{slug}.html"
    filepath = os.path.join(POSTS_DIR, filename)
    date_str = datetime.datetime.now().strftime("%b %d, %Y")

    # 3. Read Template
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Error: Template not found at {TEMPLATE_PATH}")
        return

    # 4. Fill Template
    # Simple replace for placeholders
    new_content = template_content.replace("<!-- TITLE_PLACEHOLDER -->", f"<title>{title} | Nusa & North Insights</title>")
    new_content = new_content.replace("<!-- CATEGORY_PLACEHOLDER -->", category)
    new_content = new_content.replace("<!-- HEADER_PLACEHOLDER -->", title)
    new_content = new_content.replace("<!-- DATE_PLACEHOLDER -->", date_str)
    
    # 5. Write New Post File
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"\n✅ Created post file: {filepath}")

    # 6. Update Index Page (Prepend to Grid)
    update_index_page(title, category, excerpt, date_str, filename)

def update_index_page(title, category, excerpt, date_str, filename):
    """Injects the new card HTML into the top of the grid in index.html"""
    
    # The HTML Card snippet
    # Using a random image for now, can be customized later
    import random
    img_num = random.randint(1, 3)
    
    new_card_html = f'''
        <!-- Article: {title} -->
        <a href="insights/posts/{filename}" class="insight-card">
            <div class="insight-thumb-wrapper">
                <img src="assets/images/hero/img{img_num}.webp" alt="{title}" class="insight-thumb">
            </div>
            <div class="insight-content">
                <span class="insight-tag">{category}</span>
                <h2 class="insight-headline">{title}</h2>
                <p class="insight-excerpt">{excerpt}</p>
                <div class="insight-meta">
                    <div class="insight-author-img" style="background-image: url('assets/images/hero/img1.webp'); background-size: cover;"></div>
                    <div class="insight-author-text">
                        By <span class="insight-author-name">Reuben Hester</span> • {date_str}
                    </div>
                </div>
            </div>
        </a>
    '''

    try:
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            index_content = f.read()
            
        # Find the marker to insert after. We look for the start of the grid.
        # Ideally we'd have a comment <!-- GRID_START -->, but let's hook into the ID.
        marker = '<main class="insights-grid-container" id="articles-grid">'
        
        if marker in index_content:
            parts = index_content.split(marker)
            # parts[0] is everything before grid
            # parts[1] is everything inside grid + footer
            
            updated_content = parts[0] + marker + "\n" + new_card_html + parts[1]
            
            with open(INDEX_PATH, "w", encoding="utf-8") as f:
                f.write(updated_content)
            
            print(f"✅ Updated Index page: {INDEX_PATH}")
            print("\nSUCCESS! Your new article is ready to edit.")
            print(f"Open this file to write your content: {os.path.abspath(POSTS_DIR)}/{filename}")
            
        else:
            print("Warning: Could not find insertion point in index.html. You may need to add the link manually.")

    except FileNotFoundError:
        print(f"Error: Index file not found at {INDEX_PATH}")

if __name__ == "__main__":
    create_new_post()
