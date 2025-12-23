import requests
import json

videos = [
    {"url": "https://vimeo.com/1148681925/1c440d73b7"},
    {"url": "https://vimeo.com/1148685522/7a947c5ad6"},
    {"url": "https://vimeo.com/1120102595/8d245ade90"},
    {"url": "https://vimeo.com/1143266792/307333a803"}
]

print("| URL | ID | Hash | Thumbnail URL | Title |")
print("|---|---|---|---|---|")

for v in videos:
    try:
        url = f"https://vimeo.com/api/oembed.json?url={v['url']}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            vid_id = data.get('video_id')
            title = data.get('title')
            thumb = data.get('thumbnail_url')
            
            # Extract hash from URL manually as oEmbed doesn't always give it
            url_parts = v['url'].split('/')
            hash_val = url_parts[-1].split('?')[0] if len(url_parts) > 4 else ""
            
            print(f"| {v['url']} | {vid_id} | {hash_val} | {thumb} | {title} |")
        else:
            print(f"| {v['url']} | - | - | FAILED ({response.status_code}) | - |")
    except Exception as e:
        print(f"| {v['url']} | - | - | ERROR: {e} | - |")
