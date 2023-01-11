#list is iterated
l1 = ['Apple','banna','cherry']
print(l1[0])

l1[0] = 'pineapple'

print(l1[0])

print(l1[1:3])

l1[1:3] = ['grasap','pineapple']

print(l1[1:3])

l1.insert(2,'Mango')
print(l1)

l1.append('papaya')
print(l1)

#delete element

del l1[0];

del l1[1:2]

# l1.remove("Mango") #you want to write this fun look in to this ele present in or not if not it give it error
# how to handel






# pop:-

# print(l1.pop[3])

# concatenationg and repeating
l2=[2,3,5,6,]
l3=[11,13,56,66]

# print(l2+l3)
# print(l2*l3)


# list comprehension:- used to shorter the syntex when a new list is to be created based on the values of an existing list.

# newlist = [expression for item in list if condition == True]



num_list = [10,25,33,78,98,65,14,21,20,99]

odd = []
even = []

for i in num_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)

# This is list comprehencen

odd = [i for i in num_list if i%2!=0]
even = [i for i in num_list if i%2==0]

print(odd)
print(even)


# double it


double_l=[i*2 for i in num_list]

print(double_l)


# squre even number list

double_l=[i**2 for i in num_list if i%2==0]

print(double_l)


# How to calcualte the time of exeqution

import time

n = 10**6
begin = time.time()
#in loop
result = []
for i in range(n):
    result.append(i**2)
end = time.time()
print("Time takey for loop: ",round(end-begin,2))



# list functions:--- 


# sort():
str_list = ['pineapple', 'grasap', 'Mango', 'pineapple', 'papaya']
str_list.sort(reverse=False)
print(str_list)


# copy()  :new_list=nm_list.copy

l4 = str_list.copy()
l5 = l4

str_list[0] = "papaya"

print(l4)

print(l5)



# len()
# count()
# reverse()
print(num_list.len())
print(num_list.index(99))


print(num_list.count(99))

# count1 = 0
# for i in num_list:
#         if num_list[i]
    
