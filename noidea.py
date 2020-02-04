n,m = input().split(" ") # no of input array no of values in sets A and B

n,m = int(n),int(m)
if 1<=int(n)<=10**5 and 1<=int(m)<=10**5:
	a = input().split(" ")
	A = set(input().split(" "))
	B = set(input().split(" "))
	

Hap_ctr=0

if len(A)==m and len(B)==m:
	
	for i in a :
		
		if i in A:
			Hap_ctr+= 1
		if i in B:
			Hap_ctr-= 1

print (Hap_ctr)