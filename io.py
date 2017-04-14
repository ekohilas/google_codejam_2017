from sys import argv

def write_cases(func, filename):
    with open(filename) as fi, open(filename.split(".")[0] + ".out", "w") as fo:
        for i in range(1, int(fi.readline().strip())+1):
            line = func(int(fi.readline().strip()))
            print("Case #{}: {}".format(i, line), file=fo)

def print_cases(func, filename):
    with open(filename) as fi:
        for i in range(1, int(fi.readline().strip())+1):
            line = fi.readline().strip()
            print("{} -> {}".format(line, func(int(line))))

if __name__ == "__main__":
    #write_cases(, argv[1])

