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


def main():
    f = open("day12.txt")
    lines = f.readlines()

    cg = CaveGraph(lines)
    paths = cg.all_paths()
    print(len(paths))


if __name__ == '__main__':
    main()
