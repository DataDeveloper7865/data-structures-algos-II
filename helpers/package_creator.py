import csv
from models.package import Package

# create packages from the excel file given
def create_packages(package_list, truck_1, truck_2, truck_3):

    # read in excel data using csv reader python library
    with open('./data/input_data.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')

        # each row in the file corresponds to a new package
        # create a new package object from the row, using the
        # respective indices
        for row in read_csv:
            new_package = Package(
                package_id = row[0],
                address = row[1],
                city = row[2],
                state = row[3],
                zip_code = row[4],
                deadline = row[5],
                kilos = row[6],
                special_notes = row[7],
                delivery_time= ""
            )

            # place packages in various deliveries depending on certain circumstances outlined in the
            # rubric. Each special case factored in below
            if '84104' in new_package.zip_code and '10:30' not in new_package.deadline:
                truck_3.package_list.append(new_package)

            if new_package.deadline != 'EOD':
                if 'Must' in new_package.special_notes or 'None' in new_package.special_notes:
                    truck_1.package_list.append(new_package)

            if new_package.package_id == '14':
                truck_1.package_list.append(new_package)

            if 'Can only be' in new_package.special_notes or 'Delayed' in new_package.special_notes:
                truck_2.package_list.append(new_package)
            
            if new_package not in truck_1.package_list and new_package not in truck_2.package_list and new_package not in truck_3.package_list:
                truck_2.package_list.append(new_package) if len(truck_2.package_list) < len(truck_3.package_list) else truck_3.package_list.append(new_package)

