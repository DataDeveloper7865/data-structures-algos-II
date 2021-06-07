


class Truck:

    def __init__(self, truck_number, departure_time_from_hub):
        self.departure_time_from_hub = departure_time_from_hub
        self.truck_number = truck_number
        self.package_list = []

    def __repr__(self):
        return repr(f"""truck number: {self.truck_number} departure time: {self.departure_time}""")