# Convert ASCII Unicode Character 'A' to 65
y = ord('A')
print(type(y), y)

alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Print 65-90
for i in alphabet_list:
    print(ord(i), end=", ")
