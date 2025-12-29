
import os

HTML_FILES = [
    "booking.html",
    "files/floating-phones-hero.html",
    "files email/email-hero-final.html",
    "index.html",
    "insights/drafts/email-segmentation-for-vips.html",
    "insights/drafts/google-performance-max-friend-or-foe.html",
    "insights/drafts/the-death-of-the-link-in-bio.html",
    "insights/drafts/the-newsletter-reinassance.html",
    "insights/drafts/the-rise-of-silent-video.html",
    "insights/drafts/video-length-the-goldilocks-zone.html",
    "insights/drafts/why-best-practice-is-a-trap.html",
    "insights/drafts/why-your-roas-is-lying-to-you.html",
    "insights/index.html",
    "insights/posts/educational-email-flow.html",
    "insights/posts/educational-google-vs-meta.html",
    "insights/posts/educational-luxury-psychology.html",
    "insights/posts/educational-quiet-luxury.html",
    "insights/posts/educational-roas-vs-poas.html",
    "insights/posts/educational-scaling-creative.html",
    "insights/posts/educational-ugc-luxury.html",
    "insights/posts/educational-video-roi.html",
    "insights/posts/email-segmentation-for-vips.html",
    "insights/posts/four-seasons-bangkok.html",
    "insights/posts/google-performance-max-friend-or-foe.html",
    "insights/posts/harpers-bazaar.html",
    "insights/posts/hp-media-markt.html",
    "insights/posts/placeholder-1.html",
    "insights/posts/placeholder-2.html",
    "insights/posts/placeholder-3.html",
    "insights/posts/placeholder-4.html",
    "insights/posts/placeholder-5.html",
    "insights/posts/placeholder-6.html",
    "insights/posts/the-death-of-the-link-in-bio.html",
    "insights/posts/the-newsletter-reinassance.html",
    "insights/posts/the-rise-of-silent-video.html",
    "insights/posts/the-vietage.html",
    "insights/posts/video-length-the-goldilocks-zone.html",
    "insights/posts/why-best-practice-is-a-trap.html",
    "insights/posts/why-your-roas-is-lying-to-you.html",
    "insights/template.html",
    "meta_ads_mockup.html",
    "portfolio/illuzion.html",
    "privacy-policy.html",
    "services/content-strategy/index.html",
    "services/email-marketing/index.html",
    "services/google-ads/index.html",
    "services/meta-ads/index.html",
    "services/performance-creative/index.html",
    "services/photography/index.html",
    "terms.html"
]

def inject_cta(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already injected
        if 'class="mobile-nav-cta"' in content:
            print(f"Skipping {file_path} (Already injected)")
            return

        # Locate the mobile menu button
        target_str = '<button class="mobile-menu-btn" aria-label="Toggle Navigation">'
        
        if target_str not in content:
            print(f"Skipping {file_path} (Button not found)")
            return

        # Determine relative path to contact anchor
        # If in root (e.g. index.html), use "#contact"
        # If in subdir (e.g. services/abc/), use "../../index.html#contact"
        # This is a bit tricky, simpler to assume consistent structure or just link to /#contact if web server handles it
        # Safest is to rely on what 'logo' uses or similar reference.
        
        # Let's inspect the logo link to guess relative root
        logo_tag = 'class="logo">nusa<span>&</span>north</a>'
        root_path = "/" # Default absolute
        
        # Simple heuristic: count depth
        depth = file_path.count('/')
        if depth == 0:
            link = "#contact"
        elif depth == 1: # e.g. insights/index.html
            link = "../index.html#contact"
        elif depth == 2: # e.g. services/google-ads/index.html
            link = "../../index.html#contact"
        elif depth == 3: # e.g. insights/posts/abc.html
            link = "../../index.html#contact"
        else:
            link = "/#contact" # Fallback

        # Check file content for existing logo href to be sure?
        # Actually, let's just make the replacement with a wrapper.
        
        # Replacement HTML
        # We wrap the existing button and the new link in a div, OR just place them side by side?
        # The CSS uses .nav-controls { display: flex }. 
        # So we should wrap them if possible, or just insert the link BEFORE the button and let the parent nav handle flex?
        # The parent nav usually has `justify-content: space-between`.
        # Structure: Logo ... [Links] ... [Mobile Button]
        # We want: Logo ... [Links] ... [CTA + Mobile Button]
        
        # Let's wrap them in a .nav-controls div to strictly group them on mobile.
        # BUT this might break existing desktop layout if .nav-controls isn't handled on desktop.
        # .nav-controls is defined in our new CSS. 
        # Let's try inserting the CTA *before* the button.
        
        new_html = f'''
        <div class="nav-controls">
            <a href="{link}" class="mobile-nav-cta">Book</a>
            <button class="mobile-menu-btn" aria-label="Toggle Navigation">'''
            
        transformed_content = content.replace(target_str, new_html)
        
        # We need to close the div? 
        # Wait, if I replace `<button...>` with `<div...><a...><button...>`, the closing `</button>` is still there. 
        # I need to close the div AFTER the button closes. 
        # This is risky with simple replace if I don't match the closing tag.
        
        # Alternative: Just insert the <a> before the <button>.
        # <a ...>Book</a>
        # <button ...>
        # And rely on the parent flex container?
        # On mobile, the parent is <nav>. <nav> has justify-content: space-between.
        # If I have logo, links (hidden), CTA, Button... 
        # Space between will put CTA in middle? 
        # That's why I added .nav-controls style in CSS.
        
        # Regex replacement might be safer to wrap the button.
        import re
        # Pattern: <button class="mobile-menu-btn".*?</button>
        # We replace it with <div class="nav-controls"><a...>Book</a> <button ...></button></div>
        
        pattern = re.compile(r'(<button class="mobile-menu-btn".*?</button>)', re.DOTALL)
        
        def replacement(match):
            btn_html = match.group(1)
            return f'<div class="nav-controls"><a href="{link}" class="mobile-nav-cta">Book</a>\n        {btn_html}</div>'

        transformed_content = pattern.sub(replacement, content)

        if transformed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(transformed_content)
            print(f"Updated {file_path}")
        else:
            print(f"No match in {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Run
for file in HTML_FILES:
    if os.path.exists(file):
        inject_cta(file)
    else:
        print(f"File not found: {file}")
