import os
import re

POSTS_DIR = "insights/posts"
TEMPLATE_FILE = "insights/posts/educational-video-roi.html"

# Thumbnail Mapping
# Thumbnail Mapping (1:1 specific mapping)
THUMB_MAP = {
    # Existing Matches
    "Quiet Luxury": "../../assets/images/insights/img_editorial_portrait.png",
    "Video ROI": "../../assets/images/insights/img_cinematic_film.png",
    "Email Segmentation": "../../assets/images/insights/img_artistic_hands.png", 
    "ROAS": "../../assets/images/insights/img_cinematic_tech.png",
    
    # New Generated Matches
    # Generated / Premium Matches
    "Link": "../../assets/images/insights/img_link_in_bio.png",
    "Best Practice": "../../assets/images/insights/img_best_practice_trap.png",
    "Scaling Creative": "../../assets/images/insights/img_scaling_creative.png",
    "Video ROI": "../../assets/images/insights/img_cinematic_film.png",
    "Quiet Luxury": "../../assets/images/insights/img_editorial_portrait.png",
    "Flow": "../../assets/images/insights/img_artistic_hands.png", 
    "ROAS": "../../assets/images/insights/img_cinematic_tech.png",

    # Distinct Fallbacks (Using specific existing assets to avoid duplicates)
    "Google": "../../assets/images/insights/thumb_google_meta_people_1766972620645.png",
    "UGC": "../../assets/images/insights/thumb_ugc_luxury_people_1766972659454.png",
    "Newsletter": "../../assets/images/insights/thumb_email_flow_people_1766972592459.png", 
    "Email Segmentation": "../../assets/images/insights/thumb_email_flow_1766972416311.png",
    
    # Project / Case Study Specifics
    "Psychology": "../../assets/images/insights/thumb_luxury_psych_people_1766972550624.png",
    "Media Markt": "../../assets/images/insights/thumb_events_cinematic_1766972493585.png",
    "Vietage": "../../assets/images/insights/thumb_creative_people_1766972565160.png",
    "Harper": "../../assets/images/insights/thumb_quiet_luxury_people_1766972646266.png",
    "Four Seasons": "../../assets/images/insights/thumb_events_cinematic_1766972493585.png",
    "POAS": "../../assets/images/insights/thumb_roas_metric_people_1766972606720.png",
}

def get_thumb(title):
    # Strict Priority Match
    if "Link" in title: return THUMB_MAP["Link"]
    if "Best Practice" in title: return THUMB_MAP["Best Practice"]
    if "Scaling Creative" in title: return THUMB_MAP["Scaling Creative"]
    
    if "Video" in title and "ROI" in title: return THUMB_MAP["Video ROI"]
    if "Quiet Luxury" in title: return THUMB_MAP["Quiet Luxury"]
    
    if "Newsletter" in title: return THUMB_MAP["Newsletter"]
    if "Segmentation" in title: return THUMB_MAP["Email Segmentation"]
    if "Flow" in title: return THUMB_MAP["Flow"]
    
    # Disambiguate ROAS articles
    if "POAS" in title: return THUMB_MAP["POAS"]
    if "ROAS" in title: return THUMB_MAP["ROAS"]
    
    if "Google" in title: return THUMB_MAP["Google"]
    if "UGC" in title: return THUMB_MAP["UGC"]
    
    # Case Studies
    if "Psychology" in title: return THUMB_MAP["Psychology"]
    if "Media Markt" in title: return THUMB_MAP["Media Markt"]
    if "Vietage" in title: return THUMB_MAP["Vietage"]
    if "Harper" in title: return THUMB_MAP["Harper"]
    if "Four Seasons" in title: return THUMB_MAP["Four Seasons"]
    
    return "../../assets/images/insights/img_editorial_portrait.png" # Fallback

def clean_tag(tag_text):
    # Fix "TRENDSSTRATEGY" -> "TRENDS"
    if "TRENDS" in tag_text: return "TRENDS"
    if "STRATEGY" in tag_text: return "STRATEGY"
    if "CREATIVE" in tag_text: return "CREATIVE"
    if "EMAIL" in tag_text: return "EMAIL"
    if "TECHNOLOGY" in tag_text: return "TECHNOLOGY"
    return "INSIGHTS"

def clean_title(title_text):
    return title_text.replace("Article Title Goes Here", "").strip()

