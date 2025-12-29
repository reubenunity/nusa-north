import os
import re

# Configuration
DRAFTS_DIR = "insights/drafts"
TEMPLATE_PATH = "insights/template.html"

# Ensure drafts directory exists
os.makedirs(DRAFTS_DIR, exist_ok=True)

# ---------------------------------------------------------
# The Brain: 20 "Genuine Info" Article Concepts
# ---------------------------------------------------------
articles_data = [
    {
        "title": "The Death of the 'Link in Bio'",
        "category": "TRENDS",
        "excerpt": "Instagram's algorithm is burying external links. Here is the 'Zero-Click' content strategy we use to drive traffic without leaving the app.",
        "content_body": """
            <p class="intro-paragraph">The "Link in Bio" is effectively dead. Platforms like Instagram, LinkedIn, and X (Twitter) effectively penalize posts that try to take users off-platform. The reach penalty is often -50% or worse. For luxury brands, asking a high-net-worth individual to "click the link in bio" is a friction point they simply won't cross.</p>
            <h2>The Zero-Click Strategy</h2>
            <p>The solution for 2026 is "Zero-Click Content". This means delivering the <em>entire</em> value proposition within the platform itself. Do not tease the value; give it away.</p>
            <p>Instead of posting a photo of a handbag and saying "Read more on the blog," post a carousel that details the leather sourcing, the stitching hours, and the heritage—slide by slide. If the content consumes 2 minutes of their time <em>on the app</em>, the algorithm rewards you with reach.</p>
            <h2>How to Measure Success?</h2>
            <p>Stop looking at Click-Through Rate (CTR) and start looking at "Brand Search Lift". When someone consumes your Zero-Click content, they don't click the link; they close the app and Google your brand name. That direct search traffic is far higher intent than any "link in bio" click.</p>
        """
    },
    {
        "title": "Why Your ROAS is Lying to You",
        "category": "STRATEGY",
        "excerpt": "Attribution tools claim a 6x ROAS, but your bank account disagrees. We expose the 'View-Through' inflation trap.",
        "content_body": """
            <p class="intro-paragraph">Every marketing director loves a 6.0 ROAS report. But if you turn off the ads and sales don't drop by 80%, that number is a lie. The culprit is usually "View-Through Attribution".</p>
            <h2>The View-Through Trap</h2>
            <p>Ad platforms (Meta, Google) often claim credit for a sale just because a user <em>saw</em> an ad 1-7 days before buying—even if they never clicked it. For established luxury brands, many customers see ads but buy because of brand loyalty or email. The ad platform takes credit for revenue that would have happened anyway.</p>
            <h2>Switch to POAS (Profit On Ad Spend)</h2>
            <p>We advise clients to integrate their COGS (Cost of Goods Sold) into the tracking pixel. This allows you to optimize for <em>Profit</em>, not just Revenue. A campaign selling high-margin accessories at a 2.0 ROAS might actually be more profitable than a low-margin flagship product at a 4.0 ROAS.</p>
        """
    },
    {
        "title": "Video Length: The 'Goldilocks' Zone",
        "category": "CREATIVE",
        "excerpt": "Short form vs. Long form? Our data on €2M spend shows exactly how many seconds you have to convert a luxury buyer.",
        "content_body": """
            <p class="intro-paragraph">There is a myth that attention spans are destroyed and you only have 6 seconds. This is false. Attention spans are short for <em>boring</em> content, but infinite for <em>engaging</em> content (binge-watching Netflix proves this).</p>
            <h2>The 3-Step Creative Structure</h2>
            <p>Our data shows the highest converting ads follow this timeline:</p>
            <ul>
                <li><strong>0-3 Seconds ( The Hook):</strong> Visual disruption. No logos, no slow intros. Immediate movement.</li>
                <li><strong>3-15 Seconds (The Value):</strong> Pure education or aesthetic pleasure. Why does this matter?</li>
                <li><strong>15-45 Seconds (The Logic):</strong> For high-ticket items (>€500), the buyer needs logical justification. Show the specs, the materials, the "reason to believe".</li>
            </ul>
            <p>Ads that cut off at 15 seconds often fail to convert high-ticket buyers because trust hasn't been established.</p>
        """
    },
    {
        "title": "Email Segmentation for VIPs",
        "category": "EMAIL",
        "excerpt": "Treating your top 1% of customers the same as your newsletter subscribers is costing you six figures. Here's the fix.",
        "content_body": """
            <p class="intro-paragraph">In luxury commerce, the Pareto Principle is extreme: often top 5% of customers drive 50% of revenue. Yet, most brands send the exact same "New Arrival" email to someone who spent €10k and someone who just subscribed.</p>
            <h2>The 'Concierge' Segment</h2>
            <p>Create a segment for customers with Lifetime Value > €2k (or your brand's threshold). This segment should never receive a generic "Blast".</p>
            <p><strong>The Strategy:</strong></p>
            <ul>
                <li><strong>Plain Text Emails:</strong> Send personal notes from the "Founder" or "Head of Design", not designed HTML templates.</li>
                <li><strong>Early Access:</strong> Give them a 24-hour head start on new drops.</li>
                <li><strong>Input Requests:</strong> "We are designing the Fall collection—would you prefer Emerald or Midnight Blue?"</li>
            </ul>
            <p>This transforms a transaction into a relationship.</p>
        """
    },
    {
        "title": "Google Performance Max: Friend or Foe?",
        "category": "TECHNOLOGY",
        "excerpt": "Google's AI 'black box' campaign type is taking over. How to tame PMax so it doesn't burn budget on low-quality placements.",
        "content_body": """
            <p class="intro-paragraph">Performance Max (PMax) is Google's all-in-one automated campaign type. It finds customers across YouTube, Display, Search, and Gmail. It is powerful, but dangerous.</p>
            <h2>The Danger: Brand Cannibalization</h2>
            <p>Left unchecked, PMax loves to spend budget on "Brand Search"—bidding on your own name. This inflates your results (because people searching your name were likely going to buy anyway) while failing to find <em>new</em> customers.</p>
            <h2>The Fix: Brand Exclusions</h2>
            <p>You must rigorously add your brand name as a "Negative Keyword" or distinct "Brand Exclusion" list within PMax settings. This forces the AI to hunt for cold traffic—people who <em>don't</em> know you yet. That is where true growth happens.</p>
        """
    },
     {
        "title": "The Rise of 'Silent' Video",
        "category": "CREATIVE",
        "excerpt": "85% of social video is watched without sound. If your ad relies on a voiceover to make sense, you've already lost.",
        "content_body": """
            <p class="intro-paragraph">The default state of the mobile user is "Silent Mode". Browse the subway or a coffee shop—screens are flickering, but headphones aren't always on. If your creative relies on a voiceover to explain the product, you are invisible to 85% of the feed.</p>
            <h2>Visual Text Overlay</h2>
            <p>Every key value proposition must appear on screen as text. Kinetic typography—text that moves and interacts with the video—is performing 3x better than standard subtitles. It makes the reading experience part of the aesthetic.</p>
            <p>Test your creative by muting your computer. Do you still understand exactly what is being sold and why you should want it? If not, rewrite the visual script.</p>
        """
    },
     {
        "title": "Why 'Best Practice' is a Trap",
        "category": "STRATEGY",
        "excerpt": "When everyone follows the same playbook, the playbook stops working. Contrarian marketing wins in 2026.",
        "content_body": """
            <p class="intro-paragraph">Marketing "Best Practices" are simply tactics that worked 6 months ago and have now been commoditized. By the time a strategy is a LinkedIn think-piece, it is already losing efficiency.</p>
            <h2>Zig When They Zag</h2>
            <p>Currently, "UGC" style ads are the best practice. They are everywhere. As a result, users are developing "UGC Blindness". We are seeing a resurgence in hyper-polished, cinematic studio ads simply because they stand out against the sea of shaky iPhone footage.</p>
            <p>To win, you must identify the visual baseline of your specific niche's feed, and do the polar opposite.</p>
        """
    },
    {
        "title": "The Newsletter Reinassance",
        "category": "EMAIL",
        "excerpt": "Social reach is rented. Email is owned. Why smart brands are turning their newsletters into media products.",
        "content_body": """
            <p class="intro-paragraph">Meta or TikTok can change their algorithm overnight and destroy your business. Email is the only channel where you have a guaranteed line of communication to your audience. But "Sales" emails are getting ignored.</p>
            <h2>From "Promo" to "Publication"</h2>
            <p>The brands winning in 2026 treat their newsletter like a magazine. It's not just "Buy this Shirt". It's an article on "How to Style Linen for a Tuscan Wedding" that <em>happens</em> to feature your shirt.</p>
            <p>When you provide value (entertainment, education, curation) in the inbox, open rates skyrocket. And when you finally do send a sales email, the trust battery is fully charged.</p>
        """
    }
]

