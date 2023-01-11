# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# (num1,num2) = (num2,num1)
# print(num1)
# print(num2)

# __init__() and self::When a new object is created it is called automaticlly

# it can be called by constructor

# self:- is a prarameter which fefers the currednt object of the clas.



class Test:
    def __init__(myself):
        print('Object creaeted....')
        myself.x=10
        print(id(myself))
    def Show(self):
        print("Inside show method")
# t1=Test()
# t2=Test()
# print(t1,x)
# print(id(t1))   #This is give the same address

# t3 = Show() #This is not call automaticaly because it not a init self function

# class car:
#     def __init__(self,whl,mil) :
#         self.wheel=whl
#         self.milg=mil
#         print("Object created")

#     def show(self):
#         print(self.wheel)
#         print(self.milg)

# c1 = car(4,20)
# c1.show()
# print(c1.wheel)
# print(c1.milg)


# consturctor


class car:
    def __init__(self,whl,mil) :
        self.wheel=whl
        self.milg=mil
        print("Object created")
    def __del__(self):       #It is called garbage collector memorymenegement is automatically
        print("Objedct destroyed")
c1 = car(4,20)
# del c1   it is not called it automatically call by garbage collector

