import sys

from src.helper.message import Message
from .login_view import Login
from src.Enum.homepage_options import HomepageOptions
from src.Exceptions.app_decorators import loop
class HomePage:

    def __init__(self,login,register):
        self.login=login
        self.register=register

    @loop
    def start(self):
        print(Message.homepage)
        option=int(input(Message.input))

        if option == HomepageOptions.REGISTER.value:
            self.register.user_registration('User')
        elif option == HomepageOptions.LOGIN.value:
            self.login.user_login()
        elif option == HomepageOptions.EXIT.value:
            sys.exit()
        else:
            print(Message.wrong_input)





