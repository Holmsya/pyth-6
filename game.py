from random import randint

games = int(input("Введите количество партий: "))

kam = 0
noj = 0
bum = 0
wins = 0

while True:
    stepHum = int(input("Сделайте свой ход(1 - камень, 2 - ножницы, 3 - бумага): "))
    stepAI = randint(1, 3)

    if stepAI == 1:
        print("AI: камень")
        kam += 1
    elif stepAI == 2:
        print("AI: ножницы")
        noj += 1
    elif stepAI == 3:
        print("AI: бумага")
        bum += 1
    
    if stepHum == 1:
        print("Human: камень")
        kam += 1
    elif stepHum == 2:
        print("Human: ножницы")
        noj += 1
    elif stepHum == 3:
        print("Human: бумага")
        bum += 1

    if (stepHum == 1 and stepAI == 2) or (stepHum == 2 and stepAI == 3) or (stepHum == 3 and stepAI == 1):
        print("Вы победили!")
        wins += 1
    elif (stepAI == 1 and stepHum == 2) or (stepAI == 2 and stepHum == 3) or (stepAI == 3 and stepHum == 1):
        print("Вы проиграли!")
    else:
        print("Ничья")
    
    games -= 1
    if games == 0:
        break

print("Выбрано: \n", "\t- камень:", kam, "\n", "\t- ножницы:", noj, "\n", "\t- бумага:", bum)
print("Побед:", wins)