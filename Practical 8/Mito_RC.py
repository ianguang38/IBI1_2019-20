def RC(s):
    bp={'A':'T','T':'A','C':'G','G':'C','\n':'\n'}
    bp.setdefault('','\n')
    l = len(s)
    rev=''
    for i in range(l):
        rev += bp[s[l-i-1]]
    return rev


inp=open('E:/GITKRAKEN/IBI1_2019-20/Practical 8/mito_gene.fa','r')

fn=input('input a filename\n')
dn='E:/GITKRAKEN/IBI1_2019-20/Practical 8/'+fn+'.fa'
output=open(dn,'w')
s=''
for line in inp:
	if line.startswith('>'):
		#print(s)
		output.write(RC(s))
		s=''
		output.write("\n"+line)
	else:
		s+=''.join(line.rsplit())
		


inp.close()
output.close()