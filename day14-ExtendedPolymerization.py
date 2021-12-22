class Polymerizer:
    def __init__(self, template, insertion_pairs):
        self._edges = [template[0], template[-1]]
        self._polymer = {}
        for i in range(len(template) - 1):
            link = (template[i], template[i + 1])
            if link not in self._polymer.keys():
                self._polymer[link] = 0
            self._polymer[link] += 1

        self._insertion_pairs = {}
        for pair in insertion_pairs:
            self._insertion_pairs[tuple(list(pair[0]))] = pair[1]

    def step(self):
        new_polymer = {}
        for link in self._polymer.keys():
            new_links = (link)
            if link in self._insertion_pairs.keys():
                new_links = ((link[0], self._insertion_pairs[link]), (self._insertion_pairs[link], link[1]))
            for new_link in new_links:
                if new_link not in new_polymer.keys():
                    new_polymer[new_link] = 0
                new_polymer[new_link] += self._polymer[link]
        self._polymer = new_polymer

    def most_common_element(self):
        counter = {}
        for link in self._polymer.keys():
            for i in [0, 1]:
                if link[i] not in counter.keys():
                    counter[link[i]] = 0
                counter[link[i]] += self._polymer[link]
        m = max(counter.keys(), key=lambda x: counter[x])
        if m in self._edges:
            m = counter[m] + 1
        else:
            m = counter[m]
        return m // 2

    def least_common_element(self):
        counter = {}
        for link in self._polymer.keys():
            for i in [0, 1]:
                if link[i] not in counter.keys():
                    counter[link[i]] = 0
                counter[link[i]] += self._polymer[link]
        m = min(counter.keys(), key=lambda x: counter[x])
        if m in self._edges:
            m = counter[m] + 1
        else:
            m = counter[m]
        return m // 2


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

    p = Polymerizer(lines[0].strip(), pairs)
    for i in range(40):
        p.step()
    print(p.most_common_element() - p.least_common_element())


if __name__ == '__main__':
    main()
