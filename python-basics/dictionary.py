user = {
    "username" : "rahulmishra" , 
    "name" : "Rahul Mishra" , 
    "age" : 24 
}

print("Dictionary" , user)


name_of_user = user.get("name")
print("Name ->" , name_of_user)


user["is_married"] = False #to create a key and value
print("user" , user)

#looping in the dictionary
for key in user:
    print(key)

for key , value in user.items():
    print(f"The key : {key} and the value : {value}")