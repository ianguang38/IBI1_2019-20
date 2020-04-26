import re

gene=open('E:/GITKRAKEN/IBI1_2019-20/Practical 8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output=open('E:/GITKRAKEN/IBI1_2019-20/Practical 8/mito_gene.fa','w')

for line in gene:
    if line.startswith('>'):
        name=re.search(r'gene:(\S+) ',line)
        output.write('>'+name.group(1)+'\n')
        #print(name)
    else:
        output.write(line)
 
gene.close()
output.close()