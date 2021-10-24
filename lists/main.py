from random import randint

someList = ["text", 'test', 23, True]

print(someList)

someList.append(input())
print(someList)

genList = [i for i in range(randint(1, 100))]
print(genList)

print()
for elem in someList:
    print(elem)

someCortege = ("test", "text", 2)

someDict = {'1': "text", '67': "red", "white": "0000h"}

userKey = input()
print(someDict[userKey])
