import unittest.mock as mock
import pytest
import unittest
from src.Exceptions.duplicate_error import DuplicateError
from src.Exceptions.not_found_error import NotFoundError
from src.business.auth_business import AuthBusiness
from src.business.publisher_business import PublisherBusiness
from src.business.rider_business import RiderBusiness
from src.config.query import Query
from src.model.ride import Ride
from src.model.rider_input import RiderInput
from src.model.user import User
from src.database.database import Database
from src.model.user_ride_mapping import UserRideMapping
from src.model.user_vehicle_mapping import UserVehicleMapping
from src.model.vehicle import Vehicle

class TestRiderBusiness:
    @pytest.fixture(autouse=True)
    def rider_business(self):
        self.obj = RiderBusiness(mock.MagicMock())

    def test_view_available_rides_success(self):
        rider_input=RiderInput('Depa','Dest','2024-02-02')
        self.obj.db.get_data.return_value=['1','2','s1','s2','2024-02-02','2','2','4','03:00:00','04:00:00']
        assert self.obj.view_available_rides(rider_input)
        self.obj.db.get_data.assert_called_once()

    def test_view_available_rides_failed(self):
        rider_input=RiderInput('Depa','Dest','2024-02-02')
        self.obj.db.get_data.return_value=[]
        with pytest.raises(NotFoundError):
            assert self.obj.view_available_rides(rider_input)
        self.obj.db.get_data.assert_called_once()

    def test_delete_ride_success(self):
        test_ride = UserRideMapping("testUser", "AA", "AB")
        self.obj.db.get_data.return_value=[test_ride]
        self.obj.db.delete_data.return_value=[None]
        assert self.obj.delete_ride('1')==None
        self.obj.db.get_data.assert_called_once()
        self.obj.db.delete_data.assert_called_once()

    def test_delete_ride_failed(self):
        test_ride = UserRideMapping("testUser", "AA", "AB")
        self.obj.db.get_data.return_value=[]
        self.obj.db.delete_data.return_value=[None]
        with pytest.raises(NotFoundError):
            assert self.obj.delete_ride('1')==None
        self.obj.db.get_data.assert_called_once()
        self.obj.db.delete_data.assert_not_called()

    def test_view_ride_by_ride_id_success(self):
        test_ride = UserRideMapping("testUser", "AA", "AB")
        self.obj.db.get_data.return_value = (test_ride,)
        assert self.obj.view_ride_by_id('testUser') == (test_ride,)
        self.obj.db.get_data.assert_called_once()

    def test_view_ride_by_ride_id_failed(self):
        test_ride = UserRideMapping("testUser", "AA", "AB")
        self.obj.db.get_data.return_value = None
        with pytest.raises(NotFoundError):
            assert self.obj.view_ride_by_id('testUser') == (test_ride,)
        self.obj.db.get_data.assert_called_once()

    def test_view_ride(self,mocker):
        test_ride = UserRideMapping("testUser", "AA", "AB")
        mocker.patch.object(self.obj,"view_ride_by_id",return_value=(test_ride,))
        self.obj.db.


