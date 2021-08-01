import numpy as np
import random

n_piles = 10
max_iter = 100000

piles = np.empty(n_piles)
piles.fill(n_piles)

iter = 0;
while (iter < max_iter and piles.size > 1):  # for N iterations or if there's still piles
    piles = piles[np.nonzero(piles)]         # select all non zero coins piles
    for i in np.arange(piles.size):          # for each pile
        piles[i] -= 1                        # take a coin from pile
        num = np.random.randint(piles.size)  # choose a pile
        piles[num] += 1                      # add a coin to pile choosen
    iter += 1                                # next iteration
else:
    print(f'In {iter} interations')

print(f"we're left with {piles.size} pile")
