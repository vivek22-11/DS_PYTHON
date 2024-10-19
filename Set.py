
#CREATE SET 

basket= {'apple','orange','apple','pear','orange','banana'}
print(basket)

#Accessing Elements 

basket= {'apple','orange','apple','pear','orange','banana'}
for item in basket:
    print(item)

#Adding Elements (add/update)

basket= {'apple','orange','pear','banana'}
basket.add('apricot')
print(basket)

#add more elements
basket= {'apple','orange','pear','banana'}
basket.update(['apricot','mango','grapefruit'])
print(basket)

#Length

basket= {'apple','orange','apple','pear','orange','banana'}
print(len(basket))

#MAX/MIN

basket2={23,45,67,12,456}
print(max(basket2))
print(min(basket2))

#Remove Elements (remove/discard)

basket= {'apple','orange','apple','pear','orange','banana','apricot'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket)

#Set Operations(Union/Intersection/Difference)

s1={'apple','orange','pear','banana'}
s2={'apricot','mango','grapefruit','banana'}
print('Union:',s1|s2)
print('Intersection:', s1 & s2)
print('Difference:',s1 - s2)
print('Difference:',s2 - s1)