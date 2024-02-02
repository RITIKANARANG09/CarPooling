from src.model.user import User
class Register:
    def __init__(self,auth_controller):
        self.auth_controller=auth_controller

    def user_registration(self,role):
        username=input('Enter your name : ')
        password = input('Enter your password : ')
        phone_number=input("Enter your phone number : ")
        email=input('Entr your email : ')
        adhaar_card_number=input("Enter your adhaar card number : ")
        self.auth_controller.user_register(User(username,password,phone_number,email,role,adhaar_card_number))