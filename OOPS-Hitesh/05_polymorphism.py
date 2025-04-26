"""
Multiform -> polymorphism
Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes , but with different behaviours.
"""

class Car():
    def __init__(self , brand , model):
        self.brand = brand 
        self.model = model
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


my_petrol_car = Car("Tata" , "Safari")
my_tesla = ElectricCar("Tesla" , "Top_Car" , "100kw")

print(f"safari -> {my_petrol_car.fuel_type()}")
print(f"tesla-> {my_tesla.fuel_type()}")

"""
Here same name of the method => but still the output is different and hence the different form with same name -> Polymorphism
"""
