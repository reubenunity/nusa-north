import os
from PIL import Image

def optimize_images(input_dir, output_dir, max_width=800):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_dir, output_filename)

            with Image.open(input_path) as img:
                # Convert to RGB if necessary (e.g. for WebP conversion from RGBA)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Resize if wider than max_width
                if img.width > max_width:
                    ratio = max_width / float(img.width)
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                
                # Save as WebP
                img.save(output_path, 'WEBP', quality=80)
                print(f"Optimized: {filename} -> {output_filename} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    team_dir = "/Users/reubenhester/Desktop/websites copy/nusa-north/assets/images/team"
    optimized_dir = os.path.join(team_dir, "optimized")
    optimize_images(team_dir, optimized_dir)
