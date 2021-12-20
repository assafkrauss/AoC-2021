class CaveGraph:
    def __init__(self, edges):
        self._connections = {}
        for edge in edges:
            vertices = edge.strip().split('-')
            for v in vertices:
                if v not in self._connections.keys():
                    self._connections[v] = []
            self._connections[vertices[0]].append(vertices[1])
            self._connections[vertices[1]].append(vertices[0])

    def _all_paths_util(self, src, dest, visited, path, all_paths):
        if str.islower(src):
            visited.add(src)
        path.append(src)

        if src == dest:
            all_paths.append(path)
        else:
            for v in self._connections[src]:
                if v not in visited:
                    self._all_paths_util(v, dest, visited, path, all_paths)

        path.pop()
        if src in visited:
            visited.remove(src)

    def all_paths(self):
        visited = set()
        path = []
        all_paths = []
        self._all_paths_util('start', 'end', visited, path, all_paths)
        return all_paths

    def _all_paths_with_doubles_util(self, src, dest, visited, path, all_paths, double_cave):
        if str.islower(src):
            visited[src] += 1
        path.append(src)

        if src == dest:
            all_paths.append(list(path))
        else:
            for v in self._connections[src]:
                if v not in visited.keys() or visited[v] == 0 or visited[v] == 1 and v == double_cave:
                    self._all_paths_with_doubles_util(v, dest, visited, path, all_paths, double_cave)

        path.pop()
        if src in visited:
            visited[src] -= 1

    def all_paths_with_doubles(self):
        low_caves = [c for c in self._connections.keys() if str.islower(c) and c not in ['start', 'end']]
        total_of_all_paths = []
        for low_cave in low_caves:
            visited = {}
            for v in self._connections.keys():
                if str.islower(v):
                    visited[v] = 0
            path = []
            all_paths = []
            self._all_paths_with_doubles_util('start', 'end', visited, path, all_paths, low_cave)
            total_of_all_paths += all_paths
        return total_of_all_paths


def main():
    f = open("day12.txt")
    lines = f.readlines()

    cg = CaveGraph(lines)
    paths = cg.all_paths()
    print(len(paths))

    paths = cg.all_paths_with_doubles()
    # no idea why there are duplications, so let's filter those out:
    no_dups = set()
    for p in paths:
        no_dups.add(tuple(p))
    print(len(no_dups))


if __name__ == '__main__':
    main()
