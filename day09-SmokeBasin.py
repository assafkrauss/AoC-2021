import queue


class CaveMap:
    def __init__(self, cave_map):
        self._cave_map = cave_map
        self._basins = {}

        for y in range(len(self._cave_map)):
            for x in range(len(self._cave_map[0])):
                if self._cave_map[y][x] < min([self._cave_map[n_y][n_x] for (n_x, n_y) in self._get_neighbors(x, y)]):
                    self._basins[(x, y)] = {(x, y)}

    def _get_neighbors(self, x, y):
        if x == 0 and y == 0:
            return [(x + 1, y), (x, y + 1)]
        elif x == 0 and y == len(self._cave_map) - 1:
            return [(x, y - 1), (x + 1, y)]
        elif x == len(self._cave_map[0]) - 1 and y == 0:
            return [(x - 1, y), (x, y + 1)]
        elif x == len(self._cave_map[0]) - 1 and y == len(self._cave_map) - 1:
            return [(x - 1, y), (x, y - 1)]
        elif y == 0:
            return [(x - 1, y), (x + 1, y), (x, y + 1)]
        elif x == 0:
            return [(x, y - 1), (x, y + 1), (x + 1, y)]
        elif y == len(self._cave_map) - 1:
            return [(x - 1, y), (x + 1, y), (x, y - 1)]
        elif x == len(self._cave_map[0]) - 1:
            return [(x, y - 1), (x, y + 1), (x - 1, y)]
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def total_risk_level(self):
        s = sum([self._cave_map[y][x] for (x, y) in self._basins.keys()])
        return s + len(self._basins)

    def calc_basins(self):
        for basin in self._basins.keys():
            q = queue.SimpleQueue()
            q.put(basin)
            visited = set()
            while not q.empty():
                point = q.get()
                visited.add(point)
                self._basins[basin].add(point)
                for neighbor in [n for n in self._get_neighbors(point[0], point[1])
                                 if self._cave_map[n[1]][n[0]] != 9 and n not in visited]:
                    q.put(neighbor)

    def calc_part2(self):
        three_largest_basins = sorted(self._basins.keys(), key=lambda k: len(self._basins[k]), reverse=True)[:3]
        return (len(self._basins[three_largest_basins[0]]) *
                len(self._basins[three_largest_basins[1]]) *
                len(self._basins[three_largest_basins[2]]))


def main():
    f = open("day09.txt")
    lines = f.readlines()

    cave_map = []
    for line in lines:
        cave_map.append([int(c) for c in line.strip()])

    cm = CaveMap(cave_map)
    print(cm.total_risk_level())
    cm.calc_basins()
    print(cm.calc_part2())


if __name__ == '__main__':
    main()
