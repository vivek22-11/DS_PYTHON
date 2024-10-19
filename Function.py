def prime_num(num):
    for i in range(2,num):
        if (num%1==0):
            return "the number is not prime"
            break
        return "the number is prime"
print(prime_num(12))



def greet_user():
    print('hello')
greet_user()

#passsing information to a function 

def greet_user(username):
    print(f'hello,{username}!')
greet_user('sanjivani AI')

#Argument and Parameter 

def describe_pet(animal_type,pet_name):
    print(f'\n I have a {animal_type}')
    print(f" my {animal_type} name is {pet_name}")
describe_pet('Dog','moti')

#default values 

def describe_pet(pet_name,animal_type='dog'):
    print(f'\n I have a {animal_type}')
    print(f" my {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name='Moti')


#Return values 

def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name
musician = get_formatted_name('ram','sarkar')
print(musician)

#Returning a Dictionary of information about a person.
def build_person(first_name,last_name):
    person = {'first': first_name,'last':last_name}
    return person
musician = build_person('ram','sarkar')
print(musician)


#Passing a list 

def greet_users(names):
    for name in names:
        msg= f"hello,{name.title()}!"
        print(msg)
username = ['sanket','rohit','sarthak']
greet_users(username)

#Anagram 

def are_anagram(str1,str2):
    a=list(str1.replace(""," ").lower())
    b=list(str2.replace(""," ").lower())
    
    if(len(a)!=len(b)):
        return False
    else:
        return(sorted(a)==sorted(b))
print(are_anagram("elbow","below"))
print(are_anagram("hii","below"))

#Addition of list 

list=[1,2,5,7,14,55,45,21,49,8,9]
def return_sum(list):
    sum=0
    for i in range(len(list)):
        if(list[i]%5==0 or list[i]%7==0):
            sum=sum+list[i]
    return sum
print(return_sum(list))

#Reverse word 

def reverse_words(input):
    if input=="":
        return"you have entered wrong input"
    else:
        words=input.split()
        reverse_sentence=" ".join(reversed(words))
    return reverse_sentence
print(reverse_words("This is India"))


def rev(s):
    l = list(s.split())
    print(" ".join(l[::-1]))
ip= input("enter the string to be reversed: ")
rev(ip)

#passsing an arbitrary number of argument 

def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#list of topping 

def make_pizza(*toppings):
    print("\n making a pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


#mixing positional and arbitrary arguments 

def make_pizza(size, *toppings):
    print(f"\n making a {size}-inch pizza with the following")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

###############################################################################

'''pizza module in another file pizza.py'''
    
import Pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


################## importing a specific functions #############################

from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


###################### give a function an alias ###############################

from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

from pizza import*
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


###############################################################################

'''pre-requisite to Decorator'''

def plus_one(number):
    number1=number + 1
    return number1
plus_one(5)


'''defining function inside another function'''

def plus_one(number):
    def add_one(number):
        number1=number + 1
        return number1
    result = add_one(number)
    return result
plus_one(5)


'''psssing functions as arguments to other function'''

def plus_one(number):
    result1=number + 1
    return result1
def function_call(function):
    result=function(5)
    return result
function_call(plus_one)

'''function returning other function'''

def hello_function():
    def say_hi():
        return "Hiii"
    return say_hi
hello=hello_function()
hello()

############################# Lambda Function #################################

def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))

add=lambda a,b,c:a+b+c
add(4,5,6)



def mul(a,b,c):
    multi=a*b*c
    return multi
print(mul(6,7,8))

mul=lambda a,b,c:a*b*c
mul(6,7,8)



val=lambda *args:sum(args)
val(1,2,3,5,6)
val(9,8,7,6,5,4,3,2,1)



def myfun(*args):
    for i in args:
        print(i)
myfun("hello","python","how","are","you")
myfun("hello","python")
myfun("this","is","python")


myfun=lambda *args:print(args)
myfun("hello","python","how","are","you")


def person(name, *data):
    print(name)
    print(data)
person('navin',28,'mumbai',98576)


person=lambda name,*data:print(name,data)
person('navin',28,'mumbai',98576)


def person(name, **data):
    print(name)
    print(data)
person(name='rohit',age=28,place='mumbai',mob_no=98576)


person=lambda name,**data:print(name,data)
person(name='rohit',age=28,place='mumbai',mob_no=98576)


def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='rohit',age=28,place='mumbai',mob_no=98576)


person=lambda **data:print(data.items())
person(name='rohit',age=28,place='mumbai',mob_no=98576)


val=lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=10)


person=lambda **data:[(i,j)for i,j in data.items()]
person(name='rohit',age=22,place='mumbai',mob_no=98576)


person=lambda **data:[(j)for i,j in data.items()]
person(name='rohit',age=22,place='mumbai',mob_no=98576)


list1=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,7,18,19,20,21,22,23,24,25,26,27,28,29,30]
sqr=lambda list1:[i**2 for i in list1]
print(sqr(list1))


###############################################################################

def plus_one(number):
        number1=number+1
        return number1
plus_one(6)


#Defining function inside other function
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(4)


#passing function as arguments to other function
def plus_one(number):
        number1=number+1
        return number1
def function_call(function):
    result=function(10)
    return result
function_call(plus_one)


#function Returning other functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi()
hello_function()

#function Returning other functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi()
hello=hello_function()    
hello



def say_hi():
    return "hello there"
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase =func.upper()
        return make_uppercase
    return wrapper()
uppercase_decorator(say_hi)


def say_hi():
    return "hello there"
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase =func.upper()
        return make_uppercase
    return wrapper()
decorate=uppercase_decorator(say_hi)
decorate


#we simply use the @ symbol befor the function we would like to decorator.
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi 


def split_string(function):
    def wrapper():
        func = function
        splitted_string = func.split()
        return splitted_string
    return wrapper()
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi



numbers=[2,6,7,8]
def cal_square(numbers):
    result=[]
    for i in numbers:
        result.append(i*i)
    return result
def cal_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i)
        
    return result
print(cal_square(numbers))
print(cal_cube(numbers))


#Nested Function
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)

#Pass Function as Argument
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)

#Return a Function as a Value
def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Sanjivani")
print(greet()) 


#A Python decorator is a function that takes in a function and returns it by adding some functionality.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
ordinary()    
 
    
def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner
# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()



def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  


#Decorating Functions with Parameters

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner
@smart_divide
def divide(a, b):
    print(a/b)
divide(2,5)
divide(2,0)


#Chaining Decorators
#*args and **kwargs in Python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner
@star
def multi(a, b):
    print(a*b)
multi (2,3)


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner
@star
@percent
def printer(msg):
    print(msg)

printer("Hello")


def multiply(num1,num2):
    return num1*num2
print("product:", multiply(2,3)) 


def multiplyThreeNumbers(num1, num2, num3):
    return num1*num2*num3
print("product:",multiplyThreeNumbers(1, 2, 3))


def multiplyNumbers(*numbers):
    product=1
    for n in numbers:
        product*=n
    return product
print("product:",multiplyNumbers(4,4,4,4,4,4))


def makeSentence(**words):
    sentence=''
    for word in words.values():
        sentence+=word
    return sentence
print('Sentence:', makeSentence(a='Kwargs ',b='are ', c='awesome!'))


def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(key, value))
    return result
print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))

def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)
printingData('007', 'agent', firstName='James', lastName='Bond') 
###############################################################################

import time
def cal_square(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i)
        
    end=time.time()
    print((end-start)*1000)
    print("took " + str((end-start)*1000) + "mili sec")
    return result
array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)


import time
def cal_cube(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i*i)
        
    end=time.time()
    print((end-start)*1000)
    print("took " + str((end-start)*1000) + "mili sec")
    return result
array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)



import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func._name_+" took "+str((end-start)*1000)+"mil sec")
        return result
    return wrapper 
@time_it 
def cal_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it 
def cal_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
array=range(1,100000)
out_square=cal_square(array)
out_cube=cal_cube(array)
