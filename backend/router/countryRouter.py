# Importing required modules
from fastapi import APIRouter, HTTPException
import requests
# Importing controllers and requests module
from controllers.CountryController import CountryController


# Create an instance of the APIRouter class
router = APIRouter()

# Define the routes in the router instance:

# World statistics
@router.get("/world")
def get_all_countries():
    return {"message": "Success", "data": CountryController.get_all_countries_data()}

# Single country statistics
@router.get("/")
@router.get("/{country_name}")
def get_single_country(country_name: str = None):
    # If no country name provided than raise exception
    if country_name is None:
        error_message = "Country name parameter is empty or missing"
        raise HTTPException(status_code=400, detail=error_message)
    try:
        return {"message": "Success", "data": CountryController.get_single_country_data(country_name)}
    except requests.exceptions.RequestException as e:
        error_message = f"Error accessing the covid-19.dataflowkit.com API, Reason: {e}"
        raise HTTPException(status_code=500, detail=error_message)


# Export the router instance:
__all__ = ["router"]
