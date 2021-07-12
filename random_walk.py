from random import randint
from math import sqrt

steps = 100
iterations = 1000

def random_walk():
    r = 0
    for _ in range(1, steps + 1):
        # couple shorthands...
        # r += (-1, 1)[randint(0,1)]
        # r += randint(0, 1) or -1
        # but a clearer way to write is:
        if (randint(0,1) == 1):
            r += 1
        else:
            r += -1
    return abs(r)

def experiements(n):
    experiments = n
    total = 0
    for _ in range(1, experiments + 1):
        total += random_walk()
    return total / experiments


print(f"""Random walk in one-dimension
Steps: {steps}
Experiments: {iterations}
Average: {experiements(iterations)}""")
