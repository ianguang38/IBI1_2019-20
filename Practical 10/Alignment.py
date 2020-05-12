#translate the matrix souce into readable dictionary
#methods refer to some answers in the Internet
mf=open('BLOSUM62','r')
lines=mf.read().strip().split('\n')
head=lines.pop(0).split()
matrix={}
for raws in lines:
    raw=raws.strip().split()
    raw_name=raw.pop(0)
    matrix[raw_name]={}
    for entries in head:
        matrix[raw_name][entries]=raw.pop(0)
mf.close()

s1=open('SOD2_human.fa','r')
s2=open('SOD2_mouse.fa','r')
s3=open('RandomSeq.fa','r')
name=[]
seq=[]
name.append(s1.readline().rstrip())
seq.append(s1.readline().rstrip())
name.append(s2.readline().rstrip())
seq.append(s2.readline().rstrip())
name.append(s3.readline().rstrip())
seq.append(s3.readline().rstrip())
s1.close()
s2.close()
s3.close()

ed=open('output.txt','w')
def w(line):
    ed.write(str(line))
    ed.write('\n')

def implement(x,y):
    score=0
    alignment=''
    if len(seq[x])>len(seq[y]):
        a=seq[x]
        b=seq[y]
    else:
        a=seq[y]
        b=seq[x]
    for k in range(len(a)-len(b)):
        b[k+len(b)]='*'
    for i in range(len(a)):
        tep=int(matrix[a[i]][b[i]])
        score+=tep
        if a[i]==b[i]:
            alignment+=a[i]
        elif tep>=0:
            alignment+='+'
        else:
            alignment+=' '
    ed.write(name[x])
    ed.write(' and ')
    w(name[y])
    w(a)
    w(alignment)
    w(b)
    ed.write('Score:')
    w(score)
    w('\n')

implement(0,1)
implement(0,2)
implement(1,2)

print('success!')
ed.close()

print('''
As the score will grow with the number of amino acids, it should divided by the number.
There are two number for a pairwise, i think the longer one should be used in the calculation.
''')