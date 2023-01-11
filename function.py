# funcion is a block of codes which performe a specific task.

# syntex:
# def function_name(arg):
#     statement1 #function body
#     return Value

# func name is uniquely 
# arguments and return statement is opetional


# def demo():
#     print("I am inside function......")

# demo()


# def sum(a,b):
#     result = a+b
#     # print(result)
#     return result

# # sum(5,2)
# print(sum(4,2))

# # default value pass in fun argument because it handel the run time error when you not pass the argument

# def hello(name = "Subhendu"):
#     print("hello I am ",name)

# hello('Rajat')

# def helloo(name,country = "India"):
#     print(name,'is from',country)
# helloo(country="USA",name="modi")


# arbitari argument//// *args

# def grit(*name):
#     print(name[2])
#     print(name)
#     print(type(name))

# # grit('subhendu','rajat','Raj')

# helloo('modi',Biden')



def dic_fun(**kwargs):
    print('name',kwargs['name'])
    print('food',kwargs['food'])
    print(kwargs)

dic_fun(name='Subhendu',food = "roti",sport='cricket')

#factorial of a number using functin recursion
def fact_rec(num):
    fact = 1
    if num>1:
        fact = num*fact_rec(num-1)
    return fact

print(fact_rec(5))


# Sum os first 10 number using Recursion

def sum_fec(num):
    sum = 0
    if num >0:
        sum = num + sum_fec(num-1)
    return sum


print(sum_fec(10))



# Lambda function:-- lambda is an anonymous function can be defined without name. It can take any number of arguments but can only have one expression.

# syntax: 
# lambda arguments : expression


# one arguments
x = lambda a:a*2

print(x(3))
# two argumentas
x = lambda a,b:a*b

print(x(3,4))

# The use os lambda is better shown when it is used as an anonumous function

def pow(n):
    return lambda a:a**n

sqr = pow(2) #This is lambda function so this is a^2
print(sqr(5))  #hear a = 5 so 5^2= 125