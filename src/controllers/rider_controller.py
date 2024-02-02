class RiderController:
    def __init__(self,rider_business):
        self.rider_business=rider_business
    def view_booked_ride(self,user):
        return self.rider_business.view_ride(user)

    def view_available_rides(self,data):
        return self.rider_business.view_available_rides(data)

    def book_ride(self,data):
        return self.rider_business.add_ride(data)

    def delete_booked_ride(self,ride_id):
        self.rider_business.delete_ride(ride_id)