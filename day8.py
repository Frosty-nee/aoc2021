#! python

def solve_p1(i):

    counts = {x:0 for x in range(10)}
    for _, suffix in i:
        for digit in suffix.split(' '):
            if len(digit) == 2:
                counts[1] += 1
            if len(digit) == 4:
                counts[4] += 1
            if len(digit) == 7:
                counts[8] += 1
            if len(digit) == 3:
                counts[7] += 1
    return sum(counts.values())

def solve_p2(i):
    #maps a digit length to a known unique number
    uniques = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }
    total = 0
    for line in i:
        numbers = {n:set() for n in range(10)}
        #go through easy solves
        for digit in line.split():
            if len(digit) in uniques:
                intended = uniques[len(digit)]
                for char in digit:
                    numbers[intended].add(char)
        #do a ponder
        for digit in line.split():
            dset = set(list(digit))
            if (l:= len(digit)) not in uniques and dset not in numbers.values():
                if l == 6:
                    #0, 6, 9
                    #if 4 is a subset it's 9
                    if numbers[4] <= dset:
                        numbers[9] = dset
                    elif numbers[1] <= dset:
                        #it's 0
                        numbers[0] = dset
                    else:
                        numbers[6] = dset
                if l == 5:
                    #it's 2, 3, or 5
                    #if 1 is a subset, it's 3
                    if numbers[1] <= dset:
                        numbers[3] = dset
                    elif numbers[8]-numbers[4]-numbers[7] <= dset:
                        numbers[2] = dset
                    else:
                        numbers[5] = dset

        val = []
        for n in line.split()[-4:]:
            try:
                n = list(numbers.values()).index(set(list(n)))
            except ValueError as e:
                for s in numbers.keys():
                    if len(numbers[s]) == 0:
                        numbers[s] = set(list(n))
                        n = list(numbers.values()).index(set(list(n)))
            val.append(n)

        t=int(''.join(list(map(str, val))))
        print(t)
        total += t

    return total

if __name__ == '__main__':
    with open('inputs/i8t') as f:
        i = [' '.join([sub.rstrip() for sub in [split for split in line.split(' | ')]]) for line in f.readlines()]
    #print(solve_p1(i))
    print(solve_p2(i))