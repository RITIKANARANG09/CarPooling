
from src.helper.message import Message
from .login_view import Login
from src.Enum.homepage_options import HomepageOptions
from src.Enum.role_options import RoleOptions
from .register_view import Register
class HomePage:

    def __init__(self,login,register):
        self.login=login
        self.register=register
    def start(self):
        home_page=print(Message.homepage)
        option=int(input(Message.input))

        if option == HomepageOptions.REGISTER.value:
            self.register.user_registration('User')
        elif option == HomepageOptions.LOGIN.value:
            self.login.user_login()





