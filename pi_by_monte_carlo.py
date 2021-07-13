import random

INTERVAL = 1000

circle_points = 0
square_points = 0

# Total Random numbers generated= possible x
# values* possible y values
for i in range(INTERVAL**2):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Distance between (x, y) from the origin
    origin_dist = x**2 + y**2

    # Checking if (x, y) lies inside the circle
    if origin_dist <= 1:
        circle_points+= 1

    square_points+= 1

    # Estimating value of pi
    pi = 4 * circle_points / square_points

    #print(x, y, circle_points, square_points, "-", pi)

print(f"estimation π = {pi}")
