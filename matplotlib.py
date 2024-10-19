import matplotlib.pyplot as plt
plt.plot([1,3,2,8,4])
plt.show()

#multiline plots
import matplotlib.pyplot as plt
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3 for xi in x])
plt.plot(x,[xi/3.0 for xi in x])
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.axis()
plt.axis([0,5,-1,13])
plt.show()


#how to add lable in graph
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel("this is the x aixs")
plt.ylabel("this is the y aixs")
plt.show()


import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('Simple plot')
plt.show()


#giving names to plots
import matplotlib.pyplot as plt
import numpy as np
x= np.arange(1,5)
plt.plot(x,x*1.5,label='Normal')
plt.plot(x,x*3.0,label='Fast')
plt.plot(x,x/3.0,label='Slow')
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y= np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show() 


import matplotlib.pyplot as plt
import numpy as np
y= np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()


#changing style of graph
import matplotlib.pyplot as plt
import numpy as np
y= np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y= np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'y',y+1,'D',y+1.5);
plt.show()


#adding label as wel, as title
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5])
plt.title('simple plot')
plt.xlabel('this is x axis')
plt.ylabel('this is y axis')
plt.show()


#giving colours
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,5])
plt.plot(y,'y')
plt.plot(y+1,'b')
plt.plot(y+2,'c')
plt.show()


#changing colours
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,3])
plt.plot(y,'y',y+1,'r',y+2,'c');
plt.show()


#styles of line ...doted,slash dot line,slash line
import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,3])
plt.plot(y,'*',y+1,'o',y+2,'D');
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y)
plt.show()


import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,4,1]);
plt.show()


#scatterd graph
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()


#change colour of scatter graph
size=50*np.random.randn(1000)
colours=np.random.randn(1000)
plt.scatter(x,y,s=size,c=colours);


#drow some text inside graph
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-4,4,1024)
y=.25*(x+4.)*(x+1.)*(x-2.)
plt.text(-0.5,-0.25,'helooooo')
plt.plot(x,y,c='b')
plt.show()


#seaborn 
#pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
df.head()

sns.countplot(x='sex',data=df)
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')

sns.kdeplot(x='age',data=df,color='black')
sns.displot(x='age',kde=True,bins=5,data=df)
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette='Set1',data=df)


df=sns.load_dataset('iris')
df.head()
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

sns.pairplot(df)

corr=df.corr()
sns.heatmap(corr)



from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cars =pd.read_csv("C:\Data Science\cars.csv")
cars.columns
cars.describe()
plt.hist(cars.speed)

sns.displot(x = 'speed',kde=True,bins=6,data =cars )

sns.displot(x = 'dist',kde=True,bins=6,data =cars)

cars.describe()
sns.boxplot(cars.speed)

plt.hist(cars.dist)
sns.boxplot(cars.dist)

speed =cars['speed'].tolist()
print(speed)
print("skewness of speed",skew(speed))
dist=cars['dist'].tolist()
print(dist)
print("skewness of dist",skew(dist))

print(skew(dist, axis=0, bias =True))

print(kurtosis(dist,axis=0,bias =True))


#join plot
sns.jointplot(x='speed',y='dist',data=cars,kind='reg')
sns.jointplot(x='speed',y='dist',data=cars,kind='hist')
sns.jointplot(x='spees',y='dist',data=cars,kind='kde')


#kde plot
sns.kdeplot(x='dist',data=cars,color='black')
sns.kdeplot(x='speed',data=cars,color='red') 


#distribution plot
sns.displot(x='dist',kde=True,bins=5,data=cars)


#scatterplot
sns.scatterplot(x='speed',y='dist',data=cars,hue='speed')


#count plot
sns.countplot(x='speed',data=cars)


#bar graph
plt.bar(speed,dist)

#heat map
corr =cars.corr()
sns.heatmap(corr)

#pair plot
sns.pairplot(cars)

#create iris dataset 

