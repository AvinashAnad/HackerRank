n=int(input())
l=[]
if 1<=n<=10**5:
	[l.append(input()) for i in range(n)]
	t=tuple(l)
#print (l)

d = dict()
sampl = l

for i in range(len(l)):
	d[l[i]] = l.count(l[i])

print (str(len(d))+'\n'+ [i for i in d.values()])