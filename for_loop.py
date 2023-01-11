name = "Subhendu"

for i in name:
    print(i)

lst = ["faju","Rajat","Subhendu"]
for i in lst:
    print(i)


for i in "subhendu":
    if i=="h" or i=="d":
       pass
    print(i)

#range():-it take three operator lazy Evaluation means it take any type of list set dic etc,,diesn't store all values in memory
range(1,10)
list(range(1,10))
#print odd number
for i in range(1,10,3):
    if i%2 != 0:
        print(i)
    

#for-else loop

for i in range(1,10):
    print(i)
    break

else:
    print('done')