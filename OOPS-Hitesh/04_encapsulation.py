"""
Encapsulation -> Capsule jaise dekho 
but hame pata nahi capsule ke andar dawai konsi
"""

class Car():
    def __init__(self , brand , model):
        self.__brand = brand 
        self.model = model 

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + " !"
"""
Make it private and create a getter method
"""

new_car = Car("Tata" , "Harrier")
#i want user to access brand using the below method and does not able to use -> new_car.brand 
print(new_car.get_brand())
print(new_car.__brand) #using double underscore , it will not be directly accessible -> me made it private 
#so we will add two underscore to that variable


"""
1.Class will be able to use it 
2.But in object will not be able to use it 
3.We will have to create the method like get_brand now 
4.two underscore makes it private
5.Learn about setter 
"""

