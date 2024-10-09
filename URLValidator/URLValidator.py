import requests

def isURLValid(url: str) -> bool:
    try:
        response = requests.head(url=url, allow_redirects=True, timeout=2)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        return False
