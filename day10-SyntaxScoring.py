def main():
    f = open("day10.txt")
    lines = f.readlines()

    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        char_stack = []
        for c in line:
            if c in ['(', '[', '{', '<']:
                char_stack.append(c)
                continue
            opener = char_stack.pop()
            if c == ')' and opener != '(' \
                    or c == ']' and opener != '[' \
                    or c == '}' and opener != '{' \
                    or c == '>' and opener != '<':
                score += score_table[c]
                break

    print(score)


if __name__ == '__main__':
    main()
