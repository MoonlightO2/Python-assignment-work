import matplotlib.pyplot as plt

print("Loading image...")
map_image = plt.imread('map7.png')
fig = plt.figure()
ax = fig.subplots()
ax.imshow(map_image)
print("Image loaded...")
plt.show()
print("Image closed...")

"""file1 = open('map7.png', 'rb')

file2 = open('map1.png', 'wb')

print("Drawing map")
for line in file1:
    file2.write(line)

print("Map image ready")
"""