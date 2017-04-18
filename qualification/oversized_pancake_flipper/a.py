def flip(pancake):
    return ["+" if x == "-" else "-" for x in pancake]

def flips(pancake, flip_size):
    pancake = list(pancake)
    flips = 0
    while pancake and (pancake[0] == "+" or len(pancake) >= flip_size):
        if pancake[0] == "+":
            pancake.pop(0)
        else:
            pancake = flip(pancake[:flip_size]) + pancake[flip_size:]
            flips += 1

    if len(pancake) == 0:
        return flips
    else:
        return "IMPOSSIBLE"

def print_cases(func):
    for i in range(1, int(input())+1):
        pancake, num = input().split()
        output = func(pancake, int(num))
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(flips)

