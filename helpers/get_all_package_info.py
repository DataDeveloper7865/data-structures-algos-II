from datetime import datetime

# Get all of the package information according to a time input by the user
def get_all_package_info(truck_1, truck_2, truck_3, 
    truck_1_start_time, 
    truck_2_start_time,
    truck_3_start_time 
):

    # Get user input
    user_input = input("""
        Please select an option below to begin or type 'quit' to quit:
            - please type a time between 08:00:00 and 16:00:00 (in that exact format) to view 
            status of packages
        """)

    # Get each of the package's status from each of the delivered truck lists
    get_package_status(truck_1, truck_1_start_time, user_input)
    get_package_status(truck_2, truck_2_start_time, user_input)
    get_package_status(truck_3, truck_3_start_time, user_input)
    
    return

# Find the status of each package based on the delivery time
def get_package_status(truck, start_time, time):
    start_datetime = datetime.strptime(start_time, "%H:%M:%S")
    time_datetime = datetime.strptime(time, "%H:%M:%S")

    # iterate through each of the packages in the delivered package list
    for package in truck.delivered_package_list:
        # if time is less than than start_time, package at hub
        if time_datetime < start_datetime:
            print(f"""Package: {package.package_id} is At Hub at {time}""")
        # if time is greater than start time, check if package has been delivered
        elif time_datetime > start_datetime:
            datetime_delivered = datetime.strptime(package.delivery_time, "%H:%M:%S")
            if datetime_delivered > time_datetime:
                print(f"""Package: {package.package_id} is In Transit at {time}""")
            else:
                print(f"""Package: {package.package_id} is Delivered by {time} and at {package.delivery_time}""")
    return