with open('values.txt') as f:
    mylist = [tuple(map(float, i.split(','))) for i in f]
