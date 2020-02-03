n=int(input())
l=[]
for i in range(n):
	id = input()
	a = sorted([i for i in id])
	if len(id) == 10 and id.isalnum() and len([i for i in id if i.isdigit()])>=3 and len([i for i in id if i.isupper()]) >=2 and len([i for i in range(len(a)-1) if a[i]==a[i+1]]) == 0:
		l.append("Valid")
	else:
		l.append("Invalid")

for i in l:
	print(i)