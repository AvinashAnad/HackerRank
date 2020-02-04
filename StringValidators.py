n = 'qA2'
l = []
alnumchk = 0
alphachk = 0
digitchk = 0
lowerchk = 0
upperchk = 0
l=[]
if len([i for i in n if i.isalnum()==True])>0:
	l.append(True)
else:
	l.append(False)
if len([i for i in n if i.isalpha()==True])>0:
	l.append(True)
else:
	l.append(False)
if len([i for i in n if i.isdigit()==True])>0:
	l.append(True)
else:
	l.append(False)
if len([i for i in n if i.islower()==True])>0:
	l.append(True)
else:
	l.append(False)
if len([i for i in n if i.isupper()==True])>0:
	l.append(True)
else:
	l.append(False)

[print (i) for i in l]

