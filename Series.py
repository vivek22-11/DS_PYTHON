''' as series is used to model one dimenstional data
similar to a list in python
the series object also has a few more bits
of data ,including an index and a row
'''

import pandas as pd
songs2= pd.Series([145,142,38,13],name='counts')
songs2.index
print(songs2)
#it is easy to inspect the index of a series (or data frame)
# the index can be string based as well
#in which case pandas indicates
#that the DataType for the index is object(not string):

songs3=pd.Series([145,142,38,13],name='counts',
                 index=['paul','john','george','ringo'])
songs3.index
print(songs3)


#'''load data from a csv file'''

import pandas as pd
f1= pd.read_csv("C:\Data Science\age.csv")
print(f1)


'''the pandas series data structure provides support for the basic 
crud operations-create,read,update,delete'''


#'''CREATE'''
import pandas as pd
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],
name='george songs')
print(george)

#'''READ'''
george['1968']

print(george['1970'])

#'''UPDATE'''
for item in george:
     print(item)
george['1969']=68
george['1969']
print(george)

#'''DELETE'''
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
print(s)

del george['1968']
print(george)

#'''convert types'''

import pandas as pd
songs_66=pd.Series([3,None,11,9],
index=['paul','john','george','ringo'],
name='Counts')
pd.to_numeric(songs_66.apply(str))

pd.to_numeric(songs_66.apply(str), errors='coerce')

songs_66.fillna(-1)

songs_66.dropna()

#'''appending,combaining and joining two series'''
songs_69 = pd.Series([7,16,21,39],
index=['Rohit','Sanket','Sarthak','Darshan'],
name='Counts')
songs=songs_66.append(songs_69)

songs=pd.concat([songs_66,songs_69])

#'''plotting two series'''

import matplotlib.pyplot as plt
fig=plt.figure()
songs_69.plot()
plt.legend()


import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='k',alpha=.5)
plt.legend()



import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='b',alpha=.5)
plt.legend() 



import numpy as np
import matplotlib.pyplot as plt
data=pd.Series(np.random.randn(500),
               name='500 random')
fig = plt.figure()
ax=fig.add_subplot(111)
data.hist()     