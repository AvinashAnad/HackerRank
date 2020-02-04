n = input()
l = []
for i in range(int(n)):
#    print(i)
    l.append([input(),round(float(input()),10)])

#print(l)
#l.sort(key = lambda x:x[1])


l1=sorted(list(set(sorted([j for i,j in l]))),key = lambda x:float(x))
#print(l,l1,l1[1])

l2 = sorted(list(filter(lambda x:x[1] ==l1[1],l)))
for i,j in l2:
	print(i)