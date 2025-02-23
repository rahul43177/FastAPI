my_list = [1,2,3,4,5]

for i in range(len(my_list)):
    print(my_list[i])



sum = 0
for i in range(5):
    sum += my_list[i]
new_sum = 0
for val in my_list:
    new_sum += val

print(f"The sum of the for loop is -> {sum}")
print(f"The new sum is {new_sum}")
