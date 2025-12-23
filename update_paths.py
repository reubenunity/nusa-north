import os
import re

service_dirs = [
    "google-ads",
    "meta-ads",
    "performance-creative",
    "email-marketing",
    "content-strategy",
    "photography"
]

base_dir = "/Users/reubenhester/Desktop/websites copy/nusa-north/services"

for s_dir in service_dirs:
    idx_path = os.path.join(base_dir, s_dir, "index.html")
    if not os.path.exists(idx_path):
        print(f"Skipping {idx_path} - not found")
        continue

    print(f"Processing {idx_path}...")
    with open(idx_path, 'r') as f:
        content = f.read()

    # 1. Update Logo Link: <a href="/" ... or <a href="../index.html" ...
    # It was previously replaced by me to "/" but I should ensure it's correct if I missed some
    # Actually, if I used "/" it should be fine. But let's check.
    
    # 2. Update Image/Asset paths: ../images/ -> ../../images/  and ../assets/ -> ../../assets/
    content = content.replace('src="../images/', 'src="../../images/')
    content = content.replace('src="../assets/', 'src="../../assets/')
    
    # Also backgrounds in style attributes
    content = content.replace('url(\'../images/', 'url(\'../../images/')
    content = content.replace('url("../images/', 'url("../../images/')
    
    # 3. Update Nav Dropdown links: 
    # Current links in subfolder index.html might look like: <a href="google-ads.html"> 
    # but they are now in the SAME folder level as the dropdown? 
    # No, services/google-ads/index.html is the file. 
    # The dropdown entries were previously e.g. <a href="google-ads.html"> in photography.html
    # Now in photography/index.html, they should point to ../google-ads/
    
    # First, fix a common pattern if they exist
    for other_dir in service_dirs:
        # Replace filename.html with ../filename/
        content = content.replace(f'href="{other_dir}.html"', f'href="../{other_dir}/"')
        # Handle cases where they might already be cleaned in the source but need folder adjustment
        # If I already had them as 'google-ads.html' it should be fine.
    
    # 4. Update relative links to root sections
    # e.g. href="/#work" is already absolute-ish if it starts with /, but usually they were ../index.html#work
    # I already replaced ../index.html with / in previous step.
    # So /#work is fine if hosted at root. 
    
    with open(idx_path, 'w') as f:
        f.write(content)

print("Done.")
