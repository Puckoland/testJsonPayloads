#!/usr/bin/env python

import json
import os
import requests

URL = "http://78.128.250.22/"

def parse_json(json_path):
    with open(json_path) as f:
      return json.load(f)

def send_requests(jsondata):
    for req in jsondata:
        method = req['method']
        url = URL + req['api_endpoint']
        data = req['data']
        
        if method == 'GET':
            resp = requests.get(url, json=data)
        elif method == 'POST':
            resp = requests.post(url, json=data)
        else:
            print("You fucked up! Unknown method:", method)
        
        if resp.status_code == 200:
            print("Got a response: {}".format(json.loads(resp.content)))
        else:
            print("Error: Could not get server's public key.")


if __name__ == '__main__':
    jsondata = parse_json('payloads.json')
    send_requests(jsondata)
