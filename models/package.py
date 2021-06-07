

class Package:

    def __init__(self, package_id, address, city, state,
                    zip_code, deadline, kilos, special_notes,
                    delivery_start = '', address_location = '', delivery_status = 'In Hub'):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.kilos = kilos,
        self.special_notes = special_notes
        self.delivery_start = delivery_start
        self.address_location = address_location
        self.delivery_status = delivery_status

    def __repr__(self):
        return repr(f"""id: {self.package_id} Notes: {self.special_notes} Deadline: {self.deadline}""")

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def get_deadline(self):
        return self.deadline

    def get_kilos(self):
        return self.kilos

    def get_notes(self):
        return self.special_notes