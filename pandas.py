'''What is Pandas DataFrame?
pandas DataFrame is a Two-Dimensional data structure,
an immutable, heterogeneous tabular 
data structure with labeled axes rows, and columns.


Installing Pandas
step-1 go to anaconda navigator
step-2 select environment tab
step-3 by default it will be base terminal
step-4 on base terminal-pip install pandas or conda install pandas

'''



#To check the version of pandas
import pandas as pd
pd.__version__

#Create using Constructor
#DataFrame of list
import pandas as pd
technologies = [ 
    ["Spark",10000, "30days"], 
    ["pandas",20000, "40days"] 
               ]
df=pd.DataFrame(technologies)
print(df)
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
df1=df.dtypes 
print(df1)


#dataframe using dictionary
import pandas as pd
technologies={
    'Courses':["Spark","Pyspark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[10000,20000,30000,40000,50000,60000,70000],
    'Duration':['1days','2days','3days','4days','5days','6days','7days'],
    'Discount':[1.1,1.2,1.3,1.4,1.5,1.6,1.7]
    }
df=pd.DataFrame(technologies)
print(df)


#''' drop column'''
df2=df.drop(["Fee"],axis = 1)
print(df2)


#''' Explicitly using parameter name 'labels' '''
df2=df.drop(labels=["Fee"],axis = 1)
print(df2)


df2=df.drop(columns=["Fee"],axis = 1)
print(df2)


#''' using index'''
print(df.drop(df.columns[1],axis =1))
df=pd.DataFrame(technologies)


#'''using inplace+True'''
df.drop(df.columns[2],axis =1,inplace=True)
print(df)


#'''drop two or more columns by label name'''
df=pd.DataFrame(technologies)
df2=df.drop(["Courses","Fee"],axis=1)
print(df2)


#'''drop two or more columns by index'''
df=pd.DataFrame(technologies)
df2 = df.drop(df.columns[[0,1]],axis = 1)
print(df2)

#'''drop columns from list of columns'''
df=pd.DataFrame(technologies)
lisCol=["Courses","Fee"]
df2=df.drop(lisCol,axis=1)
print(df2)

#'''Remove columns from dataframe inplace'''
df.drop(df.columns[1],axis=1,inplace=True)
print(df)

###############################################################################

#'''pandas select rows by index (position/lable)'''

import pandas as pd
import numpy as np
technologies={
    'Courses':["Spark","Pyspark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies ,index=row_labels)
print(df)

''' 
use the slicing operator to get DataFrame
slicing specific rows and columns using iloc attribute
Syntax=df.iloc[startrow:endrow,startcolumn:endcolumn]

'''

df=pd.DataFrame(technologies ,index=row_labels)
df2=df.iloc[:,0:2]
print(df)



df2 = df.iloc[0:2,:]
print(df2)


df3 = df.iloc[1:2,1:3]
print(df3)

df3 = df.iloc[:,1:3]
print(df3)


#'''select row by index'''

df2 = df.iloc[2]
print(df2)

df2 = df.iloc[[2,3,6]]  
print(df2)

df2 = df.iloc[1:5]      
print(df2)

df2 = df.iloc[:1]       
print(df2)

df2 = df.iloc[:3]
print(df2)

df2 = df.iloc[-1:]      
print(df2)

df2 = df.iloc[-3:]      
print(df2)

df2 = df.iloc[::2]      
print(df2)

#'''select rows by index lables'''

df2=df.loc['r2']           
print(df2)

df2=df.loc['r2','r3','r6']  
print(df2)

df2=df.loc['r1':'r5']      
print(df2)

df2=df.loc['r1':'r5':2]    
print(df2)

#'''pandas select columns by name or index by using df[] notation'''

df2=df['Courses']
print(df2)


df2 = df[["Courses","Fee","Duration"]]
print(df2)


'''
using loc[] to take column slices.
loc[] syntax to slice columns df.loc[:,start:stop:step]
selecte multiple columns
'''

df2=df.loc[:,["Courses","Fee","Duration"]]
print(df2)

#select random columns
df2=df.loc[:,["Courses","Fee","Discount"]]
print(df2)

#select columns between two columns
df2=df.loc[:,"Fee":"Discount"]
print(df2)

#select column by range
df2=df.loc[:,"Duration":]
print(df2)

#select columns by range.all the colunms upto "Duration"
df2=df.loc[:,:"Duration"]
print(df2)

#select every alternative columns
df2=df.loc[:,::2]
print(df2)


#'''pandas.DataFrame.query()'''

df2 = df.query("Courses == 'Spark'")
print(df2)


df2 = df.query("Courses != 'Spark'")
print(df2)


###############################################################################

'''pandas add columns to DataFrame'''
import pandas as pd
import numpy as np
technologies={
    'Courses':["spark","Pyspark","Hadoop","python","pandas"],
    'Fee':[22000,25000,23000,24000,26000],
    'Discount':[1000,2300,1000,1200,2500]
    }

df=pd.DataFrame(technologies)
print(df)

# pandas add columns to DataFrame
#add new column to the DataFrame
tutors = ['Rohit','Sarthak','Sanket','Darshan','Shubham']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)

#add multiple columns to the DataFrame
MNCCompanies = ['TATA','HCL','INFOSYS','GOOGLE','AMAZON']
df2= df.assign(MNCComp = MNCCompanies, TutorsAssigned=tutors )
print(df2)


#'''derive new column from existing column'''
df = pd.DataFrame(technologies)
df2 = df.assign(Discount_Percent= lambda x: x.Fee *x.Discount /100)
print(df2)


#'''add new columns to the existing DataFrame'''
df = pd.DataFrame(technologies)
df["MNCCompanies"] = MNCCompanies
print(df)


#'''Add new column at the specific position'''
df = pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)

###############################################################################

import pandas as pd
technologies={
    'Courses':["spark","Pyspark","Hadoop","python","pandas","oracal","java"],
    'Fee':[22000,25000,23000,24000,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','50days'],
    }
df = pd.DataFrame(technologies)
df.columns
print(df.columns)


#'''Pandas rename column name'''
df2 = df.rename(columns = {'Courses':'Courses_list'})
print(df2.columns)
print(df2)

#the above statement by using 
#axis=1 or axis='columns'
#alternatively you can write above using  axis
df2 = df.rename( {'Courses':'Courses_list'},axis=1)
print(df2)

df2 = df.rename( {'Duration':'Time'},axis='columns')
print(df2)


#in order to change on the existing DataFrame
#without copying to the new DataFrame
#you have to use inplace=True
#replace existing DataFrame (inplace) this return none.
df.rename({'Courses':'Courses_list'},axis='columns',inplace=True)
print(df.columns)
print(df)


#'''get the number of rows in dataframe'''
rows_count = len(df.index)
print(rows_count)

rows_count = len(df.axes[0])
print(rows_count)

#'''return number of rows and columns'''
df=pd.DataFrame(technologies)
row_count = df.shape[0]   
col_count = df.shape[1]   
print(row_count)
print(col_count)


###############################################################################

'''pandas DataFrame.apply() to apply function add columns'''

import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df= pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3 
df2= df.apply(add_3)
print(df2)

#''' apply function single column'''
def add_4(x):
    return x+ 4 
df["B"]=df["B"].apply(add_4)
print(df["B"])
print(df)

#'''apply to multiple columns'''

df[['A','B']] = df[['A','B']].apply(add_3)
print(df)


#'''apply a lambda function to each column'''

df2= df.apply(lambda x:x+10)
print(df2)


#'''apply lambda function to single column'''

df["A"] = df["A"].apply(lambda x: x-2)
print(df)


#'''using DataFrame.transform()'''
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)

#'''using pandas.DataFrame.map() to single columns'''
df['A'] = df['A'].map(lambda A: A/2)
print(df)

'''
using NUmpy function on sigle column.
using DataFrame.apply() & [] operator
'''
import numpy as np
df['A'] = df['A'].apply(np.square)
print(df)

#'''using numpy.square() and [] operator'''

df['A'] = np.square(df['A'])
print(df)


import pandas as pd
import numpy as np
data = [(3,5,7), (2,4,6),(5,8,9)]
df = pd.DataFrame(data, columns = ['A','B','C'])
print(df)


def add_3(x):
   return x+3
df2 = df.apply(add_3)
print(df2)
#Using apply function single column
def add_4(x):
   return x+4
df["B"] = df["B"].apply(add_4)
df["B"]
#Apply to multiple columns
df[['A','B']] = df[['A','B']].apply(add_3)
#apply a lambda function to each column
df2 = df.apply(lambda x : x + 10)
# apply() function on selected list of multiple columns
df = pd.DataFrame(data, columns = ['A','B','C'])
df[['A','B']] = df[['A','B']].apply(add_3)
print(df)
#Apply Lambda Function to Each Column
df2 = df.apply(lambda x : x + 10)
print(df2)
#Using Dataframe.apply() and lambda function
df["A"] = df["A"].apply(lambda x: x-2)
print(df)
#Using pandas.DataFrame.transform() to Apply Function Column
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)
#Using pandas.DataFrame.map() to Single Column
df['A'] = df['A'].map(lambda A: A/2.)
print(df)
# Using Dataframe.apply() & [] operator
df['A'] = df['A'].apply(np.square)
print(df)
#Using numpy.square() and [] operator
df['A'] = np.square(df['A'])
print(df)




