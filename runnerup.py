n = input()
sc = input()
if 2<=int(n)<=10 and -100<=len(sc.split(" "))<=100:
	ls = list(set(int(i) for i in sc.split(" ")))
	ls.sort()
	#print(ls)
	print(ls[len(ls)-2])
