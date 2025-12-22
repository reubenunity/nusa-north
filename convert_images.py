import os
from PIL import Image

def convert_to_webp(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                file_name, _ = os.path.splitext(file)
                webp_path = os.path.join(root, file_name + '.webp')
                
                # Check if WebP already exists
                if os.path.exists(webp_path):
                    print(f"Skipping {file}, WebP already exists.")
                    continue
                
                # Check file size (skip if < 100KB to save time/quality for tiny icons)
                if os.path.getsize(file_path) < 100 * 1024:
                    print(f"Skipping {file}, too small.")
                    continue

                try:
                    img = Image.open(file_path)
                    img.save(webp_path, 'WEBP', quality=85)
                    print(f"Converted {file} to WebP")
                except Exception as e:
                    print(f"Failed to convert {file}: {e}")

if __name__ == "__main__":
    convert_to_webp('.')
