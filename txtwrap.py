import textwrap

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

if __name__ == '__main__':
	string, max_width = input(), int(input())
	result = wrap(string, max_width)
	print(result)