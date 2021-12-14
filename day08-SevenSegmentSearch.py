class WireTangle:
    def __init__(self, wires):
        self.up = self.mid = self.up_right = self.down_right = None
        one = next(d for d in wires if len(d) == 2)
        four = next(d for d in wires if len(d) == 4)
        seven = next(d for d in wires if len(d) == 3)
        self.up = [w for w in seven if w not in one][0]
        six = list(filter(lambda x: len(x) == 6, wires))
        for candidate in six:
            for w in one:
                if w not in candidate:
                    six = candidate
                    self.up_right = w
                    break
        self.down_right = [w for w in one if w != self.up_right][0]
        zero = list(filter(lambda x: len(x) == 6, wires))
        zero.remove(six)
        for candidate in zero:
            for w in four:
                if w not in candidate:
                    zero = candidate
                    self.mid = w
                    break
        self.up_left = [w for w in four if w not in [self.up_right, self.down_right, self.mid]][0]
        nine = list(filter(lambda x: len(x) == 6, wires))
        nine.remove(six)
        nine.remove(zero)
        nine = nine[0]
        self.down_left = [w for w in zero if w not in nine][0]
        self.down = [w for w in nine if w not in four and w != self.up][0]

    def decipher(self, digit):
        if len(digit) == 2:
            return 1
        if len(digit) == 4:
            return 4
        if len(digit) == 3:
            return 7
        if len(digit) == 7:
            return 8
        if len(digit) == 6:
            if self.mid not in digit:
                return 0
            if self.up_right not in digit:
                return 6
            return 9
        # must be true that: len(digit) == 5
        if self.up_right not in digit:
            return 5
        if self.down_right not in digit:
            return 2
        return 3


def main():
    f = open("day08.txt")
    lines = f.readlines()

    # part I
    unique_number_of_segments = 0
    for line in lines:
        [_, values] = line.split('|')
        # 2 for digit 1, 4 for digit 4, 3 for digit 7, 7 for digit 8:
        unique_number_of_segments += len(list(filter(lambda x: x in [2, 4, 3, 7],
                                                     list(map(lambda x: len(x), values.split())))))
    print(unique_number_of_segments)

    # part II
    total = 0
    for line in lines:
        [patterns, values] = line.split('|')
        wt = WireTangle(patterns.split())
        result = 0
        for v in values.split():
            result = result * 10 + wt.decipher(v)
        total += result
    print(total)


if __name__ == '__main__':
    main()
