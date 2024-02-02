import uuid


class UserVehicleMapping:
    def __init__(self,publisher_name,vehicle_registration_number):
        self.id= str(uuid.uuid1())
        self.publisher_name = publisher_name
        self.vehicle_registration_number=vehicle_registration_number
