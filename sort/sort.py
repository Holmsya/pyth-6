import random

def sortList(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list [j+1]:
                buf = list[j]
                list[j] = list[j+1]
                list[j+1] = buf

randList = [random.randint(0, 100) for i in range(random.randint(1, 100))]
print(randList)
sortList(randList)
print(randList)
