def main():
    f = open("day08.txt")
    lines = f.readlines()
    unique_number_of_segments = 0
    for line in lines:
        [patterns, values] = line.split('|')
        # 2 for digit 1, 4 for digit 4, 3 for digit 7, 7 for digit 8:
        unique_number_of_segments += len(list(filter(lambda x: x in [2, 4, 3, 7],
                                                     list(map(lambda x: len(x), values.split())))))
    print(unique_number_of_segments)


if __name__ == '__main__':
    main()
