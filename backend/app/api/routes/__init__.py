from fastapi import APIRouter
from app.api.routes.default import router as default_router
router = APIRouter()
router.include_router(default_router)