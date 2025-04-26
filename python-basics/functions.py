"""
Functions
"""

#function definition
def my_function():
    print("Inside the function")

#calling the function
my_function()

def print_my_name(name):
    print(f"Hello {name}")

print_my_name("Rahul")


def print_full_name(first_name , last_name):
    full_name = f"{first_name} {last_name}"
    print(f"Hi How are you {full_name}!!")

print_full_name("Rahul" , "Mishra")
print_full_name("Anshul" , "Kumar")

def multiply(a,b):
    return a*b
print(multiply(2,3))
print(multiply(5,4))

