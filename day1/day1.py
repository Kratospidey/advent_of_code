def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    return lines

lines = read_input()

lefts = []
rights = []

for line in lines:
    x, y = line.split("  ")
    lefts.append(int(x.strip()))
    rights.append(int(y.strip()))
    

lefts.sort()
rights.sort()

sums = 0

for x,y in zip(lefts,rights):
    sums += abs(x - y)

print(f"Sum of the lists is {sums}")

counts = {}
for i in lefts:
    if i in rights:
        counts[i] = i * rights.count(i) 

print(f"Similariy Score is {sum(counts.values())}")