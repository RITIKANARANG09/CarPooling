from enum import Enum


class PublisherOptions(Enum):
    publish_ride = 1
    view_published_ride = 2
    delete_published_ride = 3
    add_vehicle = 4
    view_registered_vehicles = 5
    delete_registered_vehicle = 6
    exit = 7