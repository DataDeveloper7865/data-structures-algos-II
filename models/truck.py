from helpers.distance_calcs import get_current_distance, get_index_from_address, get_time, add_time

class Truck:

    # Truck class constructor
    def __init__(self, truck_number, current_time):
        self.current_time = current_time
        self.truck_number = truck_number
        self.package_list = []
        self.total_distance_traveled = 0
        self.delivered_package_list = []

    # repr method to print instance of each truck
    def __repr__(self):
        return repr(f"""truck number: {self.truck_number} departure time: {self.current_time}""")

    # print each package of each truck
    # O(n) -> Iterates over each package contained in list
    def show_packages(self):
        print(f""" Truck Number: {self.truck_number} contains the following packages""")
        for package in self.package_list:
            print(package)

    # Greedy Algorithm for delivery of packages
    # Algorithm has 3 parts:
    # 1) Base Case -> algorithm ends when there are no more packages in the list
    # 2) Iterate through list to find the smallest distance
    # 3) Iterate through list and pop the package from the list with smallest distance
    #    update properties, calculate time and distance, and add it to the delivered
    #    package list.
    def deliver_packages(self, current_location = 0, total_distance = 0):
        
        # Base case for recursive call:
        # If the list is empty return total distance
        if not len(self.package_list):
            print(f"""Done delivering for truck number: {self.truck_number} """)
            print(f"""Total distance traveled: {self.total_distance_traveled} """)
            return float(self.total_distance_traveled)

        # initial variables
        smallest_distance = 50.0
        next_location = ''

        # iterate through the packages list
        # find the next location to travel to
        # that is the smallest distance away
        for package in self.package_list:
            address_to_compare = package.get_address()
            address_index = get_index_from_address(address_to_compare)
            if get_current_distance(current_location, address_index) <= smallest_distance:
                smallest_distance = get_current_distance(current_location, address_index)
                next_location = address_to_compare

        # iterate through the list again
        # for package in self.package_list:
        for idx, package in enumerate(self.package_list):

            address_to_compare = package.address
            address_index = get_index_from_address(address_to_compare)
            package_distance = get_current_distance(current_location, address_index)

            # if the package matches the next location
            if package_distance == smallest_distance:
                # pop it from the truck list and update the package properties
                # popped_package = self.package_list.pop(package)
                popped_package = self.package_list.pop(idx)

                # 1. calculate the distance traveled and update property on trucklist
                self.total_distance_traveled += package_distance

                # 2. update the departure time in package
                #    & update the current time for truck
                time_taken = get_time(package_distance)
                new_delivered_time = add_time(self.current_time, time_taken)
                self.current_time = new_delivered_time

                # set the delivery time of the delivered package
                popped_package.set_delivered_time(new_delivered_time)

                # 3. Add the new popped package to the delivered package list
                self.delivered_package_list.append(popped_package)

                # 4. Recursively call the function again.
                #    Until list is empty.
                self.deliver_packages(current_location = address_index, total_distance = self.total_distance_traveled)

