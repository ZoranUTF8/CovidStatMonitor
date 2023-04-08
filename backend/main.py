from fastapi import FastAPI
from router.country import router as country_router


app = FastAPI()
# Mount the router in the app
app.include_router(country_router, prefix="/v1/countries", tags=["countries"])
