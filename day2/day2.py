def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    return lines

lines = read_input()

lefts = []
rights = []

for line in lines:
    x, y = line.split("  ")
    lefts.append(x)
    rights.append(y)
    

lefts.sort()
rights.sort()
