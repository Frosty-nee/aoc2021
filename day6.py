#! python
def solve(fd, days):
    def tick_day(fd):
        nfd = {day:0 for day in range(9)}
        for day, fishes in fd.items():
            if day > 0:
                nfd[day-1] += fishes
            elif day == 0:
                nfd[6] += fishes
                nfd[8] += fishes
        return nfd
    for _ in range(days):
        fd = tick_day(fd)
    return(sum([f for _, f in fd.items()]))

if __name__ == '__main__':
    with open('inputs/i6') as f:
        i = list(map(int, f.readline().split(',')))
    fish_dict = {}
    for day in range(9):
        fish_dict[day] = 0
    for fish in i:
        fish_dict[fish] += 1
    print(solve(fish_dict, 80))
    print(solve(fish_dict, 256))