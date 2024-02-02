class PublisherController:

    def __init__(self,publisher_business):
        self.publisher_business=publisher_business
    def publish_ride(self,ride):
        self.publisher_business.add_ride_to_db(ride)

    def view_published_ride(self,vehicle_details,date):
        return self.publisher_business.view_ride(vehicle_details,date)

    def delete_published_ride(self,username,date):
        self.publisher_business.delete_ride_from_db(username,date)

    def add_vehicle(self,vehicle,user_vehicle_mapping):
        self.publisher_business.add_vehicle_to_db(vehicle,user_vehicle_mapping)
    def view_vehicles(self,username):
        print(username)
        return self.publisher_business.view_vehicles(username)

    def delete_registered_vehicle(self,username,vehicle_name):
        self.publisher_business.delete_vehicle_from_db(username,vehicle_name)