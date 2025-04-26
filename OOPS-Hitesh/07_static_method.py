"""
Static method -> 
Problem : Add a static method to the Car class that returns a general description of a car.

Static Method = Method which is accessible to the class but no the objects
"""

class Car():
    total_car = 0 
    def __init__(self , brand , model):
        self.brand = brand 
        self.model = model
        Car.total_car += 1
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod #add this so that , we have to call the class to access this -> no object will be able to access it
    def general_description():
        return "Cars are means of transport!"


safari = Car("Tata" , "Safari")
print(safari.general_description()) #I don't want the user to access this method from the object 

"""
We will apply the static method using @staticmethod and hence we don't need the self here , as we are not allowing the object to communicate with class
"""



