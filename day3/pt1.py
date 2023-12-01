f = open("input.txt", "r").read().splitlines()

total = 0

for l in f:
    firsthalf = l[:len(l)//2]
    secondhalf = l[len(l)//2:]
    for char in firsthalf:
        if char in secondhalf:
            total += ord(char) - (38 if char.isupper() else 96)
            break

print(total)
