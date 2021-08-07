import csv
from datetime import datetime

#Read all CSV files
with open('./data/distance_data.csv') as csvfile_1:
    distance_data_from_csv = list(csv.reader(csvfile_1))
with open('./data/distance_name_data.csv') as csvfile_2:
    distance_name_csv = list(csv.reader(csvfile_2))

    # Return address
    def get_address():
        return distance_name_csv

    # Gets the current distance given the row and col
    def get_current_distance(row, col):
        distance = distance_data_from_csv[row][col]
        if distance == '':
            distance = distance_data_from_csv[col][row]

        return float(distance)

    # Takes an adress in string and returns an index
    def get_index_from_address(address_to_find):
        for address in distance_name_csv:
            if address[2] == address_to_find:
                return int(address[0])

    # Takes distance as float and returns string
    def get_time(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        return final_time

    # Adds time from the current time plus the amount
    # of time elapsed
    def add_time(cur_time, elapsed_time):
        cur_time_datetime = datetime.strptime(
            cur_time,
            "%H:%M:%S"
        )
        elapsed_time_datetime = datetime.strptime(
            elapsed_time,
            "%H:%M:%S"
        )
        time_zero = datetime.strptime('00:00:00', '%H:%M:%S')

        return (cur_time_datetime - time_zero + elapsed_time_datetime).time().strftime("%H:%M:%S")