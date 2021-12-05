class Customer:
    def __init__(self, name=None, surname=None, patron=None, adr=None, cc=None, bn=None):
        self.__customer = {
            "Name": name,
            "Surname": surname,
            "Patronymic": patron,
            "Address": adr,
            "Credit card": cc,
            "Bank number": bn
        }

    def set(self, type, value):  # type - документированое название данных
        try:
            self.__customer[type] = value
        except KeyError:
            print("Не правильно введён ключ.")

    def get(self, type):
        try:
            return self.__customer[type]
        except KeyError:
            print("Не правильно введён ключ.")

    def info(self):
        for item in self.__customer.items():
            print(item[0], item[1], sep=': ')


customers = []
for i in range(10):
    customer = Customer(
        name="John",
        surname="Smith",
        cc="0000 0000 0000 0000"
    )
    customers.append(customer)

count = 0
for char in "abcdefghik":
    customers[count].set("Patronymic", char)
    count += 1

for customer in customers:
    customer.info()
    print()


