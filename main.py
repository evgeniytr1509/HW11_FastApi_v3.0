from fastapi import FastAPI
from routes.contacts import router as notes_router


app = FastAPI()

app.include_router(notes_router, prefix="/contacts", tags=["contacts"])
