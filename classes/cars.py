
class Car():
    """This is class to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = 'White'
        self.odometer_reading = 0
    # getter and setter
    def get_description(self):
        msg = f"Your car: \nmanufacture: {self.make},\nmodel: {self.model}\nYear: {self.year}\nColor: {self.color}"

        return msg

    def set_color(self, new_color):

        print(f"Changing the color {self.color} to {new_color}")
        self.color = new_color

    def read_odometer(self):
        """Get the odometr miles of the car."""
        msg = f"Car has {self.odometer_reading} miles on it."
        return msg

    def set_odometer(self, new_miles):
        if new_miles >= self.odometer_reading:
            print(f"Setting odometer reading from {self.odometer_reading} to {new_miles}")
            self.odometer_reading = new_miles

        else:
            print(f"You can not roll back odometer from {self.odometer_reading} to {new_miles}.")

    def increment_odometer(self, miles):
        """:param miles to odometer_reading"""
        # self.odometer_reading = self.odometer_reading + miles
        if miles > 0:
            print(f"Incrementing odometer with more {miles} miles")
            self.odometer_reading += miles
        else:
            print(f"Negative value cannot be passed to odometer : {miles}")



class ElectricCar(Car):
    """Represents Electric car , inherits all features of Car."""
    def __init__(self, make,model,year):
        """child class constructor , Overriding the parent constructor"""
        super().__init__(make,model,year) # calling the constructor of parent class
        self.battery_size =80

    def get_description(self):
        msg = f"Your car: \n\tmanufacture: {self.make},\n\tmodel: {self.model}\n\tYear: {self.year}"\
              f"\n\tColor: {self.color}\n\tBattery size: {self.battery_size}"

        return msg

    def test_method(self):
        print(self.get_description()) # current class get_description() method, with battery_size
        print(super().get_description()) # parent class get_description() method
