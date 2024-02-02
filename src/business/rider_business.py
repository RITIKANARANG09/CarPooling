from src.config.query import Query
from src.Exceptions.not_found_error import NotFoundError
from src.helper.message import Message
class RiderBusiness:
    def __init__(self,db):
        self.db=db
    def view_ride(self,user):
        mapping=self.view_ride_by_id(user)
        ride_details = []
        mapping_list=mapping[0]
        mapping_list=mapping_list[2:]
        if mapping_list:
            for ride_id in mapping_list:
                ride_details.append(self.db.get_data(Query.GET_RIDE_BY_RIDE_NO, (ride_id,)))
                # print(mapping)
        ride_details.append(mapping[0][:1])
        return ride_details

    def view_ride_by_id(self,user):
        return self.db.get_data(Query.GET_USER_RIDE_MAPPING, (user,))

    def view_available_rides(self,data):
        return self.db.get_data(Query.SEARCH_RIDES,(data.departure,data.destination))

    def add_ride(self,data):
        self.db.add_data(Query.CREATE_RIDE_MAPPING,(data.id,data.rider_name,data.ride_id1,data.ride_id2))

    def delete_ride(self,ride_id):
        ride=self.db.get_data(Query.GET_RIDE_BY_RIDE_ID,(ride_id,))
        if ride:
            self.db.delete_data(Query.DELETE_RIDE_FROM_MAPPING,(ride_id,))
        else:
            raise NotFoundError(Message.not_found)