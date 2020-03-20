import matplotlib.pyplot as plt

print("input the length of the gene and press enter")
l=[]
for i in range(5):
    a = input()
    l.append(int(a))

#remove the longest and shortese
l.sort(key=None,reverse=False)
print(l)
l.pop()
l.reverse()
l.pop()

plt.boxplot(l,
            vert=True,
            whis=2,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.show()