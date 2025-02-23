
#import -> from "directoryName" import "functionName"
import homework #-> Importing the entire module 
from homework import calculate_sum_numbers #-> Importing the specific function from the module 

homework_assignment_grades = {
    "homework1" : 85 ,
    "homework2" : 100 ,
    "homework3" : 81 
}



print(homework.calculate_sum_numbers(homework_assignment_grades))
print(calculate_sum_numbers(homework_assignment_grades))