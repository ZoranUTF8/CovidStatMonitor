# Import required modules
from fastapi import FastAPI
from router.countryRouter import router as country_router
from router.emailRouter import router as email_router
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()

# Mount the country router under the prefix /v1/countries and tag it as "countries"
app.include_router(country_router, prefix="/v1/countries", tags=["countries"])
app.include_router(email_router, prefix="/v1/emails",)
# Enable Cross-Origin Resource Sharing (CORS) by adding the CORSMiddleware
# This will allow requests from any origin, with any credentials, and any HTTP methods and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
