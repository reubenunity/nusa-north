import re

path = 'index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define generic grid item content to replicate
generic_item = """
                <div class="grid-item">
                    <img src="assets/images/hero/img1.webp" alt="Visual">
                </div>"""

# Define columns structure
columns_html = ""

# Create 5 columns (instead of original few) with many items each
# We will alternate animation directions
for i in range(5):
    direction = "col-anim-up" if i % 2 == 0 else "col-anim-down"
    
    # Generate 8 items per column for vertical density
    items_html = ""
    for j in range(8):
        # Cycle through images 1-4 for variety if possible, or just use placeholders
        img_num = (j % 4) + 1 
        items_html += f"""
                <div class="grid-item">
                    <img src="assets/images/hero/img{img_num}.webp" alt="Visual {img_num}" onerror="this.src='assets/images/hero/img1.webp'">
                </div>"""
        
    columns_html += f"""
            <div class="grid-column {direction}">
                {items_html}
            </div>"""

# Regex to replace the content of .floating-grid
# We look for <div class="floating-grid"> ... </div>
# This is a bit risky with regex but the structure is known.
pattern = r'(<div class="floating-grid">)(.*?)(</div>)'
replacement = f'\\1{columns_html}\n        \\3'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated floating-grid with high density columns.")
