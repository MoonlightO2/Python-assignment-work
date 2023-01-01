x = open('file1.txt', 'r')
for words in x.read():
    upperlet = words.upper()
    x = open('file2.txt', 'a')
    x.write(upperlet)

s=open('file2.txt','r')
print(s.read())

s.close()
x.close()