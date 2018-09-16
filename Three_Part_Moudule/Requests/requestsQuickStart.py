# coding=utf-8
import json, requests

url = 'http://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
r = requests.post(url, json=payload)

