import uuid


class UserRideMapping:
    def __init__(self,rider_name,ride_id1,ride_id2):
        self.id= str(uuid.uuid1())
        self.rider_name=rider_name
        self.ride_id1=ride_id1
        self.ride_id2=ride_id2