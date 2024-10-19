
#create lists 

list1 = ['john','paul','george','Ringo']
print(list1)

#Neasted list 

list1 = [1,43.5,True]
list2 = ['apple','orange',31]
root_list = ['john',list1, list2,'denise']
print(root_list)

#Accessing elements from a list 

list1 = ['john','paul','george','Ringo']
print(list1[-1])
list1[-1]
list1[-2]



list1 = ['john','paul','george','Ringo']
print('list1[1]:',list1[1])
print('list1[-1]:',list1[-1])
print('list1[1:3]:',list1[1:3])
print('list1[:3]:',list1[:3])
print('list1[1:]:',list1[1:])

# Adding element to list (APPEND/EXTEND/INSERT) 

list1 = ['john','paul','george','Ringo']
list1.append('pete')
print(list1)


list1 = ['john','paul','george','Ringo', 'pete']
print(list1)
list1.extend(['Albert', 'Bob'])
list1 

#insert element using index
a_list = ['Adele','Madonna','Cher']
print(a_list)
a_list.insert(1,'paloma')
print(a_list)

#List Concatentaion 

list1 = [3,2,1]
list2 = [6,5,4]
list3 = list1 + list2
print(list3)

#Remove Elements (remove/pop) 

another_list = ['gary','mark','robbie','joson']
print(another_list)
another_list.remove('robbie')
print(another_list)


list6 = ['once','upon','a','time']
print(list6)
print(list6.pop(2))
print(list6)

################################## PATTERN ####################################

for i in range(4):
    for j in range(4):
        print('#',end=' ')
    print()
    


for i in range(4):
    for j in range(i+1):
        print('#',end=' ')
    print()


for i in range(4):
    for j in range(4-i):
        print('#',end=" ")
    print()


for i in range(6):
    print(' ' * (6-i),'#' * (2*i+1))
for j in range(6-2,-1,-1):
    print(' ' *(6-j),'#'*(2*j+1))
    

###############################################################################

#Shallow copy and Deep copy

list_a = [ 1, 2, 3, 4, 5]
list_b = list_a
list_a[0] = -10
print(list_a)
print(list_b)


#shallow copy

import copy
list_a = [ 1, 2, 3, 4, 5]
list_b = copy.copy(list_a)
list_b[0] = -10
print(list_a)
print(list_b)


import copy
list_a = [[ 1, 2, 3, 4, 5], [6,7,8,9,10]]
list_b = copy.copy(list_a)
list_a[0][0]= -10
print(list_a)
print(list_b)



#deep copies
import copy
list_a = [[ 1, 2, 3, 4, 5], [6,7,8,9,10]]
list_b = copy.deepcopy(list_a)
list_a[0][0]= -10
print(list_a)
print(list_b)

    
#shallow copy and deep copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list
new_list[2][2] = 9
print('Old List:', old_list)
print('ID of Old List:', id(old_list))
print('New List:', new_list)
print('ID of New List:', id(new_list))



x=[1,2,3]
import copy
copy.copy(x)
copy.deepcopy(x)


import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
print("Old list:", old_list)
print("New list:", new_list)


import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)


import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)


import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
print("Old list:", old_list)
print("New list:", new_list)


import copy
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[1][0] = 'BB'
print("Old list:", old_list)
print("New list:", new_list)


import copy
lst1=[1,2,[3,4],5]
#using shallow copy
lst2=copy.copy(lst1)
print(f"The id of lst1 :{id(lst1)} and value is {lst1}and id of lst2:{id(lst2)} and the value is {lst2}")

lst1=[1,2,[3,4],5]
#using shallow copy
lst3=copy.deepcopy(lst1)
print(f"The id of lst1 :{id(lst1)} and value is {lst1}and id of lst2:{id(lst3)} and the value is {lst3}")



# importing "copy" for copy operations
import copy
#initializing list 1
li1 = [1, 2, [3,5], 4]
#using deepcopy to deep copy
li2 = copy.deepcopy(li1)
# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 

 #adding and element to new list
li2[2][0] = 7
 
#Change is reflected in l2
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
 
#Change is NOT reflected in original list

print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")

