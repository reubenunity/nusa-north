import os

# Configuration
TARGET_DIR = "/Users/reubenhester/Desktop/websites copy/nusa-north"
PLACEHOLDER = "CLARITY_PROJECT_ID_HERE"
NEW_ID = "utbi0oux59"

def update_id(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if PLACEHOLDER in content:
            new_content = content.replace(PLACEHOLDER, NEW_ID)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    count = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                if update_id(file_path):
                    count += 1
    
    print(f"\nTotal files updated: {count}")

if __name__ == "__main__":
    main()
