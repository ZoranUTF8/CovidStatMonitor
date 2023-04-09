# Import required modules
from fastapi import FastAPI
from router.country import router as country_router
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()

# Mount the country router under the prefix /v1/countries and tag it as "countries"
app.include_router(country_router, prefix="/v1/countries", tags=["countries"])

# Enable Cross-Origin Resource Sharing (CORS) by adding the CORSMiddleware
# This will allow requests from any origin, with any credentials, and any HTTP methods and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# START uvicorn main:app --reload