from scipy.stats import skew
from scipy.stats import kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
IRIS =pd.read_csv("C:\Data Science\IRIS.csv")
IRIS.columns
IRIS.describe()
plt.hist(IRIS.sepal_length)

sns.displot(x = 'sepal_length',kde=True,bins=6,data =IRIS )
sns.displot(x = 'petal_width',kde=True,bins=6,data =IRIS)

IRIS.describe()
sns.boxplot(IRIS.sepal_length)

plt.hist(IRIS.petal_width)
sns.boxplot(IRIS.petal_width)

sepal_length =IRIS['sepal_length'].tolist()
sepal_length
print("skewness of sepal_length",skew(sepal_length))

petal_width=IRIS['petal_width'].tolist()
petal_width
print("skewness of petal_width",skew(petal_width))

print(skew(petal_width, axis=0, bias =True))

print(kurtosis(petal_width,axis=0,bias =True))



import matplotlib.pyplot as plt
x=range(1,50)
y=[value *3 for value in x]
print("value of x:")
print(*range(1,50))
print("values of y(thrice of x )")
print(y)
#plot lines and/or markes to the axes
plt.plot(x,y)
#set x axis lable of the cureent axis
plt.xlabel('x-axis')
#set y axis lable of the current axis
plt.ylabel('y-axis')
#set the title
plt.title('Draw a line')
#display the figure
plt.show()


import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
#set x axis lable of the cureent axis
plt.xlabel('x-axis')
#set y axis lable of the current axis
plt.ylabel('y-axis')
#set the title
plt.title('Sample graph!')
#display the figure
plt.show()



import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:\\Data Science\\fdata.csv")
df.plot()
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('C:\\Data Science\\Attendance.csv')
df.plot()
plt.show()


import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]
x2=[10,20,30]
y2=[40,10,30]
#set x axis lable of the current axis
plt.xlabel('x -axis')
#set y axis lable of the current axis
plt.ylabel('y -axis')
#set the title
plt.title('Two or more lines with different widths and colors with suitable legends')
plt.plot(x1,y1, color='blue', linewidth=3, label='line1-width-3')
plt.plot(x2,y2, color='red', linewidth=5, label='line2-width-5')
plt.legend()
plt.show()


import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[20,40,10]
x2=[10,20,30]
y2=[40,10,30]
#set x axis lable of the current axis
plt.xlabel('x -axis')
#set y axis lable of the current axis
plt.ylabel('y -axis')
#set the title
plt.title('Two or more lines with different widths and colors with suitable legends')
plt.plot(x1,y1, color='blue', linewidth=3, label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red', linewidth=5, label='line2-dashed',linestyle='dashed')
plt.legend()
plt.show() 


import matplotlib.pyplot as plt
x=[1,4,5,6,7]
y=[2,6,3,6,3]
#plotting the points
plt.plot(x,y, color='red', linestyle='dashdot',linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)
#set the y-limits of the current axes
plt.ylim(1,8)
#set the x-limit of the current axes
plt.xlim(1,8)
#set x axis lable of the current axis
plt.xlabel('x -axis')
#set y axis lable of the current axis
plt.ylabel('y -axis')
plt.title('Display markers')
plt.show()


#write a python program to plot several lines with different format styles in one command
import numpy as np 
import matplotlib.pyplot as plt
#Sample time at 200ms intervals
t=np.arange(0.,5.,0.2)
#green dashes, blue squares and red  triangles
plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
plt.show()


#write a python programing to display  a bar chart of the popularity of programing languases
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("popularity of programing languages\n" + "worlwide,oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
plt.show()


#write a python programing to display  a horizontal bar chart of the popularity of programing languases
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("popularity of programing languages\n" + "worlwide,oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
plt.show()


import numpy as np 
import matplotlib.pyplot as plt
n_groups = 5 
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)
fig, ax = plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8
rects1=plt.bar(index,men_means,bar_width,alpha=opacity,color='g',label='men')
rects1=plt.bar(index + bar_width,women_means,bar_width,alpha=opacity,color='r',label='women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width,('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()
