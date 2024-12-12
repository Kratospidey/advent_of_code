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

sums = 0

for x,y in zip(lefts,rights):
    sums += abs(int(x.strip()) - int( y.strip()))

print(sums)