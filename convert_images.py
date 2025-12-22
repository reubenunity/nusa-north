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
                    # Optional: Delete original even if WebP exists, to clean up
                    try:
                        os.remove(file_path)
                        print(f"Deleted original {file} (WebP existed)")
                    except Exception as e:
                        print(f"Error deleting {file}: {e}")
                    continue
                
                # Check file size (skip if < 100KB to save time/quality for tiny icons)
                if os.path.getsize(file_path) < 100 * 1024:
                    print(f"Skipping {file}, too small.")
                    continue

                try:
                    with Image.open(file_path) as img:
                        img.save(webp_path, 'WEBP', quality=85)
                        print(f"Converted {file} to WebP.")
                        os.remove(file_path) # Delete original after conversion
                        print(f"Deleted original {file}")
                except Exception as e:
                    print(f"Failed to convert {file}: {e}")

if __name__ == "__main__":
    convert_to_webp('.')
