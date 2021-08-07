from helpers.show_user_interface_cli import show_user_interface
from helpers.package_creator import create_packages
from helpers.show_initial_text import show_initial_text
from models.truck import Truck
from models.hash_table import HashMap

# main method of program
def main():

    # inital welcome user interface to show text
    # Space - Time Complexity: Time - O(1) & Space - O(1)
    show_initial_text()

    # create global variable to hold the departure time for each truck
    # the departure times are chosen to account for the two drivers coming back to hub
    # Space - Time Complexity: Time - O(1) & Space - O(1)
    truck_1_start_time = "08:00:00"
    truck_2_start_time = "09:10:00"
    truck_3_start_time = "11:00:00"

    # instantiate each truck, accepts truck number and departure time
    # Space - Time Complexity: Time - O(1) & Space - O(1)
    truck_1 = Truck(1, truck_1_start_time)
    truck_2 = Truck(2, truck_2_start_time)
    truck_3 = Truck(3, truck_3_start_time)

    # instantiate hash map to hold values for fast lookup
    packages = HashMap()

    # 1. read in excel data
    # 2. create packages
    # 3. place packages into trucks
    # Space - Time Complexity: Time - O(n) & Space - O(n)
    create_packages(packages, truck_1, truck_2, truck_3)

    # Deliver all the packages
    # Space - Time Complexity: Time - O(n^2) & Space - O(n)
    truck_1.deliver_packages()
    truck_2.deliver_packages()
    truck_3.deliver_packages()

    # Add the total distance traveled by each truck
    # Space - Time Complexity: Time - O(1) & Space - O(1)
    total_distance = truck_1.total_distance_traveled + truck_2.total_distance_traveled + truck_3.total_distance_traveled
    print(f"""The total distance traveled for all trucks is {total_distance}""")

    # show user interface
    # Space - Time Complexity: Time - O(1) & Space - O(1)
    show_user_interface(truck_1, truck_2, truck_3, truck_1_start_time, truck_2_start_time, truck_3_start_time)

# call program
if __name__ == '__main__':
    main()