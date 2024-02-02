from src.config.query import Query
from src.helper.message import Message
from src.Exceptions.duplicate_error import DuplicateError
class AuthBusiness:

    def __init__(self,db):
        self.db=db
    def add_user_to_db(self,user):

        get_all_users = self.db.get_data(Query.GET_ALL_USERS)
        user_with_same_username = [user for user in get_all_users if user[0] == user.username]
        if len(user_with_same_username) > 0:
            raise DuplicateError(Message.user_exists_already)
        self.db.add_data(
            Query.CREATE_USER,
            (user.username,user.password,user.phone_number,user.password,user.role,user.adhaar_card_number))

    def get_user_details(self, username,password):
        return self.db.get_data(
                Query.GET_USER_CREDENTIALS,
                (username,password))
