
import os
import re
import time

# Timestamp for cache busting
TIMESTAMP = int(time.time())
print(f"Timestamp: {TIMESTAMP}")

# Regex to find CSS links
# Matches <link rel="stylesheet" href="style.css"> or similar
# Group 1: The quote (Applies to href=)
# Group 2: The file path
CSS_PATTERN = re.compile(r'(<link[^>]+href=)(["\'])(.*?\.css)(["\'])', re.IGNORECASE)

def bust_cache(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Function to append version
                def replace_link(match):
                    prefix = match.group(1)
                    quote = match.group(2)
                    url = match.group(3)
                    end_quote = match.group(4)
                    
                    # Remove existing query params if any
                    if '?' in url:
                        url = url.split('?')[0]
                        
                    new_url = f"{url}?v={TIMESTAMP}"
                    return f"{prefix}{quote}{new_url}{end_quote}"
                
                new_content = CSS_PATTERN.sub(replace_link, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

if __name__ == "__main__":
    bust_cache(".")