import pandas as pd
technologies={
    'Courses':["Spark","Pyspark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
    }
df = pd.DataFrame(technologies)
print(df)

#'''use groupby() to compute the sum'''
df2 = df.groupby(['Courses']).sum()
print(df2)


#'''group by multiple columns'''
df2 = df.groupby(['Courses','Duration']).sum()
print(df2)

#'''add row index to the group by result'''
df2= df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)


#'''pandas get column names from DataFrame'''
import pandas as pd
import numpy as np
technologies={
    'Courses':["spark","pyspark","hadoop","python","pandas"],
    'Fee':[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','55days','40days','60days'],
    'Discount':[1000,2300,1000,1200,2500]
    }
df = pd.DataFrame(technologies)
print(df)
print(df.columns)   

#'''get the list of all columns names from header'''
column_headers = list(df.columns.values)
print("The Column Header : ",column_headers)

#using list(df) to get the column headers as a list
column_headers = list(df.columns)
print(column_headers )

#using list (df) to get the list of all column names
column_headers = list(df)
print(column_headers) 


import pandas as pd
technologies={
    'Courses':["Spark","Pyspark","Hadoop","Python","Pandas","Oracal","Java"],
    'Fee':[22000,25000,23000,24000,26000,27000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','40days'],
    'Discount':[1000,2300,1000,1200,2500,1400,1600]
    }
df = pd.DataFrame(technologies)
print(df)


#'''shuffle the DataFrame rows & return all rows'''
df1 = df.sample(frac = 1)
print(df1)

#'''creating new index starting from zero'''
df1 = df.sample(frac = 1).reset_index()
print(df1)

#'''drop shuffle index'''
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)



# Create DataFrame with None/Null to work with examples
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)
df1=df.shape
print(df1)
df1=df.size
print(df1)
df1=df.columns
print(df1)
df1=df.columns.values
print(df1)
df1=df.index
print(df1)
df1=df.dtypes
print(df1)
#Accessing one column contents
df['Fee']
##Accessing two columns contents
df[['Fee','Duration']]
#select certain rows and assign it to another dataframe
df2=df[6:]
print(df2)
#accessing certain cell from column 'Duration'
df['Duration'][3]
#subtracting specific value from a column
df['Fee'] = df['Fee'] - 500
df['Fee']
# Describe DataFrame for all numberic columns
df.describe()
#rename() – Renames pandas DataFrame columns
df = pd.DataFrame(technologies, index=row_labels)
# Assign new header by setting new column names.
df.columns=['A','B','C','D']
print(df)
# Rename Column Names using rename() method
df = pd.DataFrame(technologies, index=row_labels)
df.columns=['A','B','C','D']
df2 = df.rename({'A': 'c1', 'B': 'c2'}, axis=1)
df2 = df.rename({'C': 'c3', 'D': 'c4'}, axis='columns')
df2 = df.rename(columns={'A': 'c1', 'B': 'c2'})
#Drop DataFrame Rows and Columns
df = pd.DataFrame(technologies, index=row_labels)
# Drop rows by labels
df1 = df.drop(['r1','r2'])
print(df1)
# Delete Rows by position/index
df1=df.drop(df.index[1])
print(df1)
df1=df.drop(df.index[[1,3]])
print(df1)
# Delete Rows by Index Range
df1=df.drop(df.index[2:])
df = pd.DataFrame(technologies)
df1 = df.drop(0)
print(df1)
df = pd.DataFrame(technologies)
df1 = df.drop([0, 3])
df1 = df.drop(range(0,2))

###############################################################################

#Reading data in various format

import pandas as pd
f1=pd.read_csv('c:/Data Science/buzzers.csv')


import os
with open('buzzers.csv') as raw_data:
    print(raw_data.read())

    
#Reading CSV data as lists

import csv
with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)

#Reading CSV data as  Dictionaries

import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)


import csv
with open('buzzers.csv') as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights
   


#'''write DataFrame to CSV file with Default params'''

df.to_csv("C:\Data Science\courses.csv")

#'''read CSV file into DataFrame'''

import pandas as pd
df=pd.read_csv('courses.csv')
print(df)


#'''write DataFrame to Excel File'''
df.to_excel("C:\Data Science\courses.xlsx")

#'''read Excel file'''
import pandas as pd
df=pd.read_excel("C:\Data Science\courses.xlsx")
print(df)


# Create DataFrame from Dictionary
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df = pd.DataFrame(technologies)
df
#convert dataframe to csv
df.to_csv('data_file.csv')
#Create DataFrame From CSV File
df = pd.read_csv('data_file.csv')
