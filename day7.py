#! python
import statistics

def find_median(i):
    #find median
    if len(i)%2:
        #odd length median
        median = i[int(len(i)/2)]
    else:
        #even length median
        middle = int(len(i)/2)-1
        median = int((i[middle]+i[middle])/2)
    return median

def build_cdict(i):
    cdict = {c:0 for c in range(min(i), max(i)+1)}
    for crab in i:
        cdict[crab] += 1
    return cdict

def solve_p1(i):
    median = find_median(i)
    #build dict with locations of all crabs
    cdict = build_cdict(i)
    #count fuel
    fuel_spent = 0
    for position, count in cdict.items():
        fuel_spent += abs(position - median) * count

    return fuel_spent

def solve_p2(clist):
    mean = int(round(statistics.mean(i)))
    options = {mean-1:0, mean:0, mean+1:0}
    cdict = build_cdict(i)
    #bounded 99976804 to 100347068
    print(min(cdict.keys()), max(cdict.keys()))
    for option in options:
        fuel_spent = 0
        for position, count in cdict.items():
            f = sum(range(1, abs(position-option)+1))
            fuel_spent += f*count
        options[option] = fuel_spent
    return min(options.values())

if __name__ == '__main__':
    with open('inputs/i7') as f:
        i = list(map(int, f.readline().split(',')))
    i.sort()
    print(solve_p1(i))
    print(solve_p2(i))