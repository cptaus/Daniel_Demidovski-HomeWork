from datetime import datetime
import os

# MAIN CLASS


class BestBusCompany:
    """ CLASS FOR HOLDING
        ALL INFO ABOUT COMPANY OPS

        DATA STRUCTURE:
        ROUTES= {LINE_NUMBER:{ORIGIN: STR,
                              DEST: STR,
                              STOPS: [ORDERED],
                              RIDES: [RIDES_ID]}}

        RIDES= {ID:{ORIGIN_T: time,
                    DESTINATION_T: time,
                    DRIVER_NAME: STR
                    DELAYS: LIST}}"""

    def __init__(self):
        self.__routes = []

    # Getter for specific route
    def get_route(self, l_number):
        for i in range(len(self.__routes)):
            if self.__routes[i].__getattribute__("_line_number") == l_number:
                return self.__routes[i]
            else:
                pass

    # Getter for all routes
    def get_routes(self):
        return self.__routes

    # Setter for new route
    def add_route(self, route_obj: object):
        for i in range(len(self.__routes)):
            if self.__routes[i].__getattribute__("_line_number") == route_obj.__getattribute__("_line_number"):
                raise Exception("Route number taken, try other number.")
        self.__routes.append(route_obj)

    # Deleter route
    def delete_route(self, l_number):
        for i in range(len(self.__routes)):
            if self.__routes[i-1].__getattribute__("_line_number") == l_number:
                self.__routes.pop(i-1)

    # Editor route
    def edit_route(self, l_number, origin=None, destination=None, stops_list=None):
        for i in range(len(self.__routes)):
            if self.__routes[i-1].__getattribute__("_line_number") == l_number:
                self.__routes[i-1].__setattr__('_origin', origin) if origin else None
                self.__routes[i-1].__setattr__('_destination', destination) if destination else None
                self.__routes[i-1].__setattr__('_stops_list', stops_list) if stops_list else None


class Route:
    def __init__(self, line_number, origin, destination, stops_list):
        self._line_number = line_number
        self._origin = origin
        self._destination = destination
        stops_list.insert(0, origin)
        stops_list.append(destination)
        self._stops_list = stops_list
        self._rides = []

    # Getter rides
    def get_rides(self):
        return self._rides

    # Setter rides
    def add_ride(self, ride_obj: object):
        if ride_obj is None:
            raise Exception("Please provide an ride!")
        self._rides.append(ride_obj)

    def __repr__(self):
        return f"\nLine {self._line_number} | " \
               f"Start at {self._origin} | " \
               f"End at {self._destination}:\n" \
               f"Stops: {self._stops_list}\n" \
               f"Active Rides: {self._rides}\n"

    def __del__(self):
        return "deleted successfully"


class Ride:
    def __init__(self, origin_time, destination_time, driver_name, delays):
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.driver_name = driver_name
        self.delays = []

    def add_delay(self, delay_in_minutes):
        self.delays.append({datetime.utcnow().strftime("%H:%M:%S"): delay_in_minutes})

    def __repr__(self):
        return f"\nOrigin Time {self.origin_time} | " \
               f"Destination Time {self.destination_time} | " \
               f"Driver Name {self.driver_name} | " \
               f"Delay reports: {self.delays}\n"


# CORE FUNCTIONS


def console_cleaner(new_line=False):
    if new_line:
        os.system('cls')
        print()
    else:
        os.system('cls')


def wait_for_user_continue():
    input("Press Enter to continue...")
    console_cleaner()
