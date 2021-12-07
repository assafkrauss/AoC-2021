def main():
    f = open("day07.txt")
    line = f.readline()
    all_crabs = list(map(lambda x: int(x), line.split(',')))

    min_fuel = -1
    for i in range(min(all_crabs), max(all_crabs) + 1):
        fuel = 0
        for crab in all_crabs:
            fuel += abs(crab - i)
        if min_fuel == -1:
            min_fuel = fuel
        else:
            min_fuel = min(min_fuel, fuel)
    print(min_fuel)


if __name__ == '__main__':
    main()
