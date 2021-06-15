import json
import requests
import time

def get_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer <INSERT PAT>"
    }


def print_json(js):
    print(json.dumps(js, indent=3))

def construct_request(r):
    tpl = f"http://18.118.116.231:3005/v4/{r}"
    return tpl

def get(url):
    r = requests.get(url, headers=get_headers(),verify=False)
    print(f"Status code: {r.status_code}")
    return r.json()

def get_request(url):
    r = requests.get(url, headers=get_headers(),verify=False)
    return (r.status_code, r.json())

def get_content(url):
    r = requests.get(url, headers=get_headers(),verify=False)
    return r.content

def raw_post(url):
    print(f"POST URL :: {url}")
    r = requests.post(url, headers=get_headers(),verify=False)
    return r.json()

def post(url, headers, data):
    r = requests.post(url, headers=get_headers(),verify=False,json=data)
    return r.json()

def get_flow(id):
    url = construct_request(f"flows/{id}/inputs")
    #url = construct_request(f"flows/{id}")
    return get(url)

def list_datasets():
    url = construct_request(f"datasetLibrary?datasetsFilter=all")
    return get(url)

def list_datasets_by_flow(id):
    url = construct_request(f"datasetLibrary?datasetsFilter=all&datasourceFlowId={id}")
    return get(url)

def list_flows():
    url = construct_request("flows")
    return get(url)

def list_datasets():
    url = construct_request("wrangledDatasets")
    return get(url)

def list_plans():
    url = construct_request("plans")
    return get(url)

def list_deployments():
    url = construct_request("deployments")
    res = get(url)
    print(res)
    return res

def deployment_by_name(name):
    deps = list_deployments()
    return next((dep for dep in deps["data"] if dep["name"] == name), None)

def export_plan(id):
    url = construct_request(f"plans/{id}/package")
    res = get(url)
    print(res)
    return

def export_flow(id):
    url = construct_request(f"flows/{id}/package")
    res = get_content(url)
    open('save.zip', 'wb').write(res)
    return

def create_deployment(name, pkg):
    # Check if deployment exists
    url = construct_request(f"deployments/{name}")
    dep = deployment_by_name(name)

    deployment_id = None

    if dep is not None:
        print("Deployment exists")
        print(f"--> {dep}")
        deployment_id = dep["id"]
    else:
        print("Deployment does not exist")
        url = construct_request(f"deployments")
        data = { "name": name }
        res = post(url, get_headers(), data)
        print(f"--> {res}")
        deployment_id = res["id"]

    print(f"Deployment id is {deployment_id}")
    url = construct_request(f"deployments/{deployment_id}/releases")
    headers = {
        "Content-Type": "multipart/form-data"
    }

    data = {
        "data": "@save.zip"
    }

    print(url)
    res = requests.post(url, headers={**get_headers(), **headers}, json=data, verify=False)
    print(res.status_code)
    print(res.content)

def run_flow(id):
    url = construct_request(f"flows/{id}/run")
    res = raw_post(url)
    return res

def get_flow_runs(id):
    url = construct_request(f"flowRuns/{id}")
    res = get(url)
    return res

def get_flow_status(id):
    # Complete, Cancelled, Created, Failed, Pending
    url = construct_request(f"flowRuns/{id}/status")
    res = get(url)
    return res

if __name__ == '__main__':
    print("--- Flows")
    flows = list_flows()
    print_json(flows)
    for flow in flows["data"]:
        name = flow["name"]
        print(f"{name} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print_json(get_flow(flow["id"]))
        #print_json(list_datasets_by_flow(flow["id"]))
        #print("****************************************")

    print(" Wranlged Datasets ****")
    #print_json(list_datasets())

    myflow = 3
    print("--- Export Flow")
    export_flow(myflow)

    print("Running flow")
    res = run_flow(myflow)
    print_json(res)

    flow_id = res["data"][0]["flowRun"]["id"]
    while True:
        print(f"Looking for {flow_id}")
        res2 = get_flow_status(flow_id)
        print(res2)
        if res2 == "Complete":
            print("Job Complete")
            break

        time.sleep(5)

#print("Deployments")
#print_json(list_deployments())

