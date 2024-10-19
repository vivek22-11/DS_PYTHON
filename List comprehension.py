numbers=[1,4,6]
value=numbers.__iter__()
item1=value.__next__()
print(item1)
item2=value.__next__()
print(item2)
item3=value.__next__()
print(item3)



num2=[6,8,2]
val=iter(num2)
itm1=next(val)
print(itm1)
itm2=next(val)
print(itm2)
itm3=next(val)
print(itm3)


list=[]
for num in range(0,20):
    list.append(num)
print(list)


list=[num for num in range(0,20)]
print(list)

#Capital first Letter

names=['sarthak','rohit','sanket']
list1=[name.capitalize() for name in names]
print(list1)

#list comprehension with if statement

def is_even(num):
    return num%2== 0 
list2 = [
    num
    for num in range(10)
    if is_even(num)
    ]
print(list2)


lst = [f"{x}{y}"
       for x in range(3)
       for y in range(3)
       ]
print(lst)


#set comprehension 

lists = { x
         for x in range(3)
          }
print(lists)


#Dictionary comprehension

''' output will be like key value pair'''
dict = {x:x*x
        for x in range(3)
        }
print(dict)