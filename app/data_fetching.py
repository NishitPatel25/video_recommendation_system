import requests
from app.models import Video

API_BASE = "https://api.socialverseapp.com"
HEADERS = {"Flic-Token": "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"}

def fetch_data(url, headers=None, page_size=1000):
    data = []
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={"page": page, "page_size": page_size})
        if response.status_code != 200:
            break
        page_data = response.json()
        data.extend(page_data.get("posts", []))
        
        if len(page_data.get("posts", [])) < page_size:
            break
        page += 1
    return data

def fetch_all_videos():
    url = f"{API_BASE}/posts/summary/get"
    return fetch_data(url, headers=HEADERS)

def get_user_posts(username):
    return fetch_data(f"{API_BASE}/posts/view?page=1&page_size=1000", headers=HEADERS)
