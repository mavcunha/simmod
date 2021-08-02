import random as rnd

Δt = 2
x, y = 0, 0

def step():
    choices = (-Δt, 0, Δt)
    v_x = rnd.choice(choices)
    v_y = rnd.choice(choices)
    return (v_x, v_y)


print(f't=0 x={x} y={y}')
for t in range(1 , 10 + 1):
    v_x, v_y = step()
    x = x + Δt * v_x
    y = y + Δt * v_y
    print(f't={t} x={x} y={y}')

