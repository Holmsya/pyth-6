import os

peoples = []
menu = ("1. Вывести список", "2. Добавить", "3. Удалить", "4. Выйти")
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    for item in menu:
        print(item)
    choise = input("Команда: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choise == '1':
        for name in peoples:
            print(name)
        input()
    elif choise == '2':
        peoples.append(input("Введите имя человека, которого хотите пригласить: ").capitalize())
    elif choise == '3':
        try:
            peoples.remove(input("Введите имя человека, которого хотите удалить из списка: ").capitalize())
        except ValueError:
            print("Такого человека в списке нет")
            input()
    elif choise == '4':
        break
    os.system('cls' if os.name == 'nt' else 'clear')



