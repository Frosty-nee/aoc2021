#! python

def find_low_points(i):
    lows = {}
    for xpos, _ in enumerate(i):
        for ypos, val in enumerate(i[xpos]):
            #check neighbors
            nbrs = [i[x][y] for x,y in get_nbrs(i,(xpos,ypos))]
            if val < min(nbrs):
                lows[(xpos,ypos)] = val
    return lows

def fill_basins(i, lows):
    basins = []
    for low in lows:
        basin = set()
        step = [tuple(low)]
        while len(step):
            pos = step.pop()
            if i[pos[0]][pos[1]] < 9:
                basin.add(pos)
            nbrs = get_nbrs(i, pos)
            for nbr in nbrs:
                if nbr not in basin and nbr not in step and i[nbr[0]][nbr[1]] < 9:
                    t = tuple(nbr)
                    step.append(t)
        basins.append(basin)
    return basins

def get_nbrs(i, pos):
    x, y = pos
    nbrs = []
    if y < len(i[0])-1:
        nbrs.append(tuple([x,y+1]) )
    if y != 0:
        nbrs.append(tuple([x,y-1]))
    if x < len(i)-1:
        nbrs.append(tuple([x+1,y]))
    if x != 0:
        nbrs.append(tuple([x-1,y]))
    return nbrs


def count_risk(l):
    risk = 0
    for val in l.values():
        risk += val+1
    return risk



if __name__ == '__main__':
    with open('inputs/i9') as f:
        i = [list(map(int, line.rstrip())) for line in f.readlines()]

    print(count_risk(find_low_points(i)))
    lengths = [len(b) for b in fill_basins(i, find_low_points(i))]
    lengths.sort()
    b = 1
    for n in lengths[-3:]:
        b = b*n
    print(b)
