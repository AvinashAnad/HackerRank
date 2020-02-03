#list operations
lists = []
n = input()
#print (len(n))
for i in range(int(n)):
    inop = input()
    #print (inop)
    if inop.find('insert') != -1:
    #        print ('inside insert')
        ins_op = inop.split(" ")
        lists.insert(int(ins_op[1]),int(ins_op[2]))


    elif inop == 'print':
        print (lists)

    elif inop.find('remove') != -1:
    #    print ('inside remove')
        ins_op = inop.split(" ")
        lists.remove(int(ins_op[1]))

    #elif inop == 'append':
    #    print ('inside append')
    elif inop.find('append') != -1:
    #    print ('inside remove')
        ins_op = inop.split(" ")
        lists.append(int(ins_op[1]))

    elif inop == 'sort':
    #print ('inside sort')
        lists.sort()


    elif inop == 'pop':
    #        print ('inside pop')
        lists.pop()

    elif inop == 'reverse':
        #print ('inside reverse')
        lists.reverse()

    #print(i)



