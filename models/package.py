
class Package:

    # contstructor of package class
    def __init__(self, package_id, address, city, state, zip_code, deadline, kilos, special_notes, delivery_time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.kilos = kilos
        self.special_notes = special_notes
        self.delivery_time = delivery_time

    #  repr method to print instantiated packages
    def __repr__(self):
        tab = '\n'
        return f"""{tab}
            package id: {self.package_id} {tab}
            Delivery Address: {self.address} {tab}
            City: {self.city} {tab}
            State: {self.state} {tab}
            Zip Code: {self.zip_code} {tab}
            Deadline: {self.deadline} {tab}
            Kilos: {self.kilos} {tab}
            Notes: {self.special_notes} {tab}
            Delivered At: {self.delivery_time} {tab}"""

    # return string of address
    def get_address(self):
        return self.address

    # set the delivered time of the package property
    def set_delivered_time(self, time):
        self.delivery_time = time