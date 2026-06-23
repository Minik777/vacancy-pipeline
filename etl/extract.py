import requests
import json
def get_posts(query, count=20) -> list[dict]:
    url = "https://jobicy.com/api/v2/remote-jobs"
    params = {
        'count': count,
        'tag': query
    }
    headers = {
        'User-Agent': 'vacancy-pipeline/1.0'
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return data["jobs"]


