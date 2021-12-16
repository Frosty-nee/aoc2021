#! python

def process_input(i):
    caves = set()
    for item in i:
        for cave in item:
            caves.add(cave)


    connections = {c:set() for c in caves if c != 'END'}
    for connection in i:
        if 'END' in connection:
            end = connection[connection.index('END')]
            connection.remove('END')
            other = connection[0]
            connections[other].add(end)
        elif 'START' in connection:
            start = connection[connection.index('START')]
            connection.remove('START')
            other = connection[0]
            connections[start].add(other)
        else:
            connections[connection[0]].add(connection[1])
            connections[connection[1]].add(connection[0])
    return connections

def generate_paths(conns, part, lower=None, paths=None, complete_paths=set()):
    new_paths = set()
    if paths == None:
        lowers = [c for c in conns.keys() if c.islower()]
        for conn in conns['START']:
            new_paths.add('-'.join(['START', conn]))
        for lower in lowers:
            complete_paths = complete_paths.union(generate_paths(conns, part, lower, new_paths, complete_paths))
        return complete_paths
    else:
        for path in paths:
            pl = path.split('-')
            if pl[-1] == 'END':
                complete_paths.add(path)
            else:
                for conn in conns[pl[-1]]:
                    if conn.isupper() or (conn == lower and pl.count(conn) < part) or (pl.count(conn) < 1):
                        step = '-'.join([path, conn])
                        new_paths.add(step)
        if len(paths) == 0:
            return complete_paths
        return generate_paths(conns, part, lower, new_paths, complete_paths)

if __name__ == '__main__':
    with open('inputs/i12') as f:
        i = [line.rstrip().split('-') for line in f.readlines()]
    for pos,conn in enumerate(i):
        for pos2,cave in enumerate(conn):
            if cave == 'start' or cave == 'end':
                i[pos][pos2] = cave.upper()
    connections = process_input(i)
    print(len(generate_paths(connections, 1)))
    print(len(generate_paths(connections, 2)))