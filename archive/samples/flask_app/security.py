from werkzeug.security import safe_str_cmp
from models import UserModel

def authenticate(username, password):
    user = UserModel.get_by_name(username) #username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload["identity"]
    return UserModel.get_by_id(user_id) #userid_mapping.get(user_id, None)
