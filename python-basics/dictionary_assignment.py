"""
1. Create a for loop to print all the keys  -> Done
2. Create a new variable vehicle2 , which is a copy of my_vehicle  -> Done
3. Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4  => Done
4. Delete the mileage key and value from the vehicle2  => Done 
5. Print just the keys from the vehicle2 
"""

#Created a dictionary 
my_vehicle = {
    "model" : "Ford" , 
    "make" : "Explorer" , 
    "year" : 2018 , 
    "mileage" : 40000
}

#Task 1 -> Printing the key and value both 
for key , value  in my_vehicle.items():
    print(f"Key : {key}\nvalue : {value}")
print("\n \n")
#Task 2 -> Creating the copy
vehicle2 = my_vehicle.copy()
print(vehicle2)

#Task 3 -> New key in vehicle2 -> Number of types = 4 
vehicle2["number_of_tyres"] = 4 
print(f"new vehicle 2 with key with types {vehicle2}")

#Task 4-> Delete the mileage key  -> Done 
vehicle2.pop("mileage")
print(vehicle2)

#Task 5 -> Print just the keys from the vehicle2 
for key in vehicle2:
    print("Key",key)
