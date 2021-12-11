#! python

import utils
import math


def process_input(i):

    processed = []
    for line in i:
        endpoints = [tuple(int(n) for n in m.split(',')) for m in line.split(' -> ')]
        processed.append((endpoints))
    return processed

def draw_lines(endpoints):
    def find_extents(endpoints):
        x_max=0
        y_max=0
        for endset in endpoints:
            if (x:= max([endset[0][0], endset[1][0]])) > x_max:
                x_max = x+1
            if (y:= max([endset[0][1], endset[1][1]])) > y_max:
                y_max = y+1
        return x_max, y_max

    x_max, y_max = find_extents(endpoints)
    grid = [[0]*y_max for _ in range(x_max)]
    for endset in endpoints:
        start, end = endset
        cx, cy = start
        ex, ey = end
        grid[cx][cy] += 1
        while cx != ex or cy != ey:
            if cx != ex:
                cx -= int(math.copysign(1, cx - ex))
            if cy != ey:
                cy -= int(math.copysign(1, cy-ey))
            grid[cx][cy] += 1
    return grid

def prune(endpoints):
    #remove diagonal lines
    pruned = []
    for endpoint in endpoints:
        if endpoint[0][0] == endpoint[1][0] or endpoint[0][1] == endpoint[1][1]:
            pruned.append(endpoint)
    return pruned

def solve(endpoints):
    grid = draw_lines(endpoints)
    count = 0
    for line in grid:
        for cel in line:
            if cel > 1:
                count +=1
    return count


if __name__ == '__main__':
    endpoints = process_input(utils.process_raw_input('i5'))
    
    print(solve(prune(endpoints)))
    print(solve(endpoints))