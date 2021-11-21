from random import randint

class Hero:
    def __init__(self):
        self.__power = 25
        print("Герой вступил в игру.")

    def buf(self, art):
        self.__power += art
        print("Герой получил услиение на", art)

    def power(self):
        return self.__power

class Artefact:
    def __init__(self, value):
        self.__power = value

    def power(self):
        return self.__power

class Monster:
    def __init__(self, value):
        self.__power = value

    def power(self):
        return self.__power


levels = [randint(0, 1) for i in range(10)]

hero = Hero()
count = 1
for level in levels:
    if level == 0:
        art = Artefact(randint(10, 80))
        print("Герой увидел артефакт силой", art.power())
        hero.buf(art.power())
        count += 1
    else:
        monster = Monster(randint(5, 100))
        print("Герой встретил монстра силой", monster.power())
        if hero.power() >= monster.power():
            print("В этой схватке победил герой.")
            count += 1
        else:
            print("В этой схватке победил монстр.", "Герой пал на " + str(count) + " уровне.", sep='\n')
            exit()
print("Герой прошёл все комнаты со значением силы", hero.power())

