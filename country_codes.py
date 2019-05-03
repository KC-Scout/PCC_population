from pygal.maps.world import COUNTRIES

countries_lower = []
for k, v in COUNTRIES.items():
    countries_lower.append(v.lower())


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for country_code, country in COUNTRIES.items():
        if country_name.lower() == country.lower():
            return country_code

        elif 'congo, dem.' in country_name.lower():
            return 'cd'
        elif 'hong kong' in country_name.lower():
            return 'hk'
        elif 'macao' in country_name.lower():
            return 'mo'
        elif 'egypt' in country_name.lower():
            return 'eg'
        elif 'gambia' in country_name.lower():
            return 'gm'
        elif 'yemen' in country_name.lower():
            return 'ye'
        else:
            return None
            
