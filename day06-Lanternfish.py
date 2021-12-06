def main():
    f = open("day06.txt")
    line = f.readline()
    all_fish = list(map(lambda x: int(x), line.split(',')))
    cycle = 9 * [0]
    for fish in all_fish:
        cycle[fish] += 1

    for i in range(80):
        new_fish = cycle[0]
        for j in range(len(cycle) - 1):
            cycle[j] = cycle[j + 1]
        cycle[8] = new_fish
        cycle[6] += cycle[8]

    print(sum(cycle))


if __name__ == '__main__':
    main()
