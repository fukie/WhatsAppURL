# On Mac, run the following in Terminal first if package is missing.
# python3 -m pip install requests
import requests

def generate_country_options():
    # Get the latest country data from the REST Countries API
    url = "https://restcountries.com/v2/all?fields=name,callingCodes,alpha3Code"
    response = requests.get(url)
    data = response.json()

    # Generate the HTML options for the country dropdown
    options = ""
    for country in data:
        name = country["name"]
        code = country["callingCodes"][0]
        iso3 = country["alpha3Code"]
        #flag = chr(ord(iso3[0]) + 127397) + chr(ord(iso3[1]) + 127397) + chr(ord(iso3[2]) + 127397)  # Convert ISO code to flag emoji
        option = f'{name} (+{code})'  # Format the option text
        options += f'<option value="{iso3}">{option}</option>\n'

    return options

print( generate_country_options() )