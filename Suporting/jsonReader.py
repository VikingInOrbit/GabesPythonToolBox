import json
def read_json(file_path,**kwargs):
    with open(file_path, "r", encoding=kwargs.get("encoding", "utf-8")) as f:
            return json.load(f)