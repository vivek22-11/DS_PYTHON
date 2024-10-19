
height = float(input("please enter your height in m:"))
weight = float(input ("please enter your weight in kg:"))
BMI= round((weight/(height*height)),2)
if BMI < 18.5:
    print(f"you are under weight and your BMI is :{BMI}")
elif BMI>18.5 and BMI<25:
    print(f"you are normal weight and your BMI is :{BMI}")
elif BMI>25 and BMI<30:
    print(f"you are over weight and your BMI is :{BMI}")
elif BMI>30 and BMI<35:
    print(f"you are obese weight and your BMI is :{BMI}")
elif BMI>35:
    print(f"you are clinically obese weight and your BMI is :{BMI}")
    
###############################################################################

print("welcome to the roller coaster!!!!") 
height=int(input("please enter your height in cm:"))
if height>=120:
    print("you are eligibal for roller coaster")
    age=int(input("enter your age in years"))
    bill=0
    if age<12:
        print("child's ticket is 5$")
        bill=5
    elif age>12 and age<18:
        print("youths ticket is 7$")
        bill=7
    elif age>=18 and age<45:
         print("youths ticket is 12$")
         bill=12
    elif age>=45 and age<=55:
         print("Adults ticket is 50$")
         bill=50
    want_photo=input("Do you want photo Y or N:")
    if want_photo=='Y':
        bill+=3

###############################################################################

num = input("Enter a number:")
if num == num[::-1]:
    print("\nYes, its a palindrome")
else:
    print("\nNo, its not a palindrome")  
    
###############################################################################

#write a program to find out its duplicate elements
list1=[1,1,2,3,4,5,5,6,7,1]
def is_duplicate(list1):
    for i in range(len(list1)-1):
        #campare current number with next number
        if (list1[i]==list1[i+1]):
            return True
        return False
print(is_duplicate(list1))


list1=[1,2,3,4,5,5,6,7]
def duplicate(list1):
    n=len(list1)
    dup = []
    for i in range(n):
        k= i + 1
        for j in range(k,n):
            if list1[i] == list1[j] and list1[i] not in dup:
                dup.append(list1[i])
    return dup
print("duplicate elements:",duplicate(list1))


###############################################################################

list2 =  [1,12,2,53,0,6,17098] 
max_value = max(list2)
min_value = min(list2)
print("Max_value is:",max_value)
print("Min_value is:",min_value)
if len(list2) == 0 :
    print("avg_value = 0") 
    
else :
      print(sum(list2)/len(list2))

###############################################################################

def are_anagram(str1,str2):
    a=list(str1.replace(""," ").lower())
    b=list(str2.replace(""," ").lower())
    
    if(len(a)!=len(b)):
        return False
    else:
        return(sorted(a)==sorted(b))
print(are_anagram("elbow","below"))
print(are_anagram("hii","below"))

###############################################################################

list=[1,2,5,7,14,55,45,21,49,8,9]
def return_sum(list):
    sum=0
    for i in range(len(list)):
        if(list[i]%5==0 or list[i]%7==0):
            sum=sum+list[i]
    return sum
print(return_sum(list))

###############################################################################

def reverse_words(input):
    if input=="":
        return"you have entered wrong input"
    else:
        words=input.split()
        reverse_sentence=" ".join(reversed(words))
    return reverse_sentence
print(reverse_words("This is India"))

###############################################################################

def is_leap(year):
    if((year>0)  and (year%100==0) and (year%400==0)):
        print(year,"is leap year")
    elif(year%4==0) and (year%100!=0):
        print(year,"is leap year")
    else:
        print(year,"not leap year")
is_leap(1601)
is_leap(2020)

###############################################################################

from random import randint
SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

'''generate a random password'''

def randomPassword():
    #select random length for the password
    randomLength=randint(SHORTEST, LONGEST)
    result=" "
    for i in range (randomLength):
        randomChar=chr(randint(MIN_ASCII,MAX_ASCII))
        result=result+randomChar
    return result
print("your random password is:",randomPassword())

###############################################################################

def fibbo(n):
    list=[]
    prev=0
    cnt=1 
    list.append(cnt)
    for i in range(n-1):
        prev,cnt=cnt,prev+cnt
        list.append(cnt)
    return list
print(fibbo(7))


###############################################################################

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

###############################################################################

from random import randrange
MIN_NUM=1
MAX_NUM=49
NUM_NUMS=6
ticket_nums=[]
for i in range (NUM_NUMS):
    rand=randrange(MIN_NUM,MAX_NUM+1)
    while rand in ticket_nums:
        rand = randrange(MIN_NUM,MAX_NUM+1)
    ticket_nums.append(rand)
ticket_nums.sort()
for n in ticket_nums:
    print(n,end=" ")
    
###############################################################################

''' write a python code to remove outliers'''
values=[89,105,7,4,12,23]
retval=sorted(values)
def removeOutliers(data,num_outliers):
    retval=sorted(data)
    for i in range(num_outliers):
        retval.pop(-1)
    return retval
removeOutliers(values,2)

###############################################################################

def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    for ch in password:
        if ch>"A" and ch<"Z":
            has_upper=True
        elif ch>"a" and ch<"z":
            has_lower=True
        elif ch>="0" and ch<"9":
            has_num= True
            
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
p=input("Enter a password: ")
if checkPassword(p):
    print("Good password")
else:
    print("Try Again new password")
    
###############################################################################

'''password picker'''

import string
#pick the adjectives
adjectives=['sleepy','slow','smelly','wet','fat',
            'rad','orange','yellow','green','blue',
            'purpal','fluffy','white','proud','brave']
# pick the nouns
nouns=['Sarthak','Rohit','Sanket','Aniket','Yash','Abhishek','Vivek']
#pick the words
import random
adjective = random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number = random.randrange(0,100)
#select a special character
special_char = random.choice(string.punctuation)
#create the new secure password
password =adjective + noun + str(number) + special_char
print('your new password is: %s'% password)

# Another one?
# you can use a while loop to generate

print('welcome to password picker!')
while True:
    adjective = random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char= random.choice(string.punctuation)
    password= adjective+noun+str(number)+special_char
    print('your new password is: %s'% password)
    responce = input('would you like another password: ')
    if responce =='n':
        print(end= " ")
        break

