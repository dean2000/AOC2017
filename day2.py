from itertools import combinations

checksum = 0
with open('input', 'r') as input:
    for line in input:
        line = list(map(int, line.split()))
        for x,y in combinations(line, 2):
            if x < y:
                x,y = y,x
            if x % y == 0:
                checksum += x // y

print(checksum)
        