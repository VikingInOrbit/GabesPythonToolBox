import yaml
def read_ymal(file_path,**kwargs):
    with open(file_path, "r", encoding=kwargs.get("encoding", "utf-8")) as f:
            return yaml.safe_load(f)