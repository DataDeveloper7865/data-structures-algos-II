import csv
from models.package import Package


def create_packages(package_list, truck_1, truck_2, truck_3):

    with open('./data/input_data.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')

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

            # TODO: fix package_list
            # insert package into hash table for fast lookup
            # package_list.insert_value_into_hash_table(new_package.id, new_package)

            # place packages in various deliveries depending on certain circumstances

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

