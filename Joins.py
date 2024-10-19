import pandas as pd
technologies1={
    'Courses':["Spark","Pyspark","Python","Pandas"],
    'Fee':[22000,25000,23000,24000],
    'Duration':['30days','50days','55days','20days']
              }
index_labels1= ['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies1,index=index_labels1)
print(df1)

technologies2={
    'Courses':["Spark","Java","Python","Oracal"],
    'Discount':[1000,2300,1000,1200]
    }
index_labels2= ['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
print(df2)

df3=df1.join(df2,lsuffix="_Left",rsuffix="_right")
print(df3)

#''' INNER JOIN '''

df3=df1.join(df2,lsuffix="_Left",rsuffix="_right", how='inner')
print(df3)

#'''LEFT OUTER JOIN'''
df3=df1.join(df2,lsuffix="_Left",rsuffix="_right", how='left')
print(df3)

#'''RIGHT OUTER JOIN '''
df3=df1.join(df2,lsuffix="_Left",rsuffix="_right", how='right')
print(df3)


#'''pandas join in columns'''

df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')
print(df3)

df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='left')
print(df3)

df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='right')
print(df3)

#'''pandas merge DataFrame'''
import pandas as pd
technologies1={
    'Courses':["Spark","Pyspark","Python","Pandas"],
    'Fee':[22000,25000,23000,24000],
    'Duration':['30days','50days','55days','20days'],

    }
index_labels1= ['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies1,index=index_labels2)
print(df1)

technologies2={
    'Courses':["Spark","Java","Python","Oracal"],
    'Discount':[1000,2300,1000,1200]
    }
index_labels2= ['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
print(df2)

#using pandas .merge() 
df3= pd.merge(df1,df2)
print(df3)

#using DataFrame.merge()
df3= df1.merge(df2)
print(df3)

import pandas as pd
df1=pd.DataFrame({'Courses':["Spark","Pyspark","Python","Pandas"],
                 'Fee':[22000,25000,23000,24000]})

df2=pd.DataFrame({'Courses':["Pandas","Hadoop","Java","Hyperion"],
                  'Fee':[2000,21000,26000,27000]})

#'''using pandas.concat() to concat two DataFrame'''
data = [df1,df2]
df3=pd.concat(data)
print(df3)

#'''concatenate multiple DataFrame using pandas.concat()'''
import pandas as pd
df =pd.DataFrame({'Courses':["Spark","Pyspark","Python","Pandas"],
                 'Fee':[22000,25000,23000,24000]})

df1=pd.DataFrame({'Courses':["Pandas","Hadoop","Java","Hyperion"],
                  'Fee':[2000,21000,26000,27000]})

df2 = pd.DataFrame({'Duration':['30days','50days','55days','40days'],
                    'Discount':[1000,2300,1000,1200]})

df3=pd.concat([df,df1,df2])
print(df3)
