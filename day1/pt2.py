f = open("input1.txt","r").read().splitlines()

elves = []
curr = 0
for line in f:
    if len(line) == 0:
        elves.append(curr)
        curr = 0
        continue
    curr += int(line)

elves.sort()
elves.reverse()
print(sum(elves[:3]))
