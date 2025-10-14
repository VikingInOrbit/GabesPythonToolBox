import yaml
def write_yaml(file_path,data,mode: str = 'w'):
    with open(file_path,mode=mode, encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)