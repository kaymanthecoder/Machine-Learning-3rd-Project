import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import csv
import math

#Import dataset
dataset = ""

xax = "" #x-axises of that dataset file
yax = ""#y-axises of that dataset file
filechoice = input("Which file do you want to use?\n1)data2008\n2)data1953\n3)databoth")
if(filechoice == "1"):
    xax = "BirthRate(Per1000 - 2008)"
    yax = "LifeExpectancy(2008)"
    dataset = pd.read_csv('data2008.csv')
elif(filechoice == "2"):
    xax = "BirthRate(Per1000 - 1953)"
    yax = "LifeExpectancy(1953)"
    dataset = pd.read_csv('data1953.csv')
elif(filechoice == "3"):
    xax = "BirthRate(Per1000)"
    yax = "LifeExpectancy"
    dataset = pd.read_csv('databoth.csv')

X = dataset.iloc[:,[1,2]].values#only want 2 columns

#Fitting hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)#predict points

fig= plt.subplot()#plot points

my_scatter_plot = fig.scatter(#The columns we want to see
    dataset[xax],
    dataset[yax]
    )#The reason why is this was below scatters only the outline would have the color, because that color is behind

#ploting the clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 50, c= 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 50, c= 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 50, c= 'green', label = 'Cluster 3')

#I am getting the points from each cluster
#The np.split function is used to turn this list into an array so that in the while loops I can look for specific values
cluster1X = str(np.split(X[y_hc == 0, 0], 1))
cluster1Y = str(np.split(X[y_hc == 0, 1], 1))

cluster2X = str(np.split(X[y_hc == 1, 0], 1))
cluster2Y = str(np.split(X[y_hc == 1, 1], 1))

cluster3X = str(np.split(X[y_hc == 2, 0], 1))
cluster3Y = str(np.split(X[y_hc == 2, 1], 1))

num = dataset[xax].count()-1 #there is "-1" because when I run it, it complains about being out of range
country = dataset["Countries"]#We want the countries to be displayed in the while loops
birth = dataset[xax] #putting all the x-axises here
life = dataset[yax] #putting all the x-axises here

#each of these are keeping track of the number of countries in each cluster
clus1 = 0
clus2 = 0
clus3 = 0

#These are groups by each cluster
Ltot1 = 0 #total of Life expentancy
Btot1 = 0 #total of Birth rate
Lmean1 = 0 #mean of Life expentancy
Bmean1 = 0 #mean of Birth rate

#Same applys for the next 2
Ltot2 = 0
Btot2 = 0
Lmean2 = 0
Bmean2 = 0

Ltot3 = 0
Btot3 = 0
Lmean3 = 0
Bmean3 = 0

#These 2 are used to calculate euclidean distance
a = 0 #keeps track of row in csv
a2 = 1 #keeps track of 1 row ahead

#Same applys to the next 2
b = 0
b2 = 1

c = 0
c2 = 1

#the distances of each cluster
dis1 = 0
dis2 = 0
dis3 = 0

#Explaining how this works:
#birth[a] gets the values of birth rate than it is used to be found in cluster1X the x-axises of birth rate
#life[a] gets the values of life expentancy it is used to be found in cluster1Y the y_axises of life expentancy
#So.....if a country has both the points it is placed in that specific cluster

print("\nCluster 1\n")
for a in range(num):
        while(str(birth[a]) in str(cluster1X) and str(life[a]) in str(cluster1Y)):
                print(str(country[a])+" is in cluster 1")
                
                Ltot1 = Ltot1 + life[a] #adding total for Life Expentancy
                Btot1 = Btot1 + birth[a] # adding total for Birth Rate
            
                dis1 = dis1 + math.sqrt((birth[a2]-birth[a])**2+(life[a2]-life[a])**2) #Calculating euclidean distance
                print("The sum of the distance between the points is " + str(dis1))
                clus1 = clus1 + 1
                a = a + 1
                a2 = a2 + 1
                
Lmean1 = Ltot1/clus1
Bmean1 = Btot1/clus1    
print("There are " + str(clus1) + " countries in this cluster 1")
print("The mean of cluster1 Birthrate is " + str(Bmean1) + " and Life Expentancy is " + str(Lmean1))


print("\nCluster 2\n")
for b in range(num):
        while(str(birth[b]) in str(cluster2X) and str(life[b]) in str(cluster2Y)):
                print(str(country[b])+" is in cluster 2")
    
                Ltot2 = Ltot2  + life[b] #adding total for Life Expentancy
                Btot2 = Btot2 + birth[b] # adding total for Birth Rate

                dis2 = dis2 + math.sqrt((birth[b2]-birth[b])**2+(life[b2]-life[b])**2) #Calculating euclidean distance
                print("The sum of the distance between the points is " + str(dis2))
                clus2 = clus2 + 1
                b = b + 1
                b2 = b2 + 1


Lmean2 = Ltot2/clus2
Bmean2 = Btot2/clus2    
print("There are " + str(clus2) + " countries in this cluster 2")
print("The mean of cluster1 Birthrate is " + str(Bmean2) + " and Life Expentancy is " + str(Lmean2))

print("\nCluster 3\n")
for c in range(num):
        while(str(birth[c]) in str(cluster3X) and str(life[c]) in str(cluster3Y)):
              print(str(country[c])+" is in cluster 3")
              
              Ltot3 = Ltot3 + life[c] #adding total for Life Expentancy
              Btot3 = Btot3 + birth[c] # adding total for Birth Rate

              dis3 = dis3 + math.sqrt((birth[c2]-birth[c])**2+(life[c2]-life[c])**2) #Calculating euclidean distance
              print("The sum of the distance between the points is " + str(dis3))

              clus3 = clus3 + 1
              c = c + 1
              c2 = c2 + 1

Lmean3 = Ltot3/clus3
Bmean3 = Btot3/clus3    
print("There are " + str(clus3) + " countries in this cluster 3")
print("The mean of cluster1 Birthrate is " + str(Bmean3) + " and Life Expentancy is " + str(Lmean3))

plt.title('Clusters of Life') #label title
plt.xlabel('Birth Rate') #label x-axis
plt.ylabel('Life Expectancy') #label y-axis
plt.legend() #label legends

plt.show()
