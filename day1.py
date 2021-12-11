#! python

with open('i1') as t:
    lines = [ int(l.rstrip()) for l in t.readlines()]


def solve_p1():
    prev = lines[0]
    count = 0
    for line in range(len(lines)):
        current = lines[line]
        if current > prev:
            count+=1
        prev = lines[line]
    print('Part 1: ', count)

def solve_p2():
    prev = sum(lines[0:3])
    count = 0
    for line in range(len(lines)-2):
        lsum = sum(lines[line:line+3])
        if lsum > prev:
            count +=1
        prev = lsum
    print(count)

if __name__ == '__main__':
    solve_p1()
    solve_p2()