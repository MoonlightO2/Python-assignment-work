words = []
fileOB = open('values.txt', "r")
lines = fileOB.read().splitlines()
for line in lines:
    words.extend(line.split())
print(words)
