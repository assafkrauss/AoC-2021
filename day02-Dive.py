def main():
    f = open("day02.txt")
    lines = f.readlines()

    horizontal, depth = 0, 0
    for line in lines:
        [direction, val] = line.strip().split()[:2]
        if direction == "forward":
            horizontal += int(val)
        elif direction == "down":
            depth += int(val)
        else:  # assuming direction == "up"
            depth -= int(val)

    print(horizontal * depth)


if __name__ == '__main__':
    main()
