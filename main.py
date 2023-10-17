"""
Main file for the project. Run this file to start the program.
"""

from app.create_app import create_app
from app.routes import router


# Create app
app = create_app()

# Register api routes
app.include_router(router)


@app.get("/")
def welcome():
    """
    Welcome message for the API.
    """
    return {"message": "Welcome to the Phone Recommendation API!"}
