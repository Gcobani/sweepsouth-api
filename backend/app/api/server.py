from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.db import config
from app.services import handlers

def get_application():
    app = FastAPI(title="sweepsouth", version="1.0.0")
    app.add_event_handler("startup", handlers.create_start_app_handler(app))
    app.add_event_handler("shutdown", handlers.create_stop_app_handler(app))
    app.include_router(api_router, prefix="/api")
    return app
app = get_application()