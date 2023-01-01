import re
import os


def assignlettervalues(filename):
    with open(filename, 'r') as modules:
       return dict(map(lambda x: x.rstrip().split(maxsplit=1), modules))


def normalisedata(a1):
    os.remove("file1.txt")
    for a2 in a1:
        #Convert to upper case
        a3 = a2.upper()
        #print(a3)
        #Remove unwanted character "-"
        a4 = a3.replace("-", " ")
        # Remove unwanted character "'"
        a5 = a4.replace("'", " ")
        # Remove unwanted character " "
        a6 = a5.replace(" ", "")
        #print(a6)
        with open("file1.txt", "a") as a7:
            a7.write(a6)


def abbreviations(newstr):
    print(newstr)
    """Print all 3-element subsequences of a string."""
    for i in range(len(newstr)):
        for j in range(i + 1, len(newstr)):
            for k in range(j + 1, len(newstr)):
                m = newstr[i] + newstr[j] + newstr[k]
                mm = m.strip()
                if len(mm) == 3:
                    if mm[0] == newstr[0]:
                        print(mm)
    print()


with open('trees.txt', 'r') as treenames:
    normalisedata(treenames)

with open('file1.txt', 'r') as abbs:
    for abbvs in abbs:
        abbreviations(abbvs)


j = input("Enter word to count value: ")
y(key, val) = {'A': '25', 'B': '8', 'C': '8', 'D': '9', 'E': '35', 'F': '7', 'G': '9', 'H': '7', 'I': '25', 'J': '3', 'K': '6', 'L': '15', 'M': '8', 'N': '15', 'O': '20', 'P': '8', 'Q': '1', 'R': '15', 'S': '15', 'T': '15', 'U': '20', 'V': '7', 'W': '7', 'X': '3', 'Y': '7', 'Z': '1'}
k = len(j)
for i in j:
    if x[i] == y[j]:
