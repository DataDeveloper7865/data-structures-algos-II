from helpers.show_user_interface_cli import show_user_interface
from helpers.package_creator import create_packages
from helpers.show_initial_text import show_initial_text
from models.truck import Truck
from models.hash_table import HashMap

def main():

    # inital welcome user interface
    show_initial_text()

    # instantiate trucks, accepts truck number and departure time
    truck_1 = Truck(1, "08:00:00")
    truck_2 = Truck(2, "09:10:00")
    truck_3 = Truck(3, "11:00:00")

    # instantiate hash map to hold values for fast lookup
    packages = HashMap()

    # 1. read in excel data
    # 2. create packages
    # 3. store in hash table
    # 4. place packages into trucks
    create_packages(packages, truck_1, truck_2, truck_3)

    #print packages in trucks
    truck_1.show_packages()
    truck_2.show_packages()
    truck_3.show_packages()

    # Deliver all the packages
    # method returns distance traveled for package
    total_distance_truck_1 = truck_1.deliver_packages()
    total_distance_truck_2 = truck_2.deliver_packages()
    total_distance_truck_3 = truck_3.deliver_packages()

    # Add the total distance traveled by each truck
    total_distance = total_distance_truck_1 + total_distance_truck_2 + total_distance_truck_3
    print(f"""The total distance traveled for all trucks is {total_distance}""")

    # show user interface
    show_user_interface()


if __name__ == '__main__':
    main()