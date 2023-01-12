# Encapsulation:This puts restriction on accessing variables and methods and methods directly

class bike:
    def __init__(self) -> None:
        self.__bike=8000
    
    def showPrice(self):
        print("Bike: ",self.__price)
    def setPrice(self,new_price):
        self.__price = new_price

b1 = bike()
b1.showPrice()
b1.__price = 7500
b1.setPrice(7500)
b1.showPrice()