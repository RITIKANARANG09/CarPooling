import uuid
class Ride:
    def __init__(self,station,date,distance,total_distance,vehicle_registration_number,time,sequence_number):
        self.ride_id= str(uuid.uuid1())
        self.station=station
        self.date=date
        self.distance=distance
        self.total_distance=total_distance
        self.vehicle_registration_number=vehicle_registration_number
        self.time=time
        self.sequence_number=sequence_number

    def price_of_ride(self,source,destination):
        return (destination-source)*10
