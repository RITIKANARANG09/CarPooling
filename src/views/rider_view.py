from src.Enum.rider_options import RiderOptions
from src.helper.message import Message
from src.model.rider_input import RiderInput
from src.model.user_ride_mapping import UserRideMapping


class Rider:
    def __init__(self, rider_controller,publisher_controller):
        self.rider_controller = rider_controller
        self.publisher_controller=publisher_controller

    def choose(self, user):
        print(Message.riderpage)
        option = int(input(Message.input))

        if option == RiderOptions.book_ride.value:
            self.book_ride(user)
        elif option == RiderOptions.view_booked_ride.value:
            self.view_booked_ride(user)
        elif option == RiderOptions.delete_booked_ride.value:
            self.delete_booked_ride(user)


    def book_ride(self,user):
        available_rides=self.view_available_rides()
        choose_ride=input(Message.choose_ride_to_book)
        if int(choose_ride)>len(available_rides):
            print(Message.input_valid_number)
        else:
            ride=UserRideMapping(user[0][0],available_rides[int(choose_ride)-1][0],
                                            available_rides[int(choose_ride)-1][1])
            self.rider_controller.book_ride(ride)
            print(Message.ride_booked_successfully)

    def view_available_rides(self):
        departure = input(Message.departure)
        destination = input(Message.destination)
        date = input(Message.date)
        rider_input = RiderInput(departure, destination, date)
        available_rides = self.rider_controller.view_available_rides(rider_input)
        return (available_rides)

    def view_booked_ride(self,user):
        rides=self.rider_controller.view_booked_ride(user[0][0])
        if rides:
            pass
            print(Message.published_ride)
            print(rides[:2])
        else:
            print(Message.no_published_rides)

    # def print_rides(self,rides):
    #     for ride in rides[0][0]:
    #         print(ride[0][0])

    def delete_booked_ride(self, user):

        ride = self.rider_controller.view_booked_ride(user[0][0])

        if ride:
            print(ride)
            ride_id = input(Message.choose_rideId_to_delete)
            self.rider_controller.delete_booked_ride(ride_id)
            # print(Message.ride_deleted)
        else:
            print(Message.no_published_rides)
            return

