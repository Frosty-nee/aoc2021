#! python

def process_input(i):
    caves = set()
    for connection in i:
        for cave in connection:
            caves.add(cave)
    caves = {cave:set() for cave in caves}
    for connection in i:
        c1, c2 = connection
        caves[c1].add(c2)
        caves[c2].add(c1)
    return caves

def find_paths(connections, paths):
    while True:
        npaths = []
        slen = len(paths)
        for path in paths:
            for connection in connections[path[-1]]:
                if connection == 'START':
                    continue
                npath = path.copy()
                npath.append(connection)
                if is_valid(npath) and npath not in paths:
                    npaths.append(npath)
                elif npath[:-1] not in npaths:
                    npaths.append(npath[:-1])
        paths = npaths
        if slen == len(paths):
            break

    return prune(npaths)

def prune(paths):
    valids = []
    for path in paths:
        if is_valid(path) and path[-1] == 'END':
            valids.append(path)
    return valids

def is_valid(path):
    for cave in set(path):
        if path.count(cave) > 1 and cave.islower():
            return False
        if len(path) > 1 and path[-1] == 'START':
            return False
        if len(path) > 2 and path[-2] == 'END':
            return False
    return True

if __name__ == '__main__':
    with open('inputs/i12') as f:
        i = [line.rstrip().split('-') for line in f.readlines()]
        for pos,conn in enumerate(i):
            for pos2,cave in enumerate(conn):
                if cave == 'start' or cave == 'end':
                    i[pos][pos2] = cave.upper()
    connections = process_input(i)
    print(len(find_paths(connections, [['START']])))