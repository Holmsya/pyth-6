class Fridge:
    def __init__(self, volume, color, bool=True):
        # список в котором хранятся названия продуктов из холодильника
        self.__products = []
        # параметры холодильника
        self.freezer = bool # морозильная камера
        self.__volume = volume
        self.color = color.capitalize()

    def put(self, product):
        if self.__volume > 0:
            self.__products.append(product.capitalize())
            self.__volume -= 1
        else:
            print("Холодильник полон, сначала достаньте что-нибудь.")

    def pop(self, product):
        try:
            return self.__products.pop(self.__products.index(product))
        except ValueError:
            print("Такого продукта в холодильнике нет, достаньте что-нибудь другое.")

    def printProducts(self):
        for product in self.__products:
            print(product)

fridgeLG = Fridge(volume=60, color="black")



for i in range(65):
    fridgeLG.put("Milk")

print("Test")
print()
fridgeLG.printProducts()

print()

fridgeLG.pop("Meat")

fridgeLG.printProducts()

fridgeLG.pop("Fish")
