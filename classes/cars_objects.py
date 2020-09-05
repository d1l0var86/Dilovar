from classes.cars import Car, ElectricCar



car1 = Car('toyota' , 'highlander',2020)
print(car1.get_description())
car1.set_color('Red')
print(car1.get_description())
print(car1.read_odometer())

car1.odometer_reading = 1000
print(car1.read_odometer())
print(car1.odometer_reading)

car1.set_odometer(800) # not good practise
print(car1.read_odometer()) # we can put logic in the method
print(car1.odometer_reading)

car1.set_odometer(1500)
print(car1.read_odometer())

car1.increment_odometer(-500)
print(car1.read_odometer())

car1.increment_odometer(400)
print(car1.read_odometer())

ecar1 = ElectricCar('Tesla', 'Model Y','2020')
print(ecar1.get_description())
ecar1.set_color('Blue')
print(ecar1.get_description())

print('--------------------------------')
ecar1.test_method()

#  Object Oriented Programming
#  - Class , Object
#  - Inheritance (single class, multiple class)
#  - Constructor with (__init__()) method
#  - self keyword , super() method , difference
#  - Overriding(due Inheritance) - rewriting parent attributes/methods in child class
#  - check: java method to overload, using the same name with diff parameters
#  - relationship between parent and child: Parent >> child
# car1.battery_size, car1.test_method()  parent does not have access
#  - self keyword, super() method , difference
# - Overriding(due Inheritance) - rewrite parent attributes/method in child class

#  OOP concepts :
#  inheritance - reuse the code from other class(es)
#  polymorphism (overriding, overloading) - using the same methods
#  abstraction (class, method) - making abstract classes (for planing, making rules for child  classes)
#  encapsulation - putting in a capsule(data hiding or method hiding)

