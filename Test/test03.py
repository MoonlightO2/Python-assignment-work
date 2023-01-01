with open('file1.txt', 'r') as x:
    for y in x:
        print(y, end="")
        z = y.upper()
        print(z, end="")
        s = z[0] + z[2] + z[4]
        print(s)

