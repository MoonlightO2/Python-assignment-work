d = {}
with open("values.txt", "r") as a1:
    for a2 in a1:
        (key, val) = a2.split()
        d[int(val)] = key

print(d)
