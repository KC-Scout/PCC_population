import json

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
