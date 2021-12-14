#! python

def step(i, neighbors):
    flash_count = 0
    #add base energy
    for ypos in range(len(i)):
        for xpos in range(len(i[ypos])):
            i[ypos][xpos] += 1
    #resolve flashes
    flashed = {(y,x): False for y in range(len(i)) for x in range(len(i[0]))}
    while True:
        loop = False
        for ypos in range(len(i)):
            for xpos in range(len(i[ypos])):
                if i[ypos][xpos] > 9:
                    i[ypos][xpos] = 0
                    flashed[(ypos, xpos)] = True
                    flash_count += 1
                    #add energy to neighbors
                    for neighbor in neighbors[(ypos,xpos)]:
                        try:
                            if not flashed[neighbor]:
                                i[neighbor[0]][neighbor[1]] += 1
                        except:
                            pass
        #check to see if we need to do another loop
        for ypos in range(len(i)):
            for xpos in range(len(i[ypos])):
                if i[ypos][xpos] > 9:
                    loop = True
        if not loop:
            break
    return i, flash_count, flashed

def find_neighbors(i):
    neighbors = dict()
    for ypos in range(len(i)):
        for xpos in range(len(i[ypos])):
            position = []
            #there's a better way to do this but lazy
            #left and right of position
            position.append((ypos-1, xpos))
            position.append((ypos+1, xpos))
            #above and below
            position.append((ypos, xpos+1))
            position.append((ypos, xpos-1))
            #diagonals
            position.append((ypos-1, xpos+1))
            position.append((ypos-1, xpos-1))
            position.append((ypos+1, xpos+1))
            position.append((ypos+1, xpos-1))
            neighbors[(ypos, xpos)] = position
    return neighbors

if __name__ == '__main__':
    with open('inputs/i11') as f:
        i = [list(map(int, line.rstrip())) for line in f.readlines()]
    neighbors = find_neighbors(i)
    flash_count = 0
    step_count = 0
    while True:
        step_count+=1
        i, flashes, flashed=step(i, neighbors)
        flash_count += flashes
        #check if all octopus flashed
        all_flashed = True
        for octopus in flashed.values():
                if not octopus:
                    all_flashed = False
                    break
        if step_count == 100:
            print(flash_count)
        if all_flashed:
            print(step_count)
            break
