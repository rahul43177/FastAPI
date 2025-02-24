#Adding the functionality in the Class

#self is -> telephone line which is connecting 
#inside the class , we always use the self
class Car():
    def __init__(self , user_brand , user_model):
        self.branch = user_brand 
        self.model = user_model
    
    def full_name(self):
        return f"{self.branch} {self.model}"
    

my_car = Car("Tata" , "Nexon")

print(my_car.full_name())

