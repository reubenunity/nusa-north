import requests
import json

videos = [
    {"url": "https://vimeo.com/1123943736/b2bba13bf5"},
    {"url": "https://vimeo.com/1143266792/307333a803"},
    {"url": "https://vimeo.com/1148681612/edb5af0005"},
    {"url": "https://vimeo.com/1148681925/1c440d73b7"}
]

print("| URL | ID | Hash | Thumbnail URL | Title | Width | Height |")
print("|---|---|---|---|---|---|---|")

for v in videos:
    try:
        url = f"https://vimeo.com/api/oembed.json?url={v['url']}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            vid_id = data.get('video_id')
            title = data.get('title')
            thumb = data.get('thumbnail_url')
            width = data.get('width')
            height = data.get('height')
            
            # Extract hash from URL
            url_parts = v['url'].split('/')
            hash_val = url_parts[-1] if len(url_parts) > 4 and url_parts[-1][0].isalnum() else ""
            
            print(f"| {v['url']} | {vid_id} | {hash_val} | {thumb} | {title} | {width} | {height} |")
        else:
            print(f"| {v['url']} | - | - | FAILED ({response.status_code}) | - | - | - |")
    except Exception as e:
        print(f"| {v['url']} | - | - | ERROR: {e} | - | - | - |")
