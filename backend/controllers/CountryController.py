import requests


# separate module to encapsulate all the logic related to communicating with the COVID-19 API. This module can contain functions for getting data for a specific country or getting data for all countries,
# Custom CountryController class which handles the api communication
class CountryController:
    # Base url of our serving API
    BASE_URL = "https://covid-19.dataflowkit.com/v1"

# Static method to get all data for the world
    @staticmethod
    def get_all_countries_data():
        url = f"{CountryController.BASE_URL}/world"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

# Static method to get data for a specific country
    @staticmethod
    def get_single_country_data(country_name: str):
        url = f"{CountryController.BASE_URL}/{country_name}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()