import csv
import datetime

#Read all CSV files
with open('./data/distance_data.csv') as csvfile_1:
    distance_data_from_csv = list(csv.reader(csvfile_1))
with open('./data/distance_name_data.csv') as csvfile_2:
    distance_name_csv = list(csv.reader(csvfile_2))

    def get_address():
        return distance_name_csv

    def get_distance(row, col, total):
        distance = distance_data_from_csv[row][col]
        if distance == '':
            distance = distance_data_from_csv[col][row]

    def get_current_distance(row, col):
        distance = distance_data_from_csv[row][col]
        if distance == '':
            distance = distance_data_from_csv[col][row]

        return float(distance)

    # def get_time(distance, truck_list):
    #     new_time = distance / 18
    #     distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
    #         *divmod(new_time * 60, 60))
    #     final_time = distance_in_minutes + ':00'
    #     truck_list.append(final_time)
    #     total = datetime.timedelta()
    #     for i in truck_list:
    #         (hrs, mins, secs) = i.split(':')
    #         total += datetime.timedelta(hours=int(hrs),
    #                                     minutes=int(mins), seconds=int(secs))
    #     return total

    