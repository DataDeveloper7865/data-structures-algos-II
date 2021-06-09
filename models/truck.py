from helpers.distance_calcs import get_current_distance


class Truck:

    def __init__(self, truck_number, departure_time_from_hub):
        self.departure_time_from_hub = departure_time_from_hub
        self.truck_number = truck_number
        self.package_list = []
        self.total_distance_traveled = 0
        self.ordered_package_list = []

    def __repr__(self):
        return repr(f"""truck number: {self.truck_number} departure time: {self.departure_time_from_hub}""")

    def show_packages(self):
        print(f""" Truck Number: {self.truck_number} contains the following packages""")
        for package in self.package_list:
            print(package)


    def determine_shortest_path(self, current_location):
        if not len(self.package_list):
            return self.package_list

        smallest_distance = 50.0
        location = 0
        total_distance = 0


        # 1. iterate through package list
        # 2. if the distance from the current location to the next address is smaller,
        #    set the smallest distance equal to the current distance being compared
        for package in self.package_list:
            address_to_compare = package.address
            if get_current_distance(current_location, address_to_compare) <= smallest_distance:
                smallest_distance = get_current_distance(
                    current_location, address_to_compare)
                location = address_to_compare

        for package in self.package_list:
            if get_current_distance(current_location, package.address) == smallest_distance:
                self.ordered_package_list.append(package)
                self.package_list.pop(package)
                current_location = location
                total_distance += smallest_distance
                determine_shortest_path(self.package_list, current_location)

