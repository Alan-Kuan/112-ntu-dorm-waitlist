#!/usr/bin/env python3

import json
import requests
import sys
from datetime import date

if len(sys.argv) < 2:
    exit(1)

history_path = sys.argv[1]

url = 'https://housing.ntu.edu.tw/index/get.progress.json'
res = requests.get(url)
data = res.json()

with open(history_path) as f:
    history = json.load(f)

for item in data:
    new_item = {
        'date': str(date.today()),
        'male': item['male'],
        'female': item['female']
    }
    history[item['name']].append(new_item)

with open(history_path, 'w', encoding='utf8') as f:
    json.dump(history, f, ensure_ascii=False, indent=4)
