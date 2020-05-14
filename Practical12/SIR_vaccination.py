import numpy as np
import matplotlib.pyplot as plt


def var(per):
    N=10000
    I=1
    R=per*N*0.01
    S=max(N-I-R,0)
    
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
    return i

time=np.arange(101)
fig,ax=plt.subplots ()
#'''
for k in range(11):
    plt.plot(time,var(10*k),label=str(10*k)+'%')

ax.set(xlabel='time point',
         ylabel='number of people',
         title='SIR model with different vaccination rates')
ax.legend()
plt.figure(figsize=(12,8),dpi=150)
fig.savefig("SIR model with different vaccination rates.png" ,type="png")


plt.show()