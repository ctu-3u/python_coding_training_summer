class Restaurant():

    def __init__(self, name, typeset):
        self.restaurant_name = name
        self.cuisine_type = typeset
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print("Rdstaurant is open")

    def set_number_served(self, value):
        self.number_served = value
    
    def increment_number_served(self, value):
        self.number_served += value


class IceCreamStand(Restaurant):

    def __init__(self,name,flavors=[]):
        super().__init__(name,'ice cream stand')
        self.flavors = flavors
    
    def record_flavors(self,flavors):
        self.flavors = flavors

    def show_flavors(self):
        print("This stand provides ice cream with flavors:")
        for item in self.flavors:
            print(item)
        