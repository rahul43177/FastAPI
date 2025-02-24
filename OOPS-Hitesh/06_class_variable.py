"""
Class variable
how many objects created with the class -> creating a total_car variable in the class -> Car.total_car += 1
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

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

safari = Car("Tata" , "Nexon")
safariThree = Car("tata" , "Safari")
safari4 = Car("Tata" , "Nano")
# print(safari.total_car)

# test = Car("test" , "test")
# print(test.total_car) #instead of calling like this  , call directly from the class 

print(Car.total_car) #Directly accessing the Car class , class variable