import types
import numpy as np
from random import random
from dataclasses import dataclass

ti   = 0
tmax = 2
Δt = 2
k1 = 0.2
k2 = 0.2

@dataclass
class Particle:
    name: str
    k: float
    qty: int = 0

    def transform(self , t: float, p):
        if (random() < self.k * t):
            self.qty -= 1
            p.qty += 1


def choose(a: Particle, b: Particle):
    r = a.qty / (a.qty + b.qty)
    return (a, b) if random() < r else (b, a)

A = Particle("A", k1, 4)
B = Particle("B", k2, 3)

for t in np.arange(ti, tmax + 1, Δt):
    for _ in range(1, (A.qty + B.qty) + 1):
        (x, y) = choose(A, B)
        x.transform(Δt, y)
        print(f"iteration: {_}, choose:{x.name}, {x}, {y}")
    print(f"at t:{t} [A: {A.qty} and B:{B.qty}]")

