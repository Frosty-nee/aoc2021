#! python


def find_corrupt(i):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    illegals = []
    for line in i:
        stack = []
        for c in line:
            if c in pairs.keys():
                stack.append(c)
            else:
                p = stack.pop()
                if pairs[p] != c:
                    illegals.append((c, line))
    return illegals

def remove_corrupted(i, corrupts):
    for corrupt in corrupts:
        i.remove(corrupt[1])
    return i

def complete_lines(i):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    completed= []
    for line in i:
        stack = []
        for c in line:
            if c in pairs.keys():
                stack.append(c)
            else:
                stack.pop()
        stack.reverse()
        stack = [pairs[c] for c in stack]
        completed.append([line, ''.join(stack)])
    return completed

def score_complete(i):
    values =  {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []
    for line in i:
        score = 0
        for c in line[1]:
            score = score * 5
            score += values[c]
        scores.append(score)

    scores.sort()
    return scores[int(len(scores)/2)]

if __name__ == '__main__':
    with open('inputs/i10') as f:
        i = [s.rstrip() for s in f.readlines()]
        invalid_values = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
        }
        invalid_characters = find_corrupt(i)
        print(sum([invalid_values[c] for c,_ in invalid_characters]))
        print(score_complete(complete_lines(remove_corrupted(i, invalid_characters))))