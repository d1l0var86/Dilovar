# Classes -chapter 9
# Class - general template , where you haVE DESCRIPTION AND  behaviour anything you wanted to represent
# class name always starts with capital letter

class Dog():
    """"This is the general class about dog"""
    # Attribute(properties)
    breed = ''
    name = ''


    # Behavior , methods
    def bark(self):
        print('wouf wouf !!!')


# Object is the instance(representation in specific way) of Class
class NewDog():
    def __init__(self,name , age):
        self.name = name
        self.age = age
        # Behavior , methods

    def bark(self):
        print(f"{self.name} is barking: wouf wouf !!!")

    def get_name(self):
        """getting the name"""
        print(self.name)

dog1 = Dog()  # mydog is the object of Dog() class
dog1.breed = 'German Shepard'
dog1.name = 'Rex'
dog1.bark()

dog2 = Dog()
dog2.name = 'Bobik'
dog2.breed = 'Pudel'
dog2.bark()

dog3 =NewDog('Sharik', 4)
dog3.bark()
dog3.get_name()

dog4 = NewDog('ralph', 8)
dog4.bark()
dog4.get_name()

print('Name of dog1', dog1.name)
print('Breed of dog1', dog1.breed)

print('Name of dog2', dog2.name)
print('Breed of dog2', dog2.breed)

help(NewDog)