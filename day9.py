#! python

def find_low_points(i):
    lows = {}
    ex = len(i)
    ey = len(i[0])
    for xpos, _ in enumerate(i):
        for ypos, val in enumerate(i[xpos]):
            #check neighbors
            nbr = []
            if ypos < ey-1:
                nbr.append(i[xpos][ypos+1])
            if ypos != 0:
                nbr.append(i[xpos][ypos-1])
            if xpos < ex-1:
                nbr.append(i[xpos+1][ypos])
            if xpos != 0:
                nbr.append(i[xpos-1][ypos])
            if val < min(nbr):
                lows[(xpos,ypos)] = val
    return lows

def count_risk(l):
    risk = 0
    for val in l.values():
        risk += val+1
    return risk

if __name__ == '__main__':
    with open('inputs/i9') as f:
        i = [list(map(int, line.rstrip())) for line in f.readlines()]

    print(count_risk(find_low_points(i)))