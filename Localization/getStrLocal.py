from json import load
import locale
from pathlib import Path


def getStr(value: str) -> str:
    filename: str = checkislocalfile(lang=getlang())
    path: str = f"{Path.cwd()}/Localization/{filename}"
    with open(file=path, mode="r", encoding="UTF-8") as localization:
        data: dict = load(fp=localization)
        return data.get(value)

def getlang() -> str:
    if locale.getlocale()[0] is not None:
        systemlang: str = locale.getlocale()[0]
        return systemlang.split("_")[0]
    else:
        return ""

def checkislocalfile(lang: str) -> bool:
     filename: Path = Path(f"{lang}.json")

     if filename.exists() and filename.is_file():
          return str(filename)
     else:
          return "English.json"
