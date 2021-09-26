# Дано число. Если оно от -10 до 10 не включительно, то увеличить его на 5, 
# иначе уменьшить на 10.

var = int(input("Input: "))

if var > -10 and var < 10:
    var = var + 5
else:
    var = var - 10

print(var)