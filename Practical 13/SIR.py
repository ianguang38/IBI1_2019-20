import numpy as np
import matplotlib.pyplot as plt

N=10000
S=9999
I=1
R=0

beta=0.3
gamma=0.05

s=np.array([S],dtype='i2')
i=np.array([I],dtype='i2')
r=np.array([R],dtype='i2')


for j in range(100):
    beta_=beta*i[j]/N
    ss=np.random.choice(range(2),s[j],[1-beta_,beta_]).sum()
    s=np.append(s,s[j]-ss)
    rr=np.random.choice(range(2),i[j],[1-gamma,gamma]).sum()
    r=np.append(r,r[j]+rr)
    i=np.append(i,N-s[j+1]-r[j+1])

time=np.arange(101)


fig,ax=plt.subplots ()

plt.plot(time,s,label='Suscepetiable')
plt.plot(time,i,label='Inflected')
plt.plot(time,r,label='Recoverd')


ax.set(xlabel='time point',
         ylabel='number of people',
         title='SIR model')
ax.legend()
plt.figure(figsize=(6,4),dpi=150)
fig.savefig("SIR model.png" ,type="png")


plt.show()