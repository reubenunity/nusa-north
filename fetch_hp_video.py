import requests
import json

def get_vimeo_data(video_id, hash_val):
    # Construct URL with hash
    video_url = f"https://vimeo.com/{video_id}/{hash_val}"
    oembed_url = f"https://vimeo.com/api/oembed.json?url={video_url}"
    try:
        response = requests.get(oembed_url)
        if response.status_code == 200:
            data = response.json()
            print(f"ID: {data.get('video_id')}")
            print(f"Title: {data.get('title')}")
            print(f"Thumbnail: {data.get('thumbnail_url')}")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")

get_vimeo_data("1143266792", "307333a803")
