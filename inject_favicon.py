import os

target_files = [
    f"services/{d}/index.html" for d in os.listdir("services") 
    if os.path.isdir(f"services/{d}") and os.path.exists(f"services/{d}/index.html")
]

favicon_line = '    <link rel="icon" type="image/png" href="../../assets/images/favicon-new.png">\n'

for file_path in target_files:
    with open(file_path, "r") as f:
        content = f.read()
    
    if "favicon-new.png" in content:
        print(f"Skipping {file_path} (already has favicon)")
        continue
        
    lower_content = content.lower()
    head_end = lower_content.find("</head>")
    
    if head_end != -1:
        new_content = content[:head_end] + favicon_line + content[head_end:]
        with open(file_path, "w") as f:
            f.write(new_content)
        print(f"Injected favicon into {file_path} before </head>")
    else:
        body_start = lower_content.find("<body")
        if body_start != -1:
            new_content = content[:body_start] + favicon_line + content[body_start:]
            with open(file_path, "w") as f:
                f.write(new_content)
            print(f"Injected favicon into {file_path} before <body>")
        else:
            print(f"ERROR: Could not find </head> or <body> in {file_path}")

