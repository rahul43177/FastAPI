#Jo bhi papa ya dada se mile -> vo inheritance hai 

class Car():
    def __init__(self , brand , model):
        self.brand = brand 
        self.model = model 

    def full_name(self):
        return f"{self.brand} {self.model}"


#Inheritance -> create a electric car class and take the property from the car 

class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model)  #instead of doing self.brand = brand again , we have done that in the car class . We are inheriting those attributes
        self.battery_size = battery_size 

my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")

print(my_tesla.model)
print(my_tesla.full_name())


