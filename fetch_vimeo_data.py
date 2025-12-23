import requests
import json

videos = [
    {"id": "1133899956", "hash": "97ac212d90"},
    {"id": "1133529757", "hash": "e8519ee984"},
    {"id": "1123943736", "hash": "b2bba13bf5"},
    {"id": "1145009419", "hash": "90bca3a2b9"},
    {"id": "1118772124", "hash": "85090fa653"},
    {"id": "1082754781", "hash": "6636bc5898"},
    {"id": "1084881951", "hash": "3f2ec5e0f9"},
    {"id": "1122744728", "hash": "c10d5281d7"},
    {"id": "1084875985", "hash": "733ca8b56c"},
    {"id": "1102123333", "hash": "f7f9b3e6e1"},
    {"id": "239826119", "hash": ""} # User profile/album? "https://vimeo.com/user239826119/2" seems wrong format for video, checking.
    # The last link provided: https://vimeo.com/user239826119/2?fl=ip&fe=ec -> likely a specific video ID hidden in redirect or profile. 
    # Wait, fetching "2" as ID is unlikely. Let's skip the last weird one or try to fetch it if it was a typo.
]

print("| ID | Hash | Thumbnail URL | Title |")
print("|---|---|---|---|")

for v in videos:
    try:
        if v["hash"]:
            url = f"https://vimeo.com/api/oembed.json?url=https://vimeo.com/{v['id']}/{v['hash']}"
        else:
             url = f"https://vimeo.com/api/oembed.json?url=https://vimeo.com/{v['id']}"
             
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"| {v['id']} | {v['hash']} | {data['thumbnail_url']} | {data['title']} |")
        else:
            print(f"| {v['id']} | {v['hash']} | FAILED ({response.status_code}) | - |")
    except Exception as e:
        print(f"| {v['id']} | {v['hash']} | ERROR: {e} | - |")
