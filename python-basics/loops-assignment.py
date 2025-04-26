my_list = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]

count = 0

while count < 3:
    for day in my_list:
        if day == "Monday":
            continue
        print(f"day is -> {day}")
    print("\n")
    count +=1 