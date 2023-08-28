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

# it seemed like it won't get updated, so I decided to ignore it
ignored_groups = [
    '學士班新生宿舍暑假住宿申請作業',
];

try:
    with open(history_path) as f:
        history = json.load(f)
except:
    history = {}

today = str(date.today())

for item in data:
    key = item['name']
    if key in ignored_groups:
        continue

    if key in history:
        group = history[key]
        group['date'].append(today)
        group['male'].append(item['male'])
        group['female'].append(item['female'])
    else:
        history[key] = {
            'date': [today],
            'male': [item['male']],
            'female': [item['female']],
        }

data = {
    'history': history,
    'last_saved_date': today,
}

with open(history_path, 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
