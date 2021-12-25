class Packet:
    def __init__(self, txt, pos):
        self.sub_packets = []
        self.version = int(txt[pos:pos + 3], 2)
        self.id = int(txt[pos + 3:pos + 6], 2)
        self.length = 6
        pos += 6

        if self.id == 4:
            self.literal = ''
            while txt[pos] == '1':
                self.literal += txt[pos + 1:pos + 5]
                self.length += 5
                pos += 5
            self.literal += txt[pos + 1:pos + 5]
            self.length += 5
            pos += 5
            self.literal = int(self.literal, 2)
        else:
            self.len_type = txt[pos]
            self.length += 1
            pos += 1
            if self.len_type == '0':
                self.length += 15
                sub_length = int(txt[pos:pos + 15], 2)
                pos += 15
                while sub_length > 0:
                    sub = Packet(txt, pos)
                    self.sub_packets.append(sub)
                    self.length += sub.length
                    pos += sub.length
                    sub_length -= sub.length
            else:
                self.length += 11
                sub_packet_num = int(txt[pos:pos + 11], 2)
                pos += 11
                while sub_packet_num > 0:
                    sub = Packet(txt, pos)
                    self.sub_packets.append(sub)
                    self.length += sub.length
                    pos += sub.length
                    sub_packet_num -= 1

    def get_version_sum(self):
        version_sum = self.version
        for sub in self.sub_packets:
            version_sum += sub.get_version_sum()
        return version_sum


def main():
    f = open("day16.txt")
    line = f.readline().strip()
    txt = bin(int(line, 16))[2:]
    while len(txt) % 4 != 0:
        txt = '0' + txt
    p = Packet(txt, 0)
    print(p.get_version_sum())


if __name__ == '__main__':
    main()
