import requests
from pathlib import Path

def isURLValid(url: str) -> bool:
    try:
        response = requests.head(url=url, allow_redirects=True, timeout=2)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        return False

def checkFolder(path: str) -> None:
    folderPath = Path(path)
    if not folderPath.exists():
        folderPath.mkdir(parents=True, exist_ok=True)
