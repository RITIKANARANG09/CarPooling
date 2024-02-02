
class AuthController:
    def __init__(self,auth_business):
        self.auth_business=auth_business

    @
    def user_register(self, user):
        self.auth_business.add_user_to_db(user)

    def user_login(self,username,password):
        return self.auth_business.get_user_details(username,password)
