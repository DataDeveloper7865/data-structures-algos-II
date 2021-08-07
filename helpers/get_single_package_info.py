
# return the information for a single package
def get_single_package_info(truck_1, truck_2, truck_3):

    # Get the user input on which package to view
    user_input = input("""
        Please select an option below to begin or type 'quit' to quit:
            - please type a package number (1 through 40) to view information for that package:
        """)

    # Iterate through each truck list to find package information
    return_package_info(truck_1, user_input)
    return_package_info(truck_2, user_input)
    return_package_info(truck_3, user_input)
    return

# Iterate through truck packages, if it is the packge ID print the package information
def return_package_info(truck, id):
    for package in truck.delivered_package_list:
        if package.package_id == id:
            print(package)
            return
    return