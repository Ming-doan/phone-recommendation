"""
Base routes for the application.
"""

from fastapi import APIRouter
from .recommend import recommend_router

# Create base router
router = APIRouter(prefix="/api")

# Register child routers
router.include_router(recommend_router)
