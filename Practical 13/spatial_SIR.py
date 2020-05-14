import numpy as np
import matplotlib.pyplot as plt

N=10000
S=9999
I=1
R=0

beta=0.3
gamma=0.05
  
population=np.zeros((102,102))#consder the edges as the recovered
warn=np.zeros((102,102))


def badnews(x,y):
    for X in range(x-1,x+2):
        for Y in range(y-1,y+2):
            if X!=x or Y!=y:
                warn[X,Y]+=1

def goodnews(x,y):
    for X in range(x-1,x+2):
        for Y in range(y-1,y+2):
            if X!=x or Y!=y:
                warn[X,Y]-=1

for k in range(102):
    population[0,k]=2
    population[101,k]=2
    population[k,0]=2
    population[k,101]=2
                
first=np.random.choice(range(100),2)
population[first[0],first[1]]=1
badnews(first[0],first[1])

plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

for i in range(1000):
#inflect
    index0=np.where((population==0)&(warn>0))
    for k in range(len(index0[0])):
        x=index0[0][k]
        y=index0[1][k]
        beta_=beta*warn[x,y]/8
        population[x,y]=np.random.choice(range(2),1,[1-beta_,beta_])
        if population[x,y]==1:
            badnews(x,y)

#recure
    index1=np.where(population==1)
    for k in range(len(index1[0])):
        x=index1[0][k]
        y=index1[1][k]
        population[x,y]=np.random.choice(range(1,3),1,[1-gamma,gamma])
        if population[x,y]==2:
            goodnews(x,y)


    if i==10 or i==50 or i==99:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')