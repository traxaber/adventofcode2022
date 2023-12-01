f = open("input.txt", "r").read().splitlines()

total = 0
draws = { "A": 1, "B": 2, "C": 3 }
losers = { "A": 3, "B": 1, "C": 2 }
winners = { "A": 2, "B": 3, "C": 1 }

for l in f:
    opp = l[0]
    urs = l[2]
    if urs == "Y": # draw
        total += draws[opp] + 3
    elif urs == "X": # lose
        total += losers[opp]
    elif urs == "Z": # win
        total += winners[opp] + 6

print(total)
