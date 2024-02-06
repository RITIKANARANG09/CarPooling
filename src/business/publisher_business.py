from src.Exceptions.duplicate_error import DuplicateError
from src.config.query import Query
from src.Exceptions.not_found_error import NotFoundError
from src.helper.message import Message
class PublisherBusiness:
    def __init__(self,db):
        self.db=db

    def add_ride_to_db(self,ride):
        rides=self.db.get_data(Query.GET_RIDE_BY_RIDE_NO, (ride.ride_id,))

        if rides:
            raise DuplicateError(Message.ride_exists_already)
        self.db.add_data(Query.CREATE_RIDE,(ride.ride_id, ride.station,ride.date,ride.distance, ride.total_distance,
                                            ride.vehicle_registration_number,ride.time,ride.sequence_number))

    def view_ride(self,vehicle,date):

        mapping = self.db.get_data(Query.GET_RIDE_DETAILS_FROM_RIDE_TABLE, (vehicle,date))
        print(mapping)
        ride_details = []
        if mapping:
            for ride_id in mapping:
                print(ride_id[0])
                ride_details.append(self.db.get_data(Query.GET_RIDE_BY_RIDE_NO, (ride_id[0],)))
                print(ride_details)
        else:
            raise NotFoundError(Message.not_found)
        return ride_details


    def add_vehicle_to_db(self,vehicle,user_vehicle_mapping):
        vehicle_exists=self.db.get_data(Query.GET_USER_VEHICLE_MAPPING,(user_vehicle_mapping.publisher_name))
        if user_vehicle_mapping.vehicle_registration_number in vehicle_exists:
            raise DuplicateError(Message.ride_exists_already)
        self.db.add_data(Query.CREATE_VEHICLE,((vehicle.vehicle_registration_number,vehicle.vehicle_brand,vehicle.vehicle_name,vehicle.sitting_capacity)))
        self.db.add_data(Query.CREATE_VEHICLE_MAPPING,((user_vehicle_mapping.id,user_vehicle_mapping.publisher_name,user_vehicle_mapping.vehicle_registration_number)))

    def view_vehicles(self,user):
        publisher_name=user
        mapping= self.db.get_data(Query.GET_USER_VEHICLE_MAPPING, (publisher_name,))
        print(mapping)
        vehicle_details=[]
        if mapping:
            for vehicle_id in mapping:
                vehicle_details.append(self.db.get_data(Query.GET_VEHICLE_BY_REGISTRATION_NO,(vehicle_id[0],)))
        else:
            raise NotFoundError(Message.not_found)
        return vehicle_details

    def delete_ride_from_db(self,username,ride_id):
        ride=self.db.get_data(Query.GET_RIDE_BY_RIDE_NO,(ride_id,))
        # print(ride)
        if ride:
            self.db.delete_data(Query.DELETE_RIDE_FROM_MAPPING,(ride_id,))
            self.db.delete_data(Query.DELETE_RIDE_FROM_RIDE, (ride[0][0],))
        else:
            raise NotFoundError(Message.not_found)

    def delete_vehicle_from_db(self,username,vehicle_name):
        vehicle=self.db.get_data(Query.GET_VEHICLE,(vehicle_name,))
        # print(vehicle)
        # print(vehicle[0][2])
        if vehicle:
            self.db.delete_data(Query.DELETE_VEHICLE,(username,vehicle_name))
            self.db.delete_data(Query.DELETE_VEHICLE_FROM_VEHICLE, (vehicle[0][0],))
        else:
            raise NotFoundError(Message.not_found)

