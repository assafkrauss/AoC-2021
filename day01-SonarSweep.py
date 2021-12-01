def main():
    f = open("day01.txt")
    lines = f.readlines()
    inc_count = 0
    for i in range(1, len(lines)):
        if int(lines[i - 1]) < int(lines[i]):
            inc_count += 1

    print(inc_count)


if __name__ == '__main__':
    main()
