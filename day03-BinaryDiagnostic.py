class Entry:
    def __init__(self, line):
        self._val = line.strip()

    def get_bit(self, n):
        return self._val[n]

    def entry_len(self):
        return len(self._val)


def main():
    f = open("day03.txt")
    lines = f.readlines()
    entries = []
    for line in lines:
        entries.append(Entry(line))

    gamma = []
    epsilon = []
    for i in range(entries[0].entry_len()):
        count0, count1 = 0, 0
        for e in entries:
            if e.get_bit(i) == '0':
                count0 += 1
            else:
                count1 += 1
        if count0 > count1:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
    print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))


if __name__ == '__main__':
    main()
