import json
import pygal.maps.world
from country_codes import get_country_code
from pygal.style import RotateStyle

no_code_list = []
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
# Build a dictionary of country data
no_code = []
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            if population < 10000000:
                cc_pops_1[code] = population
            elif population < 1000000000:
                cc_pops_2[code] = population
            else:
                cc_pops_3[code] = population
        else:
            no_code_list.append(country_name)
            
with open('no_code_list.json', 'w') as f:
    json.dump(no_code_list, f)
    
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699')  

wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010 by Country'
wm.add('Less than 10 Million', cc_pops_1)
wm.add('Between 10 Mil & 1 Billion', cc_pops_2)
wm.add('More than 1 Billion', cc_pops_3)
wm.render_to_file('world_populations_2010.svg')
            
        
