"""
Recommend Request and Response Model
"""

from pydantic import BaseModel


class Request(BaseModel):
    """
    Request model for Recommend
    """
    message: str


class Response:
    """
    Response model for Recommend
    """

    def __init__(self, message: str, recommends: list[str]):
        self.message = message
        self.recommends = recommends

    def __call__(self) -> dict:
        return {"message": self.message, "recommends": self.recommends}
