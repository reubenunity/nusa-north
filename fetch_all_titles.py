import requests

videos = [
    ("1133899956", "97ac212d90"),
    ("1133529757", "e8519ee984"),
    ("1123943736", "b2bba13bf5"),
    ("1145009419", "90bca3a2b9"),
    ("1118772124", "85090fa653"),
    ("1143266792", "307333a803"),
    ("1082754781", "6636bc5898"),
    ("1084881951", "3f2ec5e0f9"),
    ("1122744728", "c10d5281d7"),
    ("1084875985", "733ca8b56c"),
    ("1102123333", "f7f9b3e6e1")
]

for vid, h in videos:
    url = f"https://vimeo.com/api/oembed.json?url=https://vimeo.com/{vid}/{h}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print(f"{vid}: {r.json().get('title')}")
        else:
            print(f"{vid}: Error {r.status_code}")
    except:
        print(f"{vid}: Exception")
