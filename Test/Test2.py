y = open('file2.txt', 'r')
i=0
for abb1 in y.readline():
    #print(abb1)
    abb2 = []
    for i in range(0, 2, 4):
        abb2.append(i)
        print(abb2[i])
        i=i+2
        y = open('file3.txt', 'a')
        #y.write(abb2)

#z=open('file3.txt', 'r')
#print(z.read())

y.close()
#z.close()
