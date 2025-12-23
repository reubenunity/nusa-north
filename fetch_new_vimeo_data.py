import requests
import json

# HP and the other user link
videos = [
    {"url": "https://vimeo.com/1143266792/307333a803"}, # HP
    {"url": "https://vimeo.com/user239826119/2"}        # User link
]

print("| URL | ID | Hash | Thumbnail URL | Title |")
print("|---|---|---|---|---|")

for v in videos:
    try:
        url = f"https://vimeo.com/api/oembed.json?url={v['url']}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extract ID from video_id field
            vid_id = data.get('video_id')
            # Hash isn't always in oembed, but we have it in URL for HP. For the second one, we might need to assume it's public or extract from data.
            # Actually oEmbed usually returns the public URL.
            # If the input URL had a hash, we preserve it.
            
            # Try to parse ID/Hash from local URL if oEmbed doesn't give hash
            # But for the output, we need what the player needs.
            # Start with provided URL parts
            input_url = v['url']
            
            print(f"| {input_url} | {vid_id} | (Manual Check) | {data['thumbnail_url']} | {data['title']} |")
        else:
            print(f"| {v['url']} | - | - | FAILED ({response.status_code}) | - |")
    except Exception as e:
        print(f"| {v['url']} | - | - | ERROR: {e} | - |")
