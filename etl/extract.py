import requests
from config import API_URL, HEADERS

def get_posts(query, count=20) -> list[dict]:
    params = {
        'count': count,
        'tag': query
    }

    response = requests.get(API_URL, params=params, headers=HEADERS)
    data = response.json()
    return data["jobs"]


