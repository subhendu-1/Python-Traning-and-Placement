tup1 = (10,25,33,49,78)

# print(tup1[0:3])

# # del tup1[1] #you don't do this because this is immutable
# del tup1 #this is write




# for i in tup1:
#     print(i,sep='*',end='')


fruit_tup = ('Apple','banana','orange','cherry')

(*a,b,o) = fruit_tup
print(o)

# (a,b,o) = fruit_tup
# print(a)


# Tuple Methods:- 

print(fruit_tup.count('Apple'))


# it is use whent you want to iterating 