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

    lines = [line.strip() for line in lines]
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])

    chitons = []
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[0])):
            row.append(Chiton(x, y, len(grid[0]) - 1, len(grid) - 1, grid[y][x]))
        chitons.append(row)

    print(dijkstra(chitons))

    large_grid = []
    for y in range(5 * len(grid)):
        large_row = []
        for x in range(5 * len(grid[0])):
            value = grid[y % len(grid)][x % len(grid[0])] + (x // len(grid)) + (y // len(grid[0]))
            if value > 9:
                value -= 9
            large_row.append(value)
        large_grid.append(large_row)

    chitons = []
    for y in range(len(large_grid)):
        row = []
        for x in range(len(large_grid[0])):
            row.append(Chiton(x, y, len(large_grid[0]) - 1, len(large_grid) - 1, large_grid[y][x]))
        chitons.append(row)

    print(dijkstra(chitons))


if __name__ == '__main__':
    main()
