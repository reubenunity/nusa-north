import requests
import json

videos = [
    {"url": "https://vimeo.com/1139332827/877cff4ed9"},
    {"url": "https://vimeo.com/1139331912/8e83f64171"},
    {"url": "https://vimeo.com/1139332444/1a1c84113c"},
    {"url": "https://vimeo.com/1139331392/5ee587949f"},
    {"url": "https://vimeo.com/1139333509"},
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
            
            # Try to grab hash from URL if present
            url_parts = v['url'].split('/')
            hash_val = url_parts[-1] if len(url_parts) > 4 and url_parts[-1][0].isalnum() else ""
            # That logic is weak, let's just print the input URL which has the hash
            
            print(f"| {v['url']} | {vid_id} | {width}x{height} | {thumb} | {title} | {width} | {height} |")
        else:
            print(f"| {v['url']} | - | - | FAILED ({response.status_code}) | - | - | - |")
    except Exception as e:
        print(f"| {v['url']} | - | - | ERROR: {e} | - | - | - |")
