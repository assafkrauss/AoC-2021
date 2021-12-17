def main():
    f = open("day10.txt")
    lines = f.readlines()

    opener2closer = {'(': ')', '[': ']', '{': '}', '<': '>'}
    closer2opener = {')': '(', ']': '[', '}': '{', '>': '<'}
    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    missing_closer_table = {')': 1, ']': 2, '}': 3, '>': 4}
    completion_scores = []
    for line in lines:
        char_stack = []
        corrupt = False
        for c in line.strip():
            if c in ['(', '[', '{', '<']:
                char_stack.append(c)
                continue
            opener = char_stack.pop()
            if closer2opener[c] != opener:
                score += score_table[c]
                corrupt = True
                break
        if not corrupt:
            completion_score = 0
            while len(char_stack) != 0:
                missing_closer = opener2closer[char_stack.pop()]
                completion_score = completion_score * 5 + missing_closer_table[missing_closer]
            completion_scores.append(completion_score)

    print(score)
    completion_scores = sorted(completion_scores)
    print(completion_scores[len(completion_scores) // 2])


if __name__ == '__main__':
    main()
