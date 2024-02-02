class AdminController:
    def __init__(self,admin_business):
        self.admin_business=admin_business

    def view_users(self):
        self.admin_business.view_users()

    def delete_user(self,user):
        self.admin_business.delete_user(user)

    def verify_vehicle(self,user):
        pass
