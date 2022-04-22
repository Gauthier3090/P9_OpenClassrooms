from django.contrib.auth import get_user_model
from following.models import Follower
from core.models import User

def username_exists(username) -> bool:
    User = get_user_model()
    if User.objects.filter(username=username).exists():
        return True
    return False

def createFollower(followed_user: str, user_id: int) -> str:
    try:
        follower = User.objects.get(username=followed_user)
        Follower.objects.get(followed_user_id=follower.id, user_id=user_id)
        return "La personne est déjà dans vos abonnements !"
    except Exception:
        if follower.id != user_id:
            Follower.objects.create(followed_user_id=follower.id, user_id=user_id)
            return "La personne a été rajoutée à vos abonnements !"
        else:
            return "Vous ne pouvez pas vous abonner à vous même !"
