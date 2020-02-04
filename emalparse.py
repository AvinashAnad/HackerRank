import re
import email.utils
totph = int(input())

if totph in range(1,15+1):
    l=[]
    for i in range(totph):
        l.append(input())

    for i in l:
        em = i
        em1 = email.utils.parseaddr(em)[1]
    #     print(em1)
        a,b = em1.find('@') ,em1.find('.') 
    #     print(a,b,em1.split('@')[0], em1.split('@')[0][0] ,em1.split('.')[1], len(em1.split('.')[1]))

        if a != -1 and b != -1   and em1.split('@')[0][0].isalpha() and em1.count('.')==1 and em1.split('@')[1][0].isalpha() and em1.split('.')[1][0].isalpha() and re.match("^[a-zA-Z0-9|.]*$", em1.split('@')[1:][0]) is not None:
            #print (email.utils.formataddr(email.utils.parseaddr(str(em1.split('@')[0])+' <'+str(em1)+'>')))
            print (email.utils.formataddr(email.utils.parseaddr(em)))

#and b>a and 1 <= len(em1.split('.')[1]) <= 3

#g4bhateja@gmail.com
'''
Compiler Message
Wrong Answer
Input (stdin)
Download
3
vineet <vineet.iitg@gmail.com>
vineet <vineet.iitg@gmail.co>
vineet <vineet.iitg@gmail.c>
Expected Output
Download
vineet <vineet.iitg@gmail.com>
vineet <vineet.iitg@gmail.co>
vineet <vineet.iitg@gmail.c>
'''