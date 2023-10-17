"""
Recommendation logics for APIs.
"""

from app.models import recommend_model


def recommend(message: str):
    """
    Recommendation main logic.
    """
    print(message)
    return recommend_model.Response(
        message="Đây là một số điện thoại phù hợp vói nhu cầu của bạn",
        recommends=["https://fptshop.com.vn/dien-thoai/iphone-15-pro-max",
                    "https://fptshop.com.vn/dien-thoai/samsung-galaxy-s23-ultra"]
    )
