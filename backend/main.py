from fastapi import FastAPI
from router.country import router as country_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Mount the router in the app
app.include_router(country_router, prefix="/v1/countries", tags=["countries"])


# START uvicorn main:app --reload
