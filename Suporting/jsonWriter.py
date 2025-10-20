import json
def write_json(file_path,data,mode: str = 'w'):
    with open(file_path, mode=mode, encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)