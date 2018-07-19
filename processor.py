import sys,subprocess,shlex,os
from es_ops import create_data, get_source

def run_cmd(id):
    d = get_source(id)
    if "cmd" in d:
        a = subprocess.run(shlex.split(d["cmd"]),capture_output=True)
        b = a.stdout
    else:
        b = b''
    return b

def to_json():
    obj = {"data": "", "source_id": os.environ["ID"]}
    obj["data"] = run_cmd(obj["source_id"]).decode("utf-8")
    return obj

if __name__ == "__main__":
    if "ID" in os.environ:
        create_data(to_json())