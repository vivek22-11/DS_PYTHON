#print
print('Hello World')
#Hello World

#Variables
x = 1
print(x)
#1
print(type(x))
#<class 'int'>

x =100.0
print(x)
#100.0
print(type(x))
#<class 'float'>

#Floating Point Numbers
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

#Taking input for user
age = input('Please enter your age:')
print(type(age))
print(age)



age1=int(input("please enter your age: "))
print(type(age1))
print(age1)
age2=int(input("please enter your age: "))
print(type(age2))
print(age2)
age = age1+age2
print(age)

########################### COMPLEX NUMBER ####################################

c1=1
c2=2j
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
#c1: 1 c2: 2j
#<class 'int'>
#<class 'complex'>
#1
#2.0

########################## BOOLEAN VALUES #####################################

all_ok=True
print(all_ok)
print(type(all_ok))
#True
#<class 'bool'>

all_done=False
print(all_done)
print(type(all_done))
#False
#<class 'bool'>


########################## CONVERT STRING INTO BOOLEAN ########################

status= bool(input('ok it is confirmed:'))
print(status)
print(type(status))

######################### AIRTHMETIC OPERATOR #################################

num1 = 10
num2 = 15
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(type(num1 + num2))
print(10 * 4)
print(type(10*4))


home = 10
away = 15
print(home + away)
print(type(home + away))
print(10 * 4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))



print(100 / 20)
print(type(100 / 20))
print(100 // 20)
print(type(100 // 20))
print('Modulus division 100 % 13:', 100 % 13)
print('Modulus division 3 % 2:', 3 % 2)

a = 5
b = 3
print(a ** b)

x = 0
x += 1
print(x)
######################### POSITIVE OR NEGATIVE NUMBER #########################

num = int(input ('enter the number:'))
if num < 0:
    print('negative number')
else:
    print('positive number')
    
######################### ELIF STATEMENT ######################################

saving = float(input("enter how much you have in saving:"))
if saving == 0:
    print("sorry no savings")
elif saving < 500:
    print("well done")
elif saving < 1000:
    print("thats a tidy sum")
elif saving < 10000:
    print("welcome sir!!")
else:
    print("thank you")
    
######################## BREAK LOOP STATEMENT #################################

num= int(input("enter the number :"))
for i in range (0,6):
  if  i == num:
    break
  print(i,' ',end='')
print("done!!")       


num=int(input("enter the number :"))
for i in range (0,6):
  if  i == num:
    break
  print(i,' ',end='')
  print("done!!")


for i in range(0, 10):
   #print(i, ' ', end='')
    if i % 2 == 1:
     continue
     print('hey its an even number')
     print('we love even numbers')
print('Done')

########################### FLOAT VALUE #######################################
int_value = 100
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:', float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:', float_value)
print(type(float_value))
    
########################## nested if elif #####################################

print("Welcome to the roller coaster")
height=int(input("Please enter your height"))

if height>=120:
    print("you can ride the roller coaster")
    age=int(input("Please enter your age "))
    if age<12:
        print("your ticket will be 5$")
    elif age>12 and age<18:
        print("your ticket will be 7$")

    elif age>18:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")     
    
    
####################### neasted if else #######################################
   
print("Welcome to the roller coaster")
height=int(input("Please enter your height"))
age=int(input("Please enter your age "))
if height>=120:
    print("you can ride the roller coaster")
    if age<=18:
        print("your ticket will be 7$")
    else:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")    

###############################################################################
    
winner = None
print(winner is None) 
print(winner is not None)
    
winner = None
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))
print('Set winner to True')
winner = True 
    
###############################################################################
#Comparison Operators 

num = int(input('Enter a number: '))
if num > 0:
    print(num)
  
num = int(input('Enter a number: '))
if num > 0:
 print(num)

###############################################################################
#while loop

count = 1
print('Starting')
while count <= 10:
    print(count)
    count+=1
          
#For Loop
print('Print out values in a range')
for i in range(2,10):
   print(i)
   print('Done') 
    

print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 16):
    if i == num:
      break
    print(i)
    print('Done')
    

# Now use an 'anonymous' loop variable
for _ in range(0,10):
   print('.', end='')
   print() 
    
for _ in range(0,10):
   print('.', end='')
 