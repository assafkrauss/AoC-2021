class Entry:
    def __init__(self, line):
        self._val = line.strip()

    def get_bit(self, n):
        return self._val[n]

    def entry_len(self):
        return len(self._val)

    @property
    def value(self):
        return self._val


def find_common_bit(entries, pos):
    count0, count1 = 0, 0
    for e in entries:
        if e.get_bit(pos) == '0':
            count0 += 1
        else:
            count1 += 1
    return '0' if count0 > count1 else '1'


def main():
    f = open("day03.txt")
    lines = f.readlines()
    entries = []
    for line in lines:
        entries.append(Entry(line))

    gamma = []
    epsilon = []
    for i in range(entries[0].entry_len()):
        b = find_common_bit(entries, i)
        gamma.append(b)
        epsilon.append('0' if b == '1' else '1')

    print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))

    oxygen_generator_list = list(entries)
    pos = 0
    while len(oxygen_generator_list) > 1:
        common_bit = find_common_bit(oxygen_generator_list, pos)
        oxygen_generator_list = list(filter(lambda entry: entry.get_bit(pos) == common_bit, oxygen_generator_list))
        pos += 1

    co2_scrubber_list = list(entries)
    pos = 0
    while len(co2_scrubber_list) > 1:
        common_bit = find_common_bit(co2_scrubber_list, pos)
        co2_scrubber_list = list(filter(lambda entry: entry.get_bit(pos) != common_bit, co2_scrubber_list))
        pos += 1

    print(int(oxygen_generator_list[0].value, 2) * int(co2_scrubber_list[0].value, 2))


if __name__ == '__main__':
    main()
