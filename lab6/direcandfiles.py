#task1
import os 
 
def list_directories(path): 
    return [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))] 

#task2
import os
path1 = input("Input a path: ")

print(f"{path1} exists: {os.access(path1, os.F_OK)}")
print(f"{path1} is readable: {os.access(path1, os.R_OK)}")
print(f"{path1} is writeable: {os.access(path1, os.W_OK)}")
print(f"{path1} is executable: {os.access(path1, os.X_OK)}")
#task3
path1 = input("Input a path: ")

if os.access(path1, os.F_OK):
    print(f"The path {path1} exists!")
    if os.path.isfile(path1):
        print(f"The directory portion of the path: {os.path.dirname(path1)}")
        print(f"The filename portion of the path: {os.path.basename(path1)}")
    else:
        print(f"The directory of the path: {path1}")
else:
    print(f"The path {path1} does not exist")
#task4
f = open("text4.txt", "r")
print(len(f.readlines()))
f.close()
#task5
f = open("text5.txt", "w")
li = input("Input a list of values separated by commas: ").split(", ")
f.write(str(li))
f.close()
#task6
from string import ascii_uppercase

new_path = "kbtu_pp2\\Lab6_pp2\\alphabet"
if not os.access(new_path, os.F_OK):
    os.makedirs(new_path)

for letter in ascii_uppercase:
    f = open(f"{new_path}\\{letter}.txt", "w")
    f.write(f"This is {letter}'s txt file")
    f.close()
#task7
with open("builtin_func.txt", "r") as f1:
    f2 = open(f"copy_builtin_func.txt", "w")
    for line in f1:
        f2.write(line)
    f1.close()
#task 8
path = input()

if os.access(path, os.F_OK):
    print(f"File is readeable: {os.access(path, os.R_OK)}\nFile is writeable: {os.access(path, os.W_OK)}")
    os.remove(path)
    print("The file is Deleted")
