l = ['bcdef', 'abcdefg', 'bcde', 'bcdef']

d = dict()
sampl = l
for i in range(len(l)):
	#sampl.remove([l[i]])
	d[l[i]] = l.count(l[i])

print (d)
print ( str([i for i in d.values()])[1:-1].replace(", "," ") )

	
