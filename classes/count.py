class DecCount:
    def __init__(self, value=0):
        self.__count = value
        print("test")

    def value(self):
        return self.__count

    def up(self):
        self.__count += 1
        if self.__count >= 100:
            self.__count = 99
            print("Не может быть больше 99.")

    def down(self):
        self.__count -= 1
        if self.__count < 0:
            self.__count = 0
            print("Не может быть меньше 0.")


count = DecCount()
print(count.value())

count.up()
print(count.value())

count.down()
print(count.value())

for i in range(100):
    count.up()

for i in range (101):
    count.down()
