n=int(input())
l=[]
if 1<=n<=10**5:
	[l.append(input()) for i in range(n)]
#print (l)

#ls=set(l)
#print(len(ls))
#print(ls)
#l = ['bcdef', 'abcdefg', 'bcde', 'bcdef']

d = dict()
sampl = l

[l[i],l.count(l[i]) for i in range(len(l))]


#print (d)

#print (str(len(d))+'\n'+ str([i for i in d.values()])[1:-1].replace(", "," ") )