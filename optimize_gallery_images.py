import os
from PIL import Image

# Configuration
SOURCE_DIR = 'assets/images/mobile-gallery'
TARGET_DIR = 'assets/images/mobile-gallery/optimized'
MAX_WIDTH = 1000
QUALITY = 80

def optimize_images():
    # Create target directory if it doesn't exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"Created directory: {TARGET_DIR}")

    # Process each file in the source directory
    for filename in os.listdir(SOURCE_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            source_path = os.path.join(SOURCE_DIR, filename)
            
            # Construct new filename with .webp extension
            name_without_ext = os.path.splitext(filename)[0]
            target_filename = f"{name_without_ext}.webp"
            target_path = os.path.join(TARGET_DIR, target_filename)

            try:
                with Image.open(source_path) as img:
                    # Calculate new dimensions maintaining aspect ratio
                    width, height = img.size
                    if width > MAX_WIDTH:
                        ratio = MAX_WIDTH / width
                        new_height = int(height * ratio)
                        img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
                        print(f"Resized {filename}: {width}x{height} -> {MAX_WIDTH}x{new_height}")
                    else:
                        print(f"Skipping resize for {filename} (width {width} <= {MAX_WIDTH})")

                    # Save as WebP
                    img.save(target_path, 'WEBP', quality=QUALITY, optimize=True)
                    
                    # Calculate savings
                    original_size = os.path.getsize(source_path)
                    new_size = os.path.getsize(target_path)
                    savings = (original_size - new_size) / original_size * 100
                    
                    print(f"Optimized {filename}: {original_size/1024/1024:.2f}MB -> {new_size/1024/1024:.2f}MB ({savings:.1f}% saved)")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    optimize_images()
