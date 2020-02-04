# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
totph = int(input())
#print(totph)

if totph in range(1,15+1):
#print ("Agree")

    l=[]

#    r=range(totph)
#    print ([i for i in r])

    for i in range(totph):
        l.append(input())

#    print (l)
        
    for i in l:
        if (re.search(r'7|8|9',i[0]) is not None) and (len(i) == 10) and i.isdigit():
            print ('YES')
        else: print('NO')
else:
    print ("Retry with less combinations")
