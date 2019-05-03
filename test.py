import json
from pygal.maps.world import COUNTRIES

reader_lower = [] 
with open('no_code_list.json') as f:
    reader = json.load(f)
    
    
for i in reader:
    reader_lower.append(i.lower())
    
print(reader_lower)
    
countries_lower = []
for k, v in COUNTRIES.items():
    countries_lower.append(v.lower())
    
for x in countries_lower:
    for i in reader_lower:
        if x in i:
            print(x)
    
     
