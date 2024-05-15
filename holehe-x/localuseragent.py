import json

with open('./agents.json', 'r') as f:
    useragents = json.loads(f.read())
