from random import randint
from math import sqrt

steps = 100
iterations = 1000

def random_walk():
    r = 0
    for _ in range(1, steps + 1):
        r += 1 if randint(0,1) else -1
    return r

def experiment(n):
    experiments = n
    total = 0
    for _ in range(1, experiments + 1):
        total += random_walk()
    return total // experiments


avg = experiments(iterations)

print(f"""Random walk in one-dimension
Steps: {steps}
Experiments: {iterations}
Average: {avg}""")
