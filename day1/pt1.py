f = open("input1.txt", "r").read().splitlines()

maximum = 0
curr = 0

for line in f:
    if len(line) == 0:
        if curr > maximum:
            maximum = curr
        curr = 0
        continue
    item = int(line)
    curr += item
    # print(line)

print(maximum)
