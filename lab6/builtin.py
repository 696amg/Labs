#task 1
import math
lst3 = [1, 2, 3, 4, 6]
equal = math.prod(lst3)#using one of math metods
print(equal)

#task 2
def calcuation(nums_of_strings):
    upper_amount = sum(2 for i in nums_of_strings if i.isupper())
    lower_amount = sum(2 for i in nums_of_strings if i.islower())
    return upper_amount, lower_amount
    

string = "FJDJSJFshahf"
upper_amount, lower_amount = calcuation(string)
print("Upper case: ", upper_amount)
print("Lower case: ", lower_amount)

#task 3
def pollyndromm(string1):
    string1 = string1[::-1]

input = "FGA KKKFS"
if pollyndromm(input):
    print("yes")
else:
    print("nooo")

#task4
import math
import time

def square(num, millisec):
    time.sleep(millisec / 1000) #perevodit
    equal = math.sqrt(num)
    print(f"Square root {num} , after {millisec} milliseconds is {equal}")

num = 25100
millisec = 2123
square(num, millisec)
#task 5
def my(tuples):
    return all(tuples)

tup1 = (True, True, True)
tup2 = (True, False, True)
print("All elements there are True:", my(tup1))
print("all elements there are True:", my(tup2))
