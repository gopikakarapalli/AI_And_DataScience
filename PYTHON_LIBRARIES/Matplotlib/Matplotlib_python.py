'''
Matplotlib:
-----------
-> matplotlib is a plotting library used for 2D graphics in python programming languagr.
   it can be used in python scripts, shell,web application servers and other graphical
   user interface toolkits.
   like :bar graph,histogram,scatter plot,area plot,pie plot,tc..,
-> to install matplotlib:--> conda instal matplotlib  (or)
             type in cmd---> pip install matplotlib
->data visualization is the presntation of data in a pictorial or graphical format

'''
# basic code to generate a plot :

import matplotlib.pyplot as plt

#from matplotlib import pyplot as plt
#rom matplotlib import style  # if we required style in plot we can import this
#style.use("ggplot")# type of plot used (plot type)
#%matplotlib inline#use jupyter note book only

# given names in title, x & y lablel

import matplotlib.pyplot as plt

x=[1,2,3]
y=[4,5,1]
plt.plot(x,y) # PLOTTING TO OUR CANVAS or graph 

plt.title("title of plot") # it labels the title of plot 
plt.xlabel("x axis label ") # it labels the x axis of plot like time,m\s 
plt.ylabel("y axis label") # it labels the y axis of plot like time,v, m\s
plt.show()# showing a plotted popup
#-------------------------------------------------------------------------
# given colours & style to the ploat, x & y lablel

import matplotlib.pyplot as plt
from matplotlib import style  # if we required style in plot we can import this

style.use("ggplot")# type of plot used (plot type)

x=[0,2,3]
y=[0,5,1]
x1=[0,7,8]
y1=[0,3,4]

plt.plot(x,y,color='g',label="No load",linewidth=10)# giveing colous to the plot 
# (x axis,y axis,color of plot,lable of plot,line width of plot)  
plt.plot(x1,y1,'c',label="full load",linewidth=3)

plt.legend() # it show the plot lable wrt color at right side of the top
plt.title("no load vs full load ")  
plt.xlabel("current(A)")  
plt.ylabel("voltage(Kv)")
plt.grid(True,color='k') # it show the grid line in plot (turn no\off by True\false,color of grid)

plt.show()

#--------------------------------------------------------------------------------

#geting differnt type of plot

# bar graph

import matplotlib.pyplot as plt

plt.bar([1,2,3],[4,5,1],color='r',label='bar 1') # showing bar graph type plot 

plt.title('bar graph')
plt.show()

# histogram graph :mostly used for inc\dec
x=[22,55,62,45,21,34,42,99,102,110,66,77,88,89,99,111,120,4,5,6,10,50,3,6,78,8,9,0]
y=[00,10,20,30,40,50]

plt.hist(x,y,histtype= 'bar',rwidth=0.5) # showing histogram graph type plot 

plt.title('histogram graph')
plt.show()

#scatter plot: mostly used for comparetion of two var ie.co relation
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,6]

plt.scatter(x,y,label='scatter plot',color='k',s=20,marker="o")# showing scatter plot
##                   ( s is size of marker ,marker='requir symble'       
plt.title('scatter plot')
plt.show()

# stack plot
days = [1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=10)
plt.plot([],[],color='r',label='working',linewidth=12)
plt.plot([],[],color='k',label='playing',linewidth=15)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])#showing STACK plot 

plt.title('stsck plot,or area plot')
plt.legend()
plt.show()

# pie chart:

slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
areaColors=['c','m','r','b']

plt.pie(slices,
          labels=activities,
          colors=areaColors,
          startangle=90,
          shadow=True,
          explode=(0,0.1,0,0),
          autopct='%1.1f%%') #shows % valve

plt.title('pie plot')

plt.show()

# working with multiple plots
import numpy as np
import matplotlib.pyplot as plt

def f(t):
        plt.title('woring with multiple plots')
        return np.exp(-t)*np.cos(2*np.pi*t)
t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)


plt.subplot(211) #cerate sub plot(211=> colum 2 plot row 1 plot and it is 1st plot)
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212 )#cerate sub plot(212=> colum 2 plot row 1 plot and it is 2nd plot)
plt.plot(t2,np.cos(2*np.pi*t2))

plt.title('sub plots')
plt.show()



