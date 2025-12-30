import os
from PIL import Image

def optimize_images(input_dir, output_dir, max_width=800):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0].replace(" ", "_") + '.webp'
            output_path = os.path.join(output_dir, output_filename)

            try:
                with Image.open(input_path) as img:
                    # Convert to RGB if necessary
                    if img.mode in ('RGBA', 'P'):
                        # Keep alpha for logos
                        pass
                    else:
                        img = img.convert('RGB')
                    
                    # Resize if wider than max_width
                    if img.width > max_width:
                        ratio = max_width / float(img.width)
                        new_height = int(img.height * ratio)
                        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                    
                    # Save as WebP
                    img.save(output_path, 'WEBP', quality=85)
                    print(f"Optimized: {filename} -> {output_filename} ({os.path.getsize(output_path)} bytes)")
            except Exception as e:
                print(f"Skipping {filename}: {e}")

if __name__ == "__main__":
    logos_dir = "/Users/reubenhester/Desktop/websites copy/nusa-north/Logos"
    optimized_dir = os.path.join(logos_dir, "optimized")
    optimize_images(logos_dir, optimized_dir, max_width=500) # Logos don't need to be huge
