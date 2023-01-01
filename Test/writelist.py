lines = []
with open("values.txt", "r") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
print(lines)