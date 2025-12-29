import os

DIR = 'assets/images/mobile-gallery/optimized'

files = []
for f in os.listdir(DIR):
    if f.endswith('.webp'):
        path = os.path.join(DIR, f)
        size = os.path.getsize(path)
        files.append({'name': f, 'size': size})

# Deduplicate by size
unique_files = {}
for f in files:
    # Key by size for simple dedup
    if f['size'] not in unique_files:
        unique_files[f['size']] = f['name']
    else:
        # If we already have a file, prefer "DSC" or "Screenshot" or descriptive over "gallery-XX"
        # because gallery-XX were likely the old ones
        current = unique_files[f['size']]
        if 'gallery-' in current and 'gallery-' not in f['name']:
             unique_files[f['size']] = f['name']

# Sort by name for consistency
sorted_files = sorted(unique_files.values())

print(f"Found {len(sorted_files)} unique images.")

# Split into two rows
mid = len(sorted_files) // 2
row1 = sorted_files[:mid]
row2 = sorted_files[mid:]

print("\n--- ROW 1 ---")
for img in row1:
    print(f'<div class="strip-item"><img src="../../assets/images/mobile-gallery/optimized/{img}" alt="Gallery" loading="lazy"></div>')

print("\n--- ROW 2 ---")
for img in row2:
    print(f'<div class="strip-item"><img src="../../assets/images/mobile-gallery/optimized/{img}" alt="Gallery" loading="lazy"></div>')
