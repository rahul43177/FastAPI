"""
Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

"""

animals = ["Zebra" , "Dog" , "Lion" , "Cow" , "Cat"]
print(f"The animal at the third index is {animals[3]}")
del animals[3]
print(f"The updated list -> {animals}")
animals.append("Penguin")
print(f"The new list post appending {animals}")
del animals[0]
print(f"the new list post deleting the first element -> {animals}")

print("\n")
print(f"Printing the first three elements {animals[0:3]}")


