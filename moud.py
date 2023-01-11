import Hit_module as hm
print(hm.name_list)
hm.hello_hit()

from Hit_module import *
print(name_list)
hello_hit()

# Built-in modules: pytho has several built-in modules, which can be imported as per requirement.

import math

print((math.sqrt(625)))
print(math.ceil(2.4))
print(math.floor(2.4))
print(math.pi)
print(math.e)
print(math.inf)


# Random Module::


# import random

# print(random.randint(1,10))


# while(True):

    # unum = int(input("Guess a number 1-10: "))
    # snum = random.randint(1,10)

    # if unum==snum:
    #     print("Youn won!!")
    # else:
    #     print("Better luck next itme!!!")


# Time module:--
import time

print(time.time()) #the current use epock time is 1673245917
print(time.ctime(1673245917))
# print(time.ctime(epoch))   ##Returns Human readable tiem
# This run after 5 second
# print("hello")
# time.sleep(5)
# print('hi')

# Sys module :-- system module

import sys

# print(sys.version)
# print(sys.path)
# print(sys.modules)
# print(sys.builtin_module_names)
# print(sys.copyright)


# num = int(input('Enter a non-zero number: '))
# if num==0:
#     print('Oops!!')
#     sys.exit(502)  #This is give the exit code in complet the program 502
# else:
#     print("Thank you")


num1=sys.argv[1]
num2=sys.argv[2]

print(sys.argv)

sum = int(num1) + int(num2)

print(sum)


# PIP:--PIP IS  package installer for python
# package in conainer of all the files need for a module.
# To check pip  version : pip --version
# install pip from https:pypi.org/project/pip/
# install : pip install pandas
# uninstall: pip uninstall pandas


