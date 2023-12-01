f = open("input.txt", "r").read().splitlines()

total = 0
score_d = { "X": 1, "Y": 2, "Z": 3 }
outcome_d = { 23: 3, 24: 6, 25: 0, 22: 0, 21: 6 }

for l in f:
    opp = l[0]
    urs = l[2]
    diff = ord(urs) - ord(opp)
    total += score_d[urs]
    total += outcome_d[diff]

print(total)
