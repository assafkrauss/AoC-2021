class Line:
    def __init__(self, x1, x2, y1, y2):
        self._x1 = min(x1, x2)
        self._x2 = max(x1, x2)
        self._y1 = min(y1, y2)
        self._y2 = max(y1, y2)

    def get_points(self):
        raise Exception("shouldn't have come here! (get_points)")


class HorizontalLine(Line):
    def __init__(self, x1, x2, y):
        super().__init__(x1, x2, y, y)

    def get_points(self):
        return list(map(lambda x: (x, self._y1), range(self._x1, self._x2 + 1)))


class VerticalLine(Line):
    def __init__(self, x, y1, y2):
        super().__init__(x, x, y1, y2)

    def get_points(self):
        return list(map(lambda y: (self._x1, y), range(self._y1, self._y2 + 1)))


def line_factory(x1, x2, y1, y2):
    if x1 == x2:
        return VerticalLine(x1, y1, y2)
    elif y1 == y2:
        return HorizontalLine(x1, x2, y1)
    else:
        return False


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
    points = {}
    for line in lines:
        for p in line.get_points():
            points[p] = points[p] + 1 if p in points.keys() else 1
    danger_zone = [p for p in points.keys() if points[p] > 1]
    print(len(danger_zone))


if __name__ == '__main__':
    main()
