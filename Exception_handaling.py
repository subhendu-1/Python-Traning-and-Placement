# Error caused by not following proper syntax of any language. This is run tiem and static TThis is also called syntax error.

# A python rpgram terminates as soon as it encounters and unhandled error.
# exceptin is run time error and dynamic error


# print('hello'  #This is syntex error

# num1= 10
# num2 = 0 #This is creat run tiem error

# res = num1/num2
# print(res)


# handeling process
# try...except Block


# num1= 10
# num2 = 0 #This is creat run tiem error
# try:
#     res = num1/num2
#     print(res)
# except ZeroDivisionError:  #if you know the Error
#     print('num2 can not be zero')
# except NameError as e:
#     print(e)

# except TypeError:
#     print("Wrong type")


# except Exception as ae:
#     print(ae)


# Else and Finally Block::
# Else block will be executed if no exception occurs
# Finally block will be execured if ex

num1= 10
num2 = 0 #This is creat run tiem error
try:
    res = num1/num2
    print(res)
except:
    print("Num2 can not be zero")
else:
    print('No error')
finally:
    print('Good bye....')


# Raise An Exception:If you create own exception


num = int(input('Enter my fav number: '))


if num == 45:
    print('Thank you')
else:
    raise Exception('This is not my fav number-subhendu')






