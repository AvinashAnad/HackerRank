n =  input()
n1 = input()
#print ([int(i) for i in n1.split(' ')])

print (hash(tuple([int(i) for i in n1.split(' ')])))