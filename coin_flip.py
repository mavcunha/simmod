from random import randint

attempts = 10000 # times we will repeat the throws
success  = 0     # how many times did we achieve what we expected
throws   = 4     # each experiement is this amount of throws
result   = 3     # resulting in this amount of heads.

def toss():
    # heads 1 and tails 0 just by convention
    return randint(0,1)

def tosses(n):
    # the sum of tosses is the about of heads or tails
    # depending which will attribute value 1.
    r = 0
    for t in range(1, n + 1):
        r += toss()
    return r

# experiment 
for i in range(1,attempts + 1):
    # count how many times we achieved the
    # expected result. Ex. 3 heads on 4 throws
    if tosses(throws) == result:
        success += 1

print(f"""We expect {result} heads on {throws} throws.
Repeating {attempts} we got {success} successes.""")
