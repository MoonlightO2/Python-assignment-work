import string
values = dict()
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 1
print(values)