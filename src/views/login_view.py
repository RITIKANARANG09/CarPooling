from src.Enum.role_options import RoleOptions
from src.helper.message import Message
from src.model.user import User


class Login:
    def __init__(self,publisher_view,auth_controller,rider_view):
        self.publisher_view=publisher_view
        self.auth_controller=auth_controller
        self.rider_view=rider_view

    def user_login(self):
        username=input(Message.username)
        password = input(Message.password)
        print(Message.rolepage)
        role_option=int(input(Message.input))
        user=self.auth_controller.user_login(username, password)

        if role_option == RoleOptions.PUBLISHER.value:
            self.publisher_view.choose(user)

        elif role_option == RoleOptions.RIDER.value:
            self.rider_view.choose(user)

        elif role_option == RoleOptions.ADMIN.value:
            self.admin_view.choose()

