import hashlib
from src.helper.exception_handler_decorator import errorhandler

class AuthController:
    def __init__(self,auth_business):
        self.auth_business=auth_business

    @errorhandler
    def user_register(self, user):
        self.auth_business.add_user_to_db(user)

    def user_login(self,username,password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.auth_business.get_user_details(username,hashed_password)
