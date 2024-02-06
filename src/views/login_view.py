from src.Enum.role_options import RoleOptions
from src.helper.message import Message
from src.model.user import User
from src.Exceptions.app_decorators import loop
from src.helper.validations import Validations


class Login:
    def __init__(self,publisher_view,auth_controller,rider_view):
        self.publisher_view=publisher_view
        self.auth_controller=auth_controller
        self.rider_view=rider_view

    def user_login(self):
        username=Validations.input_username()
        password = input(Message.password)
        print(Message.rolepage)
        role_option=int(input(Message.input))
        user=self.auth_controller.user_login(username, password)
        self.login_options(role_option,user)

    @loop
    def login_options(self,role_option,user):
        if role_option == RoleOptions.PUBLISHER.value:
            self.publisher_view.choose(user)

        elif role_option == RoleOptions.RIDER.value:
            self.rider_view.choose(user)

        elif role_option == RoleOptions.ADMIN.value:
            self.admin_view.choose()

