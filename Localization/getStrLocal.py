from json import load

def getStr(file_path: str, value: str) -> str:
    with open(file=file_path, mode="r", encoding="UTF-8") as localization:
        data: dict = load(fp=localization)
        return data.get(value)
