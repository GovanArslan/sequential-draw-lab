def payoff(first, second):
    if first[0] not in ["R", "B"] or second[0] not in ["R", "B"]:
        raise ValueError('Either label does not start with "R" or "B"')
    elif first == second:
        raise ValueError("Both labels are identical")
    if first[0] == "R" and second[0] == "R":
        return 3
    elif "R" in [first[0], second[0]] and "B" in [first[0], second[0]]:
        return 1
    elif "R" not in [first[0], second[0]]:
        return -2


print(payoff("R1", "R2"))
print(payoff("R1", "B3"))
print(payoff("B2", "R2"))
print(payoff("B1", "B3"))
print(payoff("R1", "R1"))
print(payoff("X1", "B2"))

def pattern_counts(outcomes):
    dicti = {
            "RR" : 0,
            "RB" : 0,
            "BR" : 0,
            "BB" : 0
            }
    for pair in outcomes:
        dicti[pair[0][0] + pair[1][0]] += 1
    return dicti

print(pattern_counts([]))
print(pattern_counts([("R1", "R2")]))
print(pattern_counts([("R1", "B2"), ("B1", "R2"), ("B2", "B3"), ("R2", "R1")]))