from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for country_code, country in COUNTRIES.items():
        if country_name.lower() == country.lower():
            return country_code
    else:
        return None
            
