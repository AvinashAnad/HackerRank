import re
n= input()
xc = n
xv = n

if n.isupper() and 0<len(n)<= 10**6:
	print ([i for i in n])
else:
	print("Error! enter the string in upper case")