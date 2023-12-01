f = open("input.txt", "r").read().splitlines()

total = 0
for i in range(0, len(f), 3):
    concat = f[i]
    for char in f[i]:
        if char in f[i+1] and char in f[i+2]:
            total += ord(char) - (38 if char.isupper() else 96)
            break

print(total)
