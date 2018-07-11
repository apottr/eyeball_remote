import sys 
from es_ops import create_data

def to_json(stdin):
    obj = {"data": "", "source_id": sys.argv[1]}
    obj["data"] = "".join(list(stdin))
    return obj

if __name__ == "__main__":
    create_data(to_json(sys.stdin.readlines()))