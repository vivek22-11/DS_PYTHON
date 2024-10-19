
#Generator
''' it is another way of creating iterators
in a simple way where
it uses the keyword "yield"
instead of returning it in a defined functions
generator are implemented using a function'''

gen=(x
     for x in range(3)
     )
print(gen)
for num in gen:
    print(num)


gen=(x
     for x in range(3)
     )
next(gen)


gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)


def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)


gen=range_even(6)
next(gen)
next(gen)


######################### Chaining Generators #################################

def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords=["NOT-GOOD","give 'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
    
    

def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords=["Vivek"]
for password in hide(lengths(passwords)):
    print(password)


######################## printing list with index #############################

lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')


#same code can be implemented using enumerate
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")


#Use of zip function
name=['Rohit','Sanket','Sarthak']
info=[9850,6032,9785] 
for nm,inf in zip(name,info):
    print(nm,inf)


#Use of zip function with mis match list
name=['Rohit','Sanket','Sarthak','Shubham']
info=[9850,6032,9785] 
for nm,inf in zip(name,info):
    print(nm,inf)   


#zip_longest
from itertools import zip_longest
name=['Rohit','Sanket','Sarthak','Shubham']
info=[9850,6032,3297]
for nm,inf in zip_longest(name,info):
    print(nm,inf)


#use of fill value instead None
from itertools import zip_longest
name=['Rohit','Sanket','Sarthak','Shubham']
info=[9850,6032,3297]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)


#use of all(),if all the values are true then it will produce output
lst=[2,3,6,8,9]
if all(lst):
    print('all values are true')
else:
    print('Useless')


lst=[2,3,0,8,9]
if all(lst):
    print('all values are true')
else:
    print('Useless')


#use of any
lst=[0,0,0,8,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')


#use of any
lst=[0,0,0,0,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')


#count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))


#Now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))


#cycle()
#suppose you have repeated tasks to be done,then you can use this method
import itertools
instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
    

#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)


#combinations()
from itertools import combinations
players=['John','Jani','Janardhan']
for i in combinations(players,2):
    print(i)


from itertools import permutations
players=['John','Jani','Janardhan']
for seat in permutations(players,2):
    print(seat)



#product()
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)


age=[27,17,21,19]
adults=filter(
    lambda age:age>=18,
    age
    )
print([age for age in adults])

