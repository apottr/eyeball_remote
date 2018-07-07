import requests,os,json

if "ES_SERVICE_SERVICE_HOST" in os.environ:
    ESHOST = os.environ["ES_SERVICE_SERVICE_HOST"]
    ESPORT = os.environ["ES_SERVICE_SERVICE_PORT"]
    es = f"{ESHOST}:{ESPORT}"
else:
    es = "localhost:8001/api/v1/namespaces/default/services/es-service/proxy"

esurl = lambda x: f"http://{es}{x}"

def guarantee_index_exists(idx):
    r = requests.get(esurl(f"/{idx}"))
    d = r.json()
    if "error" in d:
        requests.put(esurl(f"/{idx}"))

def get_x(r,field):
    j = r.json()
    o = []
    for item in j["hits"]["hits"]:
        obj = {"id": item["_id"]}
        if isinstance(field,list):
            for fi in field:
                obj[fi] = item["_source"][fi]
        else:
            obj[field] = item["_source"][field]
        o.append(obj)
    return o

def get_sources_for_region(region):
    r = requests.get(esurl("/sources/_search"),headers={
        "Content-Type": "application/json"
    },data=json.dumps({
        "query": {
            "bool": {
                "must": [
                    { "term": {"region": region} }
                ]
            }
        }
    }))
    return get_x(r,"cmd")

def get_jobs():
    r = requests.get(esurl("/jobs/_search"),headers={
        "Content-Type": "application/json"
    })
    return get_x(r,["name","sources"])

def get_sources():
    r = requests.get(esurl("/sources/_search"),headers={
        "Content-Type": "application/json"
    })
    return get_x(r,"cmd")

def db_init():
    guarantee_index_exists("config")