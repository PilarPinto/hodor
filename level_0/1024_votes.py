#!/usr/bin/python3
import requests
data = {'id': 1101, 'holdthedoor': 0}
url = 'http://158.69.76.135/level0.php'
response = []
for ind in range(1024):
    response.append(requests.post(url, data))
print(response)
print(set(response))
