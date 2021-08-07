from helpers.get_single_package_info import get_single_package_info
from helpers.get_all_package_info import get_all_package_info

# function to show user interface to user
# takes each truck and references each truck's associated start time
def show_user_interface(truck_1, truck_2, truck_3, truck_1_start_time, truck_2_start_time, truck_3_start_time
):

    # grab user input to direct user to different section's of the program
    user_input = input("""
        Please select an option below to begin or type 'quit' to quit:
            - To get info for all packages at a particular time, type 'all_packages'
            - To get info for a single package type 'package'
        """)

    while user_input != 'quit':

        # if user wants to view all packages
        if user_input == 'all_packages':

            # call associated method
            get_all_package_info(truck_1, truck_2, truck_3, truck_1_start_time, truck_2_start_time, truck_3_start_time)
            show_user_interface(truck_1, truck_2, truck_3, truck_1_start_time, truck_2_start_time, truck_3_start_time)

        # if user wants to view information on an individual package
        elif user_input == 'package':

            # call associated method
            get_single_package_info(truck_1, truck_2, truck_3)
            show_user_interface(truck_1, truck_2, truck_3, truck_1_start_time, truck_2_start_time, truck_3_start_time)

        elif user_input == 'quit':
            print("Goodbye!")
            exit()