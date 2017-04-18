import math
def find_package(p_max, p_min, packages):
    for p in reversed(packages):
        q_max, q_min = p
        if (p_max <= q_min <= p_min) or (p_max <= q_max <= p_min):
            return p
    return False

def calculate_packages(required, ingredients):

    packages = []
    p = 0

    #calculate measurements
    for ingredient in required:
        min_s, max_s = ingredient*0.9, ingredient*1.1
        calculations = []
        for package in ingredient:
            max_serve, min_serve = int(math.floor(package/min_s)), int(math.ceil(package/max_s))
            calculations.append((max_serve, min_serve))
        calculations.sort(key=lambda x: x[0] - x[1], reverse=True)
        packages.append(calculations)

    # TODO: Implement algorithm correctly
    i = 1
    while packages[0]:
        p_max, p_min = packages[0]

        for l in packages[i]:
            if find_package(p_max, p_min, l):
                found = True
            else:
                found = False
                break

        if found:
            for l in packages[i]:
                l.remove(find_pacakge(p_max, p_min, l))
            p += 1

        i += 1

    return p


def print_cases(func):
    for i in range(1, int(input())+1):
        n, p = map(int, input().split())
        required = list(map(int, input().split()))
        packages = []
        for _ in range(n):
            packages.append(list(map(int, input().split())))
        output = func(required, packages)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(calculate_packages)

