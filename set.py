# set is unordered collecton of data type that is iterable mutable and no duplicate element

s2 = {10,20,30,5,19}

print(type(s2))
print(s2)

for i in s2:
    print(i)


# print(s2.index(10))

# you dont modifiying

# add

s2.add(12)
print(s2)

s2.update([33,31,64])
print(s2)


s2.discard(1) #this is not give the error
print(s2)

# s2.remove(87)  #This is give the key error
# print(s2)



# set operations

a = {1,2,3,4,5}
b = {5,6,3,2,7,8}

print(a|b)
print(a.union(b))

print(a&b)
print(b.intersection(a))


print(a-b)
print(b-a)

# symmetric diff

print(a^b)


