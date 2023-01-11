# ia an unordered collection of items. each item of a dictionary has a key/value pair.
# unordered
# mutable
# don't allow duplicates

std = {'id':101,'name':'subhendu','sub':['python','web','c++']}

print(type(std))

print(std['id'])

print(std.get('id'))

print(std.keys())
print(std.values())
print(std.items())



# loopint in dict


for i in std:
    print(i)
for i in std.keys():
    print(i)
for i in std.values():
    print(i)

for k,b in std.items():
    print(k,b)


for i in std.keys():
    print(i)


# updated methods:


std['id'] = 102

print(std)

std['loc'] = "haldia"

print(std)


std.update({"id":105})
print(std)


# romove

res = std.pop("sub")
print(res)


res = std.popitem()

print(res)
