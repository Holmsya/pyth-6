# Даны две переменных с некоторыми значениями. Поменять местами значения этих переменных

var1 = int(input("Input, plz: "))
var2 = int(input("Input, plz: "))

print(var1, var2)

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2

print(var1, var2)