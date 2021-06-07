from helpers.get_all_package_info import get_all_package_info
from helpers.get_single_package_info import get_single_package_info

def show_user_interface():

    print("hello world from user interface")

    user_input = input("""
        Please select an option below to begin or type 'quit' to quit:
            - To get info for all packages at a particular time, type 'all_packages'
            - To get info for a single package at a particular time, type 'package'
        """)

    while user_input != 'quit':

        if user_input == 'all_packages':

            get_all_package_info()
        
        elif user_input == 'package':

            get_single_package_info()


