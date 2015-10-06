import requests
import json


HOST = "http://apps.testinsane.com/rte%s"

def get(endpoint):
    uri = HOST % endpoint
    return requests.get(uri)

def post(endpoint, headers, payload):
    uri = HOST % endpoint
    return requests.post(uri, data=json.dumps(payload), headers=headers)