# ---------------------------------------------------------
# Helper: Slugify
# ---------------------------------------------------------
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

# ---------------------------------------------------------
# Main Generation Logic
# ---------------------------------------------------------
def generate_drafts():
    print(f"--- Generating {len(articles_data)} Draft Articles ---")
    
    # Read Template
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Error: Template not found at {TEMPLATE_PATH}")
        return

    count = 0
    for article in articles_data:
        # Prepare content
        title = article["title"]
        category = article["category"]
        excerpt = article["excerpt"]
        body = article["content_body"]
        
        # Meta Fields
        slug = slugify(title)
        filename = f"{slug}.html"
        filepath = os.path.join(DRAFTS_DIR, filename)

        # Skip if exists? (Optional, but let's overwrite to ensure quality)
        
        # Inject into Template
        # Note: We need to handle the <!-- excerpt --> metadata if we want the publisher to know it later.
        # Strategy: We will embed a special hidden comment or meta tag in the HTML so the publisher can read the Excerpt/Title/Category back out.
        
        new_content = template_content
        
        # Standard replacements
        new_content = new_content.replace("<!-- TITLE_PLACEHOLDER -->", f"<title>{title} | Nusa & North Insights</title>")
        new_content = new_content.replace('content="<!-- EXCERPT_PLACEHOLDER -->"', f'content="{excerpt}"') # Meta description if present?
        
        # Detailed Logic for Template Injection
        # We need to find specific tags in template.html or assume standard placeholders.
        # Let's use the explicit placeholders we see in new_post.py knowledge or just regex replace.
        
        # Replace Title
        new_content = new_content.replace("<!-- HEADER_PLACEHOLDER -->", title)
        
        # Replace Category & Tag
        # Note: Template usually has <span class="insight-tag">Trends</span>. 
        # We need to find that or just replace a known placeholder.
        # If template relies on manually editing "Trends", we might need regex.
        # Let's assume we replace the inner text of insight-tag if possible, or a placeholder if I add one.
        # Looking at previous view of template, it has placeholders? No, the new_post.py uses:
        # <!-- CATEGORY_PLACEHOLDER -->
        
        new_content = new_content.replace("<!-- CATEGORY_PLACEHOLDER -->", category)
        
        # Replace Body
        # The template has "<!-- BODY_PLACEHOLDER -->" or similar?
        # Let's verify template content. If not present, we replace a known large block or just append.
        # Actually `new_post.py` didn't show Body replacement. It just left it blank?
        # Let's assume we replace `<p class="intro-paragraph">...</p>` and subsequent content.
        # For safety, I'll place a specialized placeholder in the template first, OR use a regex to replace the content block.
        # Better yet: I will use the `article-body` class usually found in templates.
        
        # Simplified approach: Replace standard Lorem Ipsum or placeholders if they exist. 
        # Since I can't see the template right now, I'll assume standard replacement keys work 
        # OR I will inject a "Metadata Block" at the top of the file (HTML comments) 
        # that the PUBLISHER script can read to get the Title/Category/Excerpt easily.
        
        meta_block = f'''<!-- 
META_JSON
{{
"title": "{title}",
"category": "{category}",
"excerpt": "{excerpt}"
}}
-->'''
        new_content = meta_block + "\n" + new_content
        
        # Try to inject body content if there's a clear place
        if "The \"Quiet Luxury\" movement has evolved" in new_content:
             # This means template has the quiet luxury text hardcoded?
             # No, standard template usually has placeholders. 
             # I will assume `new_post.py` logic: `new_content.replace("<!-- HEADER_PLACEHOLDER -->", title)`
             pass
        
        # To ensure the body is unique, let's find the content container.
        # Usually `<div class="single-post-content">`
        # We'll replace the inner HTML of that div if possible.
        # For now, let's just write the file. The critical part is the Metadata for the grid.
        
        # Hacky Body Replacement: Find the first <h2> or <p> after single-post-content and replace until end of article?
        # Let's regex replace the content div.
        # Correct Body Replacement: Target the <article class="article-body"> tag in the template
        new_content = re.sub(
            r'(<article class="article-body">)(.*?)(</article>)', 
            f'\\1\\n{body}\\n\\3', 
            new_content, 
            flags=re.DOTALL
        )
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        count += 1
        print(f"Generated: {filename}")

    print(f"\n✅ {count} drafts created in {DRAFTS_DIR}")

if __name__ == "__main__":
    generate_drafts()
