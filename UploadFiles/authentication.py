from database import create_user, get_user
from hasher import verify_input


def register(user):
    user_id = create_user(user)
    return True if user_id else False
        
        
def authenticate(user):
    user_database = get_user(user['username'])
    
    if user_database and verify_input(user['password'], user_database[2]):
        return True, user_database[0]
    else:
        return False, None


def change_password(username, password, repeated_password):
    return True


