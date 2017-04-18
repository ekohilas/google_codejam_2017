def find(num, people):
    if people == 1:
        return (num//2, (num-1)//2)
    elif people % 2 == 0:
        return find(num//2, people//2)
    else:
        return find((num-1)//2, people//2)

def print_cases(func):
    for i in range(1, int(input())+1):
        num, people = map(int, input().split())
        max_s, min_s = func(num, people)
        print("Case #{}: {} {}".format(i, max_s, min_s))

if __name__ == "__main__":
    print_cases(find)


