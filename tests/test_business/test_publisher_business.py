import unittest.mock as mock
import pytest
import unittest
from src.Exceptions.duplicate_error import DuplicateError
from src.Exceptions.not_found_error import NotFoundError
from src.business.auth_business import AuthBusiness
from src.business.publisher_business import PublisherBusiness
from src.config.query import Query
from src.model.ride import Ride
from src.model.user import User
from src.database.database import Database
from src.model.user_vehicle_mapping import UserVehicleMapping
from src.model.vehicle import Vehicle


class TestPublisherBusiness:
    @pytest.fixture(autouse=True)
    def publisher_business(self):
        self.obj = PublisherBusiness(mock.MagicMock())

    def test_add_ride_to_db_success(self):
        test_ride = Ride("station1","2024-02-02","0","0","94","12:00:00",1)
        self.obj.db.get_data.return_value = []
        self.obj.db.add_data.return_value = None
        assert self.obj.add_ride_to_db(test_ride)==None
        self.obj.db.get_data.assert_called_once()
        self.obj.db.add_data.assert_called_once()

    def test_add_ride_to_db_failed(self):
        test_ride = Ride("station1", "2024-02-02", "0", "0", "94", "12:00:00", 1)
        self.obj.db.get_data.return_value = [("station1", "2024-02-02","12:00:00")]
        self.obj.db.add_data.return_value = None
        with pytest.raises(DuplicateError):
            assert self.obj.add_ride_to_db(test_ride)
        self.obj.db.get_data.assert_called_once()
        self.obj.db.add_data.assert_not_called()


    def test_view_ride_from_db_success(self):
        test_vehicle_registration_id="1234"
        test_date="2024-02-02"
        test_ride=Ride("station1", "2024-02-02", "0", "0", "94", "12:00:00", 1)
        self.obj.db.get_data.return_value = [("station1", "2024-02-02", "0", "0", "94", "12:00:00", 1)]
        assert self.obj.view_ride(test_vehicle_registration_id,test_date)
    def test_add_vehicle_to_db_success(self):
        test_vehicle=Vehicle('2','test','test@12',2)
        test_user_vehicle_mapping=UserVehicleMapping('TestUser','2')
        self.obj.db.get_data.return_value=['1','3']
        self.obj.db.add_data.side_effects = [None,None]
        assert self.obj.add_vehicle_to_db(test_vehicle,test_user_vehicle_mapping)==None
        assert  self.obj.db.add_data.call_count, 2

    def test_add_vehicle_to_db_failed(self):
        test_vehicle=Vehicle('1','test','test@12',2)
        test_user_vehicle_mapping=UserVehicleMapping('TestUser','1')
        self.obj.db.get_data.return_value = ['1', '2']
        self.obj.db.add_data.side_effects = [None,None]
        with pytest.raises(DuplicateError):
            assert self.obj.add_vehicle_to_db(test_vehicle,test_user_vehicle_mapping)
        self.obj.db.get_data.assert_called_once()
        self.obj.db.add_data.assert_not_called()

    def test_view_vehicles(self):
        user = 'John Doe'
        mapping_data = [('ABC123',)]
        vehicle_data = [('ABC123', 'Toyota', 'Camry', 4)]

        self.obj.db.get_data.side_effect = [mapping_data, vehicle_data[0]]

        assert self.obj.view_vehicles(user) == vehicle_data
        # Assert the result
        assert self.obj.db.get_data.call_count, 2


    def test_view_vehicles_not_found(self):
        # Mock data
        user = 'Jane Doe'

        # Mock database response
        self.obj.db.get_data.side_effect = [None,None] # Simulate that no vehicles are found for the user

        # Perform the test
        with pytest.raises(NotFoundError):
            assert self.obj.view_vehicles(user)

        # Assert that the database method was called with the expected arguments
        assert self.obj.db.get_data.call_count,2

    def test_delete_ride_from_db_success(self):
            # test_ride = Ride("station1", "2024-02-02", "0", "0", "94", "12:00:00", 1)
            self.obj.db.get_data.return_value=[('station1','2024-03-03','03:00:00')]
            self.obj.db.delete_data.side_effect=[None,None]
            assert self.obj.delete_ride_from_db('R','1')==None
            assert self.obj.db.delete_data.call_count,2
            self.obj.db.get_data.assert_called_once()

    def test_delete_ride_from_db_failed(self):
            # test_ride = Ride("station1", "2024-02-02", "0", "0", "94", "12:00:00", 1)
            self.obj.db.get_data.return_value=[]
            # self.obj.db.delete_data.side_effect=[None,None]
            with pytest.raises(NotFoundError):
                assert self.obj.delete_ride_from_db('R','1')
            self.obj.db.delete_data.assert_not_called()
            self.obj.db.get_data.assert_called_once()

    def test_delete_vehicle_from_db_success(self):
            user = 'John Doe'
            mapping_data = [('ABC123',)]
            vehicle_data = [('ABC123', 'Toyota', 'Camry', 4)]
            self.obj.db.get_data.return_value=[vehicle_data]
            self.obj.db.delete_data.side_effect=[None,None]
            assert self.obj.delete_vehicle_from_db(user,'Camry')==None
            assert self.obj.db.delete_data.call_count,2
            self.obj.db.get_data.assert_called_once()

    def test_delete_vehicle_from_db_failed(self):
            user = 'John Doe'
            mapping_data = [('ABC123',)]
            vehicle_data = []
            self.obj.db.get_data.return_value=[]
            # self.obj.db.delete_data.side_effect=[None,None]
            with pytest.raises(NotFoundError):
                assert self.obj.delete_vehicle_from_db(user,'A')
            self.obj.db.delete_data.assert_not_called()
            self.obj.db.get_data.assert_called_once()
