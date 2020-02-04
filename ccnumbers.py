# It must start with a 4, 5 or 6. done
# It must contain exactly 16 digits.  done
# It must only consist of digits (0-9). done
# It may have digits in groups of 4, separated by one hyphen "-". done
# It must NOT use any other separator like ' ' , '_', etc. done
# It must NOT have  or more consecutive repeated digits. done

import re
n=input()
l=[]
[l.append(input()) for i in range(int(n))]
#print (l)
v=[]
for i in l:
	if len([j for j in i if i.isdigit()])==16 and (i.startswith('4') or i.startswith('5') or i.startswith('6')) and re.match("^[0-9_]*$", i) is not None and i.find('-') !=0 and len([k for k in i.split('-') if len(k)==4])==4 and len([a[i:i+5] for i in range(len(a)) if a[i:i+4] == a[i+1:i+5]])==0:
		print ('Valid')
	else:
		print('Invalid')