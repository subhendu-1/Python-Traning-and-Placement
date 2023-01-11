# Inheritance: It is define a calss ithat inheris all the methods and properites from another class the new class is called derived

# Single Inheritance: a child class

# class Emp:
#     def __init__(self):
#         self.eid = 101
#         self.ename = 'Subhendu'
#     def showId(self):
#         print('Id: ',self.eid)

# class Dev(Emp):
#     def showName(self):
#         print('Name',self.ename)

# d1 = Dev()
# d1.showId()
# d1.showName()
    

# e1 = Emp()
# e1.showId()
# e1.showName() #This is not write because it is the child calss function means parent class can acess the child class fun but child calass not acess this 

# Multipue Inheritance: When a child class inherits from multiple parent class it is called multiple Inheritance
# in this inheritance two parent is hear in child

class Emp:
    eid=102

class Traniner:
    tid=235
class Div(Emp,Traniner):
    did = 750
    def showIds(self):
        print('eid: ',self.eid)
        print('tid: ',self.tid)
        print('did: ',self.did)


e1 = Emp()
t1 = Traniner()
d1 = Div()

d1.showIds()

print(d1.tid)

# print(e1.tid)
# print(d1.eid)



