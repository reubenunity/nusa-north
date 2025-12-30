import os
from PIL import Image

def get_dimensions(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
            path = os.path.join(directory, filename)
            try:
                with Image.open(path) as img:
                    print(f"{filename}: {img.width}x{img.height}")
            except Exception as e:
                print(f"Error reading {filename}: {e}")

if __name__ == "__main__":
    print("Logos:")
    get_dimensions("/Users/reubenhester/Desktop/websites copy/nusa-north/Logos/optimized")
    print("\nProcess Images:")
    get_dimensions("/Users/reubenhester/Desktop/websites copy/nusa-north/assets/images/services")
