import random

with open("tests.in", "w") as fo:
    n = 100
    print(n, file=fo)
    for _ in range(n):
        print(random.randrange(1, 10**18), file=fo)
