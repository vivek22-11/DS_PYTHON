#CREATE DICTIONARY 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
print(capitals)

#Accessing Elements

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
print('capitals[maharashtra]:',capitals['maharashtra'])

#Adding Elements 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
capitals['west_bengal']='kolkata'
capitals

#Change Key Value 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
capitals['gujrat' ]='gandhinagar'
capitals

#Remove Elements (pop/del)

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
capitals.pop('karnataka')
capitals
del capitals['gujrat']
capitals

#Iterating Over Keys 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
for states in capitals:
        print(states,end=' , ')
for states in capitals:
        print(states,end=' , ')
        print(capitals[states])

#Values,keys and Items 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
print(capitals.values())
print(capitals.keys())
print(capitals.items())

#Membership Operator (in/ not in) 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
print('karnataka' in capitals)
print('Bihar' not in capitals)
print('Bihar'  in capitals)

#Length (len) 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
print(len(capitals))

#Dictionary can have value in tuple 

seasons={
    'summer':('feb','mar','apr','may'),
    'rainy':('june','july','august','sept'),
    'winter':('oct','nov','december','january')
    }
print(seasons['rainy'])
print(seasons['rainy'][1])
print(seasons['summer'][2])
print(seasons['winter'][2:])

#Accessing values 

capitals={
    'maharashtra':'mumbai',
    'gujrat':'ahmadbad',
    'karnataka':'banglore',
    'andhrapradesh':'hydrabad'
    }
print(capitals.get('up'))
print(capitals.get('maharashtra'))


#dictionaries cannot have two items with the key 

dict2={
       'brand':'maruti',
       'model':'breeza',
       'year':2021,
       'year':2020
       }
print(dict2)

################################ Loop #########################################

#loop through a dictionary it will show only keys
dict2={
       'brand':'maruti',
       'model':'breeza',
       'year':2020
       }

for x in dict2:
    print(x)
    
    
for x in dict2:
    print(dict2[x])


for x in dict2.values():
    print(x)

    
for x in dict2.keys():
    print(x)


for x,y in dict2.items():
    print(x,y)


################################### copy a dictionary #########################

dict2={
       'brand':'maruti',
       'model':'breeza',
       'year':2020
       }
mydict =dict2.copy()
print(mydict)


#unpacking of dictinary
friends={
    
    "Dale":9850,
    "male":6032
    
    }

contacts={
    
    "dada":8530,
    "mama":5286
    
    }
contacts.update(friends)
print(contacts)


#pipe operator
friends={"Satish":99021,
         "Ram":97603
         }
sham={"sham":85305}

all_friends=friends|sham
print(all_friends)

