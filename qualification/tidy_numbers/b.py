def tidy_number(number):
    # TODO: implement in binary
    num = list(reversed(list(map(int, str(number)))))
    tidy_num = []

    # TODO: put edgecase into loop
    if len(num) == 1:
        return number
    else:
        if num[0] < num[1]:
            tidy_num = [9] + [num[1]-1]
        else:
            tidy_num = [num[0], num[1]]

        for i in range(2, len(num)):
            if tidy_num[i-1] < num[i]:
                tidy_num = [9]*i + [num[i]-1]
            else:
                tidy_num += [num[i]]

    return int("".join(map(str, reversed(tidy_num))))

def print_cases(func):
    for i in range(1, int(input())+1):
        print("Case #{}: {}".format(i, func(int(input()))))

if __name__ == "__main__":
    print_cases(tidy_number)

