import requests
import json

videos = [
    "https://vimeo.com/1133899956/97ac212d90",
    "https://vimeo.com/1133529757/e8519ee984",
    "https://vimeo.com/1123943736/b2bba13bf5",
    "https://vimeo.com/1122744728/c10d5281d7",
    "https://vimeo.com/1118772124/85090fa653",
    "https://vimeo.com/1116517915/07cbb39ccc",
    "https://vimeo.com/1102123333/f7f9b3e6e1",
    "https://vimeo.com/1082754781/6636bc5898",
    "https://vimeo.com/1084881951/3f2ec5e0f9",
    "https://vimeo.com/1084885516/2d1d16fadb",
    "https://vimeo.com/1084883669/83cc6d80ca",
    "https://vimeo.com/1084875985/733ca8b56c",
    "https://vimeo.com/1084877907/7105a166d7"
]

print("| URL | Title | Thumbnail | Upload Date |")
print("|---|---|---|---|")

for v_url in videos:
    try:
        # Clean URL parameters for oEmbed
        clean_url = v_url.split('?')[0]
        api_url = f"https://vimeo.com/api/oembed.json?url={clean_url}"
        
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            title = data.get('title', 'Unknown')
            thumb = data.get('thumbnail_url', '')
            date = data.get('upload_date', '') # oEmbed might not verify date, but we check what we get
            
            print(f"| {clean_url} | {title} | {thumb} | {date} |")
        else:
            print(f"| {v_url} | FAILED ({response.status_code}) | - | - |")
    except Exception as e:
        print(f"| {v_url} | ERROR: {e} | - | - |")
