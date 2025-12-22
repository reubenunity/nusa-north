import json
import glob
import os

print("| Page | Performance Score | LCP | FCP | CLS |")
print("|------|-------------------|-----|-----|-----|")

files = glob.glob("./reports/*.json")
for file_path in files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        filename = os.path.basename(file_path).replace('.json', '').replace('_', ' ').title()
        
        score = int(data['categories']['performance']['score'] * 100)
        lcp = data['audits']['largest-contentful-paint']['displayValue']
        fcp = data['audits']['first-contentful-paint']['displayValue']
        cls = data['audits']['cumulative-layout-shift']['displayValue']
        
        # Add status icon
        status = "🟢" if score >= 90 else "jq" if score >= 50 else "🔴"
        if score >= 50 and score < 90: status = "🟠"

        print(f"| {filename} | {score} {status} | {lcp} | {fcp} | {cls} |")
    except Exception as e:
        print(f"| {file_path} | Error | - | - | - |")
