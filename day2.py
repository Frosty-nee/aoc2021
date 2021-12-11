#! python

import utils

def process_input(i):
    output = []
    for s in i:
        s = s.split()
        output.append((s[0], int(s[1])))
    return output

direcs = {
    'forward':  (1,0),
    'up':       (0,-1),
    'down':     (0,1)
}

def solve_p1(i):
    horiz, dep = 0, 0
    for ins in process_input(i):
        direc, dist = ins
        t = direcs[direc]
        horiz  += dist * t[0]
        dep       += dist * t[1]
    print(horiz * dep)

def solve_p2(i):
    aim = 0
    dep = 0
    horiz = 0
    for ins in process_input(i):
        direc, dist = ins
        t=direcs[direc]

        aim += dist * t[1]
        dep += dist * aim * t[0]
        horiz += dist * t[0]

    print(horiz*dep)
if __name__ == '__main__':
    i = utils.process_raw_input('i2')
    solve_p1(i)
    solve_p2(i)