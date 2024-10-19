

#Creating tuple 

tup1= (1, 3, 5, 7)
print(tup1)

#Accessing elements 

print(f'tup1[0]:{tup1[0]}')
print(f'tup1[1]:{tup1[1]}')
print(f'tup1[2]:{tup1[2]}')
print(f'tup1[3]:{tup1[3]}')

#Accessing Elements of a Tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])

# Tuples can hold different data types

tup2 = (1, 'john', True, -23.45)
for x in tup2:
    print(x)
    print(type(x))

# Iterating Over Tuples

tup3 = ('apple', 'orange', 'plum','apple')
for x in tup3:
    print(x)

# used range function

tup3 = ('apple', 'orange', 'plum','apple')
for x in range (0,4):
    print(tup3[x])
    
# Length of the tuple

tup3 = ('apple', 'orange', 'plum','apple')
len(tup3)

# count how many times a specified value

tup4 = ('apple', 'orange', 'plum', 'apple','banana')
tup4.count('apple')

# index of tuple

tup4 = ('apple', 'orange', 'plum', 'apple','banana')
print(tup4.index('apple'))
print(tup4.index('plum'))

# cheaking if an elements exists

tup4 = ('apple', 'orange', 'plum', 'apple','banana')
if 'banana'  in tup4:
    print('Yes!!')
else:
    print("Not!!")

# Nested Tuples
tuple1 =(1,2,3,4)
tuple2 =('john', 'denise' )
tuple3=(tuple1, tuple2)
print(tuple3)
