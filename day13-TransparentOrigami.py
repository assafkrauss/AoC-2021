def fold_up(dots, y):
    folded_dots = set()
    for dot in dots:
        if dot[1] > y:
            folded_dots.add((dot[0], dot[1] - 2 * (dot[1] - y)))
        else:
            folded_dots.add(dot)
    return folded_dots


def fold_left(dots, x):
    folded_dots = set()
    for dot in dots:
        if dot[0] > x:
            folded_dots.add((dot[0] - 2 * (dot[0] - x), dot[1]))
        else:
            folded_dots.add(dot)
    return folded_dots


def main():
    f = open("day13.txt")
    lines = f.readlines()

    dots = set()
    folds = []
    i = 0
    while lines[i].strip() != '':
        dots.add(tuple([int(x) for x in lines[i].strip().split(',')]))
        i += 1
    i += 1
    while i < len(lines):
        fold = lines[i].strip().split()[2].split('=')
        fold = (fold[0], int(fold[1]))
        folds.append(fold)
        i += 1

    for i in range((len(folds))):
        if folds[i][0] == 'y':
            dots = fold_up(dots, folds[i][1])
        else:
            dots = fold_left(dots, folds[i][1])
        if i == 0:
            print(len(dots))

    min_x = min(dots, key=lambda dot: dot[0])[0]
    max_x = max(dots, key=lambda dot: dot[0])[0]
    min_y = min(dots, key=lambda dot: dot[1])[1]
    max_y = max(dots, key=lambda dot: dot[1])[1]
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            row += '#' if (x, y) in dots else ' '
        print(row)


if __name__ == '__main__':
    main()
