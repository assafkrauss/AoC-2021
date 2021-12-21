class Polymerizer:
    def __init__(self, template, insertion_pairs):
        self._polymer = []
        for i in range(len(template) - 1):
            self._polymer.append((template[i], template[i + 1]))

        self._insertion_pairs = {}
        for pair in insertion_pairs:
            self._insertion_pairs[tuple(list(pair[0]))] = pair[1]

    def step(self):
        new_polymer = []
        for link in self._polymer:
            if link in self._insertion_pairs.keys():
                new_polymer.append((link[0], self._insertion_pairs[link]))
                new_polymer.append((self._insertion_pairs[link], link[1]))
            else:
                new_polymer.append(link)
        self._polymer = new_polymer

    def polymer(self):
        p = ''.join(list(self._polymer[0]))
        for link in self._polymer[1:]:
            p += link[1]
        return p

    def most_common_element(self):
        p = self.polymer()
        m = p.count(p[0])
        for element in p[1:]:
            if p.count(element) > m:
                m = p.count(element)
        return m

    def least_common_element(self):
        p = self.polymer()
        m = p.count(p[0])
        for element in p[1:]:
            if p.count(element) < m:
                m = p.count(element)
        return m


def main():
    f = open("day14.txt")
    lines = f.readlines()

    pairs = []
    for i in range(2, len(lines)):
        pairs.append(lines[i].strip().split(' -> '))

    p = Polymerizer(lines[0].strip(), pairs)
    for i in range(10):
        p.step()
    print(p.most_common_element() - p.least_common_element())


if __name__ == '__main__':
    main()
