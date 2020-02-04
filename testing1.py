#ABCDCDC
#CDC
pat = 'CDC'
n= 'ABCDCDC'
count=0
for i in range(len(n)):
	if n[i:i+len(pat)]==pat:
		count+=1


'''
n='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w=4
i=0
l=[]
while i < len(n):
	l.append(n[i:i+w])
	i += w
return '\n'.join(l)
'''
def wrap(string, max_width):
	n=string
	w=max_width
	i=0
	l=[]
	print (n,w,i,l)
	while i < len(n):
		l.append(n[i:i+w])
		i += w
	return '\n'.join(l)
	