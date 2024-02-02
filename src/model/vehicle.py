import uuid

class Vehicle:
    def __init__(self,vehicle_registration_number,vehicle_brand,vehicle_name,sitting_capacity):
        self.id=str(uuid.uuid1())
        self.vehicle_registration_number=vehicle_registration_number
        self.vehicle_brand=vehicle_brand
        self.vehicle_name=vehicle_name
        self.sitting_capacity=sitting_capacity
