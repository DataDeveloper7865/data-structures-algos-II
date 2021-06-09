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
    package_holder = HashMap()


    # 1. read in excel data 
    # 2. create packages 
    # 3. store in hash table
    # 4. place packages into trucks
    create_packages(package_holder, truck_1, truck_2, truck_3)


    #print packages in trucks
    truck_1.show_packages()
    truck_2.show_packages()
    truck_3.show_packages()

    # place packages in trucks

    # show user interface
    show_user_interface()


if __name__ == '__main__':
    main()