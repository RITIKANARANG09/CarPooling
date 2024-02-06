from src.Enum.admin_options import AdminOptions
from src.helper.message import Message
from src.Exceptions.app_decorators import loop

class Admin:
    def __init__(self,admin_controller):
        self.admin_controller=admin_controller

    @loop
    def choose(self,user):
        print(Message.adminpage)
        option=int(input(Message.input))

        if option == AdminOptions.view_users.value:
            self.view_users()
        elif option == AdminOptions.delete_user.value:
            self.delete_user(user)
        else:
            print(Message.wrong_input)

    def view_users(self):
        users=self.admin_controller.view_users()
        print(users)

    def delete_user(self,user):
        self.admin_controller.delete_user(user)

    def verify_vehicle_details(self,user):
        self.admin_controller.verify_vehicle(user)