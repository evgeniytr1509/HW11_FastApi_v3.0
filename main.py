from fastapi import FastAPI
from src.routes.notes import router as notes_router
from src.routes.tags import router as tags_router

app = FastAPI()

app.include_router(notes_router, prefix="/notes", tags=["notes"])
app.include_router(tags_router, prefix="/tags", tags=["tags"])