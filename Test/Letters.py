a = open('file1.txt', 'r')
for words in a.read():
    letters = words.upper()
    b = open('file2.txt', 'a')
    b.write(letters)
    c = open('file2.txt', 'r')

print(c.read())
print("")

a.close()
b.close()
c.close()

def subseq2(newstr):
    """Print all 2-element subsequences of a string."""
    for i in range(len(newstr)):
        for j in range(i + 1, len(newstr)):
            for k in range(j + 1, len(newstr)):
                print(newstr[i] + newstr[j] + newstr[k], end=' ')
    print()


x = open('file2.txt', 'r')
for abb in x.read():
    y = open('file3.txt', 'a')
    y.write()
    z = open('file3.txt', 'r')

print(z.read())

x.close()
y.close()
z.close()