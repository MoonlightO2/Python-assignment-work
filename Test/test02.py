words = []
x = open('file1.txt', "r")
lines = x.read().splitlines()
for line in lines:
    words.extend(line.split())

print(words)
