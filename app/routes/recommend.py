"""
Recommendation APIs.
"""

from fastapi import APIRouter
from app.models import recommend_model
from app.logic import recommendation

# Initialize router
recommend_router = APIRouter(prefix="/recommend")


@recommend_router.post("/")
def recommend(req: recommend_model.Request):
    """
    POST: get recommendation
    """
    res = recommendation.recommend(req.message)
    return res()
