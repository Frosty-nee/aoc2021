#! python

def process_input(i):
    points = [tuple(list(map(int, line.split(',')))) for line in i[:i.index('')]]
    instructions = [line.split(' ')[-1].split('=') for line in i[i.index('')+1:]]
    instructions = [(d, int(p)) for d, p in instructions]
    return points, instructions

def build_paper(points):
    ex = 0
    ey = 0
    for x, y in points:
        if x > ex:
            ex = x
        if y > ey:
            ey = y
    paper = [['.' for y in range(ex+1)] for x in range(ey+1)]
    for x,y in points:
        paper[y][x] = '#'
    return paper

def fold_paper(paper, instruction):
    direction, position = instruction
    if direction == 'x':
        left = []
        right = []
        for pos, line in enumerate(paper):
            left.append(line[:position])
            right.append(line[position+1:])
        for pos, line in enumerate(right):
            line.reverse()
        for lcount, line in enumerate(left):
            for pos, val in enumerate(line):
                if right[lcount][pos] == '#':
                    left[lcount][pos] = '#'
        return left
    elif direction == 'y':
        top = paper[:position]
        bottom = paper[position+1:]
        bottom.reverse()
        for lcount, line in enumerate(bottom):
            for pos, val in enumerate(line):
                if bottom[lcount][pos] == '#':
                    top[lcount][pos] = '#'
        return top

if __name__ == '__main__':
    with open('inputs/i13') as f:
        i = [line.rstrip() for line in f.readlines()]
    points, instructions = process_input(i)
    paper = build_paper(points)
    first_inst = instructions[0]
    instructions = instructions[1:]
    paper = fold_paper(paper, first_inst)
    print(sum([line.count('#')for line in paper]))
    for inst in instructions:
        paper = fold_paper(paper, inst)
    for line in paper:
        print(''.join(line))
    print(sum([line.count('#')for line in paper]))