from helpers.package_creator import create_packages
from helpers.show_initial_text import show_initial_text
from models.truck import Truck

def main():

    # inital welcome user interface
    show_initial_text()

    # read in excel data and create packages and store in hash table
    create_packages()

    # place packages in trucks

    # show user interface

    truck_1 = Truck(1, "noon")
    truck_2 = Truck(2, "noon")
    truck_3 = Truck(3, "noon")

    print(truck_1)
    print(truck_2)
    print(truck_3)


if __name__ == '__main__':
    main()