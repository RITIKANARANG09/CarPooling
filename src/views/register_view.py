from src.model.user import User
from src.helper.validations import Validations
class Register:
    def __init__(self,auth_controller):
        self.auth_controller=auth_controller

    def user_registration(self,role):
        username=Validations.input_username()
        password = input('Enter your password : ')
        phone_number=Validations.input_number()
        email=input('Entr your email : ')
        adhaar_card_number=input()
        self.auth_controller.user_register(User(username,password,phone_number,email,role,adhaar_card_number))