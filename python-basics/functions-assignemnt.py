"""
- Create a function that takes 3 parameters -> firstname , lastname , age 
- It returns a dictionary based on those values 
"""

def user_details(first_name , last_name , age):
    user_dict = {
        "firstname" : first_name , 
        "lastname" : last_name , 
        "age" : age
    }
    return user_dict



print(user_details("Rahul" , "Mishra" , 24))