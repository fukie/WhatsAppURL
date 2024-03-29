# On Mac, run the following in Terminal first if package is missing.
# python3 -m pip install requests
import requests

def generate_country_prefixes():
    # Get the latest country data from the REST Countries API
    # url = "https://restcountries.com/v2/all?fields=name,callingCodes,alpha3Code"
    url = "https://restcountries.com/v2/all?fields=name,callingCodes,alpha2Code"
    response = requests.get(url)
    data = response.json()

    # Generate the HTML options for the country dropdown
    options = ""
    for country in data:
        code = country["callingCodes"][0]
        #iso = country["alpha3Code"]
        iso = country["alpha2Code"]
        #flag = chr(ord(iso3[0]) + 127397) + chr(ord(iso3[1]) + 127397) + chr(ord(iso3[2]) + 127397)  # Convert ISO code to flag emoji
        options += f"'{iso}': '{code}',\n"  # Format the option text

    options = options[:-2] # Remove the last newline and comma
    return options

print( generate_country_prefixes() )