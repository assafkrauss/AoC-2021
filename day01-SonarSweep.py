def main():
    f = open("day01.txt")
    lines = f.readlines()

    # part I
    inc_count = 0
    for i in range(1, len(lines)):
        if int(lines[i - 1]) < int(lines[i]):
            inc_count += 1

    print(inc_count)

    # part II
    depths = list(map(lambda x: int(x), lines))
    window = sum(depths[0:2])
    inc_count = 0
    for i in range(3, len(depths)):
        new_window = window - depths[i - 3] + depths[i]
        if new_window > window:
            inc_count += 1
        window = new_window

    print(inc_count)


if __name__ == '__main__':
    main()
