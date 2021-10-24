# Дано число. Если оно меньше 7, 
# то вывести Yes, если больше 10, 
# то вывести No, если равно 9, то вывести Error.

var = int(input("Input: "))

if var < 7:
    print("Yes")
elif var > 10:
    print("No")
elif var == 9:
    print("Error")