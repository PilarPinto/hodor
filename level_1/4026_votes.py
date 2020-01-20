#!/usr/bin/python3
import requests
import urllib
import json
from bs4 import BeautifulSoup

url = 'http://158.69.76.135/level1.php'

response = {}
while response.get(200, 0) < 1:
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    hash_value = soup.find('input', attrs={'name': 'key'})
    str_hash_value = str(hash_value)[39:-3]
    # print(str_hash_value)
    data = {'id': '888888888', 'holdthedoor': 'submit', 'key': str_hash_value}
    header = {'content-type': 'x-www-form-urlencoded'}
    reqst = requests.post(url, data=data, headers=header)
    print(reqst.text, reqst.headers)
    reqst = reqst.status_code
    if response.get(reqst):
        response[reqst] = response[reqst] + 1
    else:
        response[reqst] = 1
    print(response)
print(response)