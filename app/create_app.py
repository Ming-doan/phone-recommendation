"""
Creator function for FastAPI app. Fixing circular imports.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    """
    Create app for FastAPI.
    """
    app = FastAPI()

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
