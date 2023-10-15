"""
Main file for the project. Run this file to start the program.
"""

from app.create_app import create_app


# Create app
app = create_app()


@app.get("/")
def welcome_message():
    """
    Welcome message for the API.
    """
    return {"message": "Welcome to the Phone Recommendation API!"}
