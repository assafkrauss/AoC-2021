class Chiton:
    def __init__(self, x, y, max_x, max_y, weight):
        self.weight = weight
        self._x = x
        self._y = y
        self.neighbors = self._get_neighbors(max_x, max_y)

    def _get_neighbors(self, max_x, max_y):
        if self._x == 0 and self._y == 0:
            return [(1, 0), (0, 1)]
        elif self._x == 0 and self._y == max_y:
            return [(0, max_y - 1), (1, max_y)]
        elif self._x == max_x and self._y == 0:
            return [(max_x - 1, 0), (max_x, 1)]
        elif self._x == max_x and self._y == max_y:
            return [(max_x - 1, max_y), (max_x, max_y - 1)]
        elif self._y == 0:
            return [(self._x - 1, 0), (self._x + 1, 0), (self._x, 1)]
        elif self._x == 0:
            return [(0, self._y - 1), (0, self._y + 1), (1, self._y)]
        elif self._y == max_y:
            return [(self._x - 1, max_y), (self._x + 1, max_y), (self._x, max_y - 1)]
        elif self._x == max_x:
            return [(max_x, self._y - 1), (max_x, self._y + 1), (max_x - 1, self._y)]
        return [(self._x - 1, self._y), (self._x + 1, self._y), (self._x, self._y - 1), (self._x, self._y + 1)]


def dijkstra(chitons):
    src = chitons[0][0]
    distances = {src: 0}
    q = set()
    for y in range(len(chitons)):
        for x in range(len(chitons[0])):
            if chitons[y][x] != src:
                distances[chitons[y][x]] = 999999999
            q.add(chitons[y][x])

    while len(q) != 0:
        v = min(q, key=lambda ch: distances[ch])
        q.remove(v)

        for n in v.neighbors:
            neighbor = chitons[n[1]][n[0]]
            alt = distances[v] + neighbor.weight
            if alt < distances[neighbor]:
                distances[neighbor] = alt

    return distances[chitons[len(chitons) - 1][len(chitons[0]) - 1]]


def main():
    f = open("day15.txt")
    lines = f.readlines()

    chitons = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[0].strip())):
            row.append(Chiton(x, y, len(lines[0].strip()) - 1, len(lines) - 1, int(lines[y][x])))
        chitons.append(row)

    print(dijkstra(chitons))


if __name__ == '__main__':
    main()