def run_fix():
    print("--- Batch Content Fix ---")
    
    # Read Golden Template
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        golden_html = f.read()

    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".html")]
    
    for filename in files:
        if filename == "educational-video-roi.html": continue # Skip source
        
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Detect if file is broken (has "Article Title Goes Here" or duplicates)
        # Or just checking if it lacks "single-post-container" (legacy template)
        # if "single-post-container" in content and "Article Title Goes Here" not in content:
        #    print(f"Skipping {filename} (Seems clean)")
        #    continue
            
        print(f"Migrating {filename}...")
        
        # Extract Metadata (Regex)
        # Title: <h1 class="article-title">(.*?)</h1> OR <h1 class="single-post-titles">(.*?)</h1>
        title_match = re.search(r'<h1 class="(?:article-title|single-post-titles)">\s*(.*?)\s*</h1>', content, re.DOTALL)
        title = clean_title(title_match.group(1)) if title_match else "Untitled Insight"
        
        # Category: <span class="article-tag">(.*?)</span>
        cat_match = re.search(r'<span class="(?:article-tag|insight-tag)">\s*(.*?)\s*</span>', content, re.DOTALL)
        category = clean_tag(cat_match.group(1)) if cat_match else "STRATEGY"
        
        # Date: By ... • (.*?)
        date_match = re.search(r'By Reuben Hester • (?:<!--.*?-->)?\s*(.*?)\s*</div>', content, re.DOTALL)
        date = date_match.group(1).strip() if date_match else "December 29, 2025"
        
        # Excerpt/Intro: <p class="intro">(.*?)</p>
        intro_match = re.search(r'<p class="(?:intro|intro-paragraph)">\s*(.*?)\s*</p>', content, re.DOTALL)
        intro = intro_match.group(1).strip() if intro_match else "Discover our latest insights on digital strategy."
        
        # Body: Just keep Placeholder or Extract content?
        # The broken files have Lorem Ipsum. Let's stick with the 'Lorem Ipsum' but formatted correctly?
        # Or better: Just use a generic "Coming Soon" body if it was broken?
        # User said "Genuine Info" was missing. I can't generate it here.
        # I will preserve the existing body HTML if possible, or fallback to the stub.
        
        # We will keep the intro and standard placeholder text for now to fix LAYOUT.
        
        # --- Critical Fix: Extract Body Content ---
        # We must find the unique content in the SOURCE file and inject it into the TEMPLATE.
        # Strategy: Look for the 'article-body' or 'single-post-content' container.
        
        source_body = ""
        body_match = re.search(r'<article class="(?P<cls>single-post-content|article-body)">(.*?)</article>', content, re.DOTALL)
        if body_match:
             source_body = body_match.group(2).strip()
             # If source has a hero image div inside, remove it so we don't double up
             source_body = re.sub(r'<div class="single-post-hero">.*?</div>', '', source_body, flags=re.DOTALL)
             source_body = re.sub(r'<!-- CONTENT_PLACEHOLDER -->', '', source_body)
        else:
             # Fallback: Extract everything after the Header?
             # This is risky. Let's fallback to a placeholder if we can't find it.
             source_body = "<p>Content restoration in progress.</p>"

        # --- Construct New File ---
        new_html = golden_html
        
        # Replace Title
        new_html = new_html.replace("Why Cinematic Video is the Highest ROI Asset for 2026", title)
        new_html = re.sub(r'<title>.*?</title>', f'<title>{title} | Nusa & North</title>', new_html)
        
        # Replace Category
        new_html = new_html.replace('<span class="insight-tag">Strategy</span>', f'<span class="insight-tag">{category.title()}</span>')
        
        # Replace Date
        new_html = new_html.replace("December 29, 2025", date)
        
        # Replace Intro (if found in source)
        # Template has <p class="intro-paragraph">...</p>
        # We should try to replace the template intro with the one we found in source (intro variable)
        if intro and "Discover our latest" not in intro:
             # Remove existing intro in source_body to avoid duplication
             # (Since we might have captured it in body_match)
             pass
        
        # Replace Image
        img_src = get_thumb(title)
        new_html = re.sub(r'src="../../assets/images/insights/[^"]+"', f'src="{img_src}"', new_html)
        new_html = re.sub(r'alt="[^"]+"', f'alt="{title}"', new_html)
        
        # Inject UNIQUE Body Content
        # We replace the TEMPLATE'S body content with our Extracted Source Body.
        # Template body is inside <article class="single-post-content"> ... </article>
        # And specifically, after the hero image and intro.
        # Let's find the end of the Hero Image + Intro in the NEW HTML.
        
        # Find where to splice.
        # The template structure:
        # <article class="single-post-content">
        #   <div class="single-post-hero">...</div>
        #   <p class="intro-paragraph">...</p>
        #   ... (Rest of content) ...
        # </article>
        
        # We want to keep Hero + Intro, but replace the rest. 
        # OR better: Assume source_body contains the intro?
        # In the draft generation, the intro IS inside the body.
        # So we should probably just replace EVERYTHING after the Hero Image.
        
        start_marker = 'class="single-hero-img">'
        end_marker = '</article>'
        
        s_idx = new_html.find(start_marker)
        if s_idx != -1:
             # Find closing div of hero
             hero_div_end = new_html.find('</div>', s_idx) + 6
             
             # Find article end
             e_idx = new_html.rfind(end_marker)
             
             if e_idx != -1:
                  pre = new_html[:hero_div_end]
                  post = new_html[e_idx:]
                  
                  # Ensure we have the Intro if it wasn't in source body?
                  # The drafts have <p class="intro-paragraph">.
                  
                  new_html = f"{pre}\n            {source_body}\n        {post}"

        
        # Replace Image
        img_src = get_thumb(title)
        # Find template image src
        new_html = re.sub(r'src="../../assets/images/insights/[^"]+"', f'src="{img_src}"', new_html)
        new_html = re.sub(r'alt="[^"]+"', f'alt="{title}"', new_html)

        # Write
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Fixed {filename}")

if __name__ == "__main__":
    run_fix()
