from core.models import User


def create_follower(user_id: int, data: list) -> str:
    user = User.objects.get(user_id=user_id)
