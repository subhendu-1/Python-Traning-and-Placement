# Inherit Private: In python private attributes are denoted usign underscore as the prefix
class Fatehr:
    def __init__(self):
            self.car=10000
            self.__home = 200000

    def myprop(self):
        print("Car" ,self.car)
        print("Home",self.__home)
f1 = Fatehr()
f1.myprop()

class son(Fatehr):
    def muOwnProp(self):
        print("my car: ",self.car) #1000
        # print("my HOme: ",self.__home) #error

s1 = son()
s1.muOwnProp()