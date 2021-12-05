class Line:
    def __init__(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def get_points(self, no_diags):
        raise Exception("shouldn't have come here! (get_points)")


class HorizontalLine(Line):
    def __init__(self, x1, x2, y):
        super().__init__(min(x1, x2), max(x1, x2), y, y)

    def get_points(self, no_diags):
        return list(map(lambda x: (x, self._y1), range(self._x1, self._x2 + 1)))


class VerticalLine(Line):
    def __init__(self, x, y1, y2):
        super().__init__(x, x, min(y1, y2), max(y1, y2))

    def get_points(self, no_diags):
        return list(map(lambda y: (self._x1, y), range(self._y1, self._y2 + 1)))


class DiagonalLine(Line):
    def __init__(self, x1, x2, y1, y2):
        super().__init__(x1, x2, y1, y2)
        if x2 < x1:
            self._x1, self._x2 = self._x2, self._x1
            self._y1, self._y2 = self._y2, self._y1

    def get_points(self, no_diags):
        points = []
        if no_diags:
            return points
        for i in range(self._x2 - self._x1 + 1):
            points.append((self._x1 + i, self._y1 + (i if self._y2 > self._y1 else -i)))
        return points


def line_factory(x1, x2, y1, y2):
    if x1 == x2:
        return VerticalLine(x1, y1, y2)
    elif y1 == y2:
        return HorizontalLine(x1, x2, y1)
    else:
        return DiagonalLine(x1, x2, y1, y2)


def main():
    f = open("day05.txt")
    in_lines = f.readlines()
    lines = []
    for in_line in in_lines:
        (start, end) = in_line.split(' -> ')
        (x1, y1) = tuple(map(lambda x: int(x), start.split(',')))
        (x2, y2) = tuple(map(lambda x: int(x), end.split(',')))
        line = line_factory(x1, x2, y1, y2)
        if line:
            lines.append(line)
    points_part1 = {}
    points_part2 = {}
    for line in lines:
        _points = line.get_points(True)
        for p in _points:
            points_part1[p] = points_part1[p] + 1 if p in points_part1.keys() else 1
        _points = line.get_points(False)
        for p in _points:
            points_part2[p] = points_part2[p] + 1 if p in points_part2.keys() else 1
    danger_zone = [p for p in points_part1.keys() if points_part1[p] > 1]
    print(len(danger_zone))
    danger_zone = [p for p in points_part2.keys() if points_part2[p] > 1]
    print(len(danger_zone))


if __name__ == '__main__':
    main()
