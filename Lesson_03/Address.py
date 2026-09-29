class Address:
    def __init__(self, index, city, street, house, apartment_number):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment_number = apartment_number

    def __formatted_address__(self):
        return (
            f"{self.index}, {self.city}, {self.street}, {self.house} - {self.apartment_number}"
        )
