import os

# Configuration
TARGET_DIR = "/Users/reubenhester/Desktop/websites copy/nusa-north"
CLARITY_SCRIPT = """
    <!-- Microsoft Clarity -->
    <script type="text/javascript">
        (function(c,l,a,r,i,t,y){
            c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", "CLARITY_PROJECT_ID_HERE");
    </script>
"""

def inject_clarity(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already injected
        if "clarity.ms/tag/" in content:
            print(f"Skipping (already exists): {file_path}")
            return False

        # Find injection point
        if "</head>" in content:
            new_content = content.replace("</head>", f"{CLARITY_SCRIPT}\n</head>")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected: {file_path}")
            return True
        else:
            print(f"Skipping (no </head> tag): {file_path}")
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
                if inject_clarity(file_path):
                    count += 1
    
    print(f"\nTotal files updated: {count}")

if __name__ == "__main__":
    main()
