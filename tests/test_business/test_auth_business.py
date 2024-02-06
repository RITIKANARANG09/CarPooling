import unittest.mock as mock
import pytest
import unittest
from src.Exceptions.duplicate_error import DuplicateError
from src.business.auth_business import AuthBusiness
from src.config.query import Query
from src.model.user import User
from src.database.database import Database

class TestAuthBusiness:
    @pytest.fixture(autouse=True)
    def auth_business(self):
        self.obj = AuthBusiness(mock.MagicMock())

    def test_add_user_to_db_failed(self):
        test_user = User("test123","Test@123","1234567890","test@email.com","user","123412341234")
        self.obj.db.get_data.return_value = [("test123","Test@123","1234567890","test@email.com","user","123412341234")]
        self.obj.db.add_data.return_value = None

        with pytest.raises(DuplicateError):
            self.obj.add_user_to_db(test_user)
        self.obj.db.get_data.assert_called_once()
        self.obj.db.add_data.assert_not_called()

    def test_add_user_to_db_success(self):
        test_user = User("test123","Test@123","1234567890","test@email.com","user","123412341234")
        self.obj.db.get_data.return_value = [("test12","Test@123","1234567890","test@email.com","user","123412341234")]
        self.obj.db.add_data.return_value = None


        assert self.obj.add_user_to_db(test_user) == None
        self.obj.db.get_data.assert_called_once()
        self.obj.db.add_data.assert_called_once()

    def test_get_user_details(self):

        test_username="test12"
        test_password="Test@123"
        self.obj.db.get_data.return_value = [("test12","Test@123","1234567890","test@email.com","user","123412341234")]
        assert self.obj.get_user_details(test_username,test_password) == [("test12","Test@123","1234567890","test@email.com","user","123412341234")]
        self.obj.db.get_data.assert_called_once()

