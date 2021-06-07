import csv
from models.package import Package


def create_packages():
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
                special_notes = row[7]
            )

            print("Packages in Hub: ", new_package)