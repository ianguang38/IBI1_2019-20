bp={'A':'T','T':'A','C':'G','G':'C'}

seq = 'ATGCGACTACGATCGAGGGCCAT'
rev = ''
l = len(seq)

for i in range(l):
    rev += bp[seq[l-i-1]]

print(seq)
print(rev)








