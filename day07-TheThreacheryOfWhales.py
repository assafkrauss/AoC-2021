def calc_fuel(points, fuel_func):
    min_fuel = -1
    for i in range(min(points), max(points) + 1):
        fuel = 0
        for p in points:
            fuel += fuel_func(abs(p - i))
        if min_fuel == -1:
            min_fuel = fuel
        else:
            min_fuel = min(min_fuel, fuel)
    return min_fuel


def main():
    f = open("day07.txt")
    line = f.readline()
    all_crabs = list(map(lambda x: int(x), line.split(',')))

    # part I
    print(calc_fuel(all_crabs, lambda x: x))
    # part II
    print(calc_fuel(all_crabs, lambda x: (x / 2) * (x + 1)))


if __name__ == '__main__':
    main()
