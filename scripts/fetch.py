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

mapping = {
    '112-1研究所宿舍申請': 'graduate',
    '112-1學士班學生申請校內宿舍(舊生候補)': 'undergraduate',
    '學士班新生宿舍暑假住宿申請作業': 'summer',
}

for item in data:
    key = mapping[item['name']]
    history[key]['date'].append(str(date.today()))
    history[key]['male'].append(item['male'])
    history[key]['female'].append(item['female'])

with open(history_path, 'w', encoding='utf8') as f:
    json.dump(history, f, ensure_ascii=False, indent=4)
