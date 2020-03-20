import matplotlib.pyplot as plt

a = input("A = ")
t = input("T = ")
c = input("C = ")
g = input("G = ")

d = {'A':a,'T':t,'C':c,'G':g}

plt.pie([a,t,c,g],explode=[0,0,0,0],labels=list(d),autopct='1.1f%%',shadow=True,startangle=0)
plt.axis('equal')

plt.show