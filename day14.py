#! python 

from datetime import datetime

def process_input(i):
    template = i[0]
    rules = i[2:]
    r = {}
    for rule in rules:
        pair, ins = rule.split(' -> ')
        r[pair] = [''.join([pair[0], ins]),''.join([ins,pair[1]])]
    return template, r

def step(template, rules, iterations):
    empty_pairs = {k:0 for k in rules.keys()}
    pairs = empty_pairs.copy()
    counts = {x:0 for x in ''.join(pairs.keys())}
    f = template[0]
    l = template[-1]
    for pair in range(len(template)-1):
        pair = template[pair:pair+2]
        pairs[pair]+=1

    for _ in range(iterations):
        new_pairs = empty_pairs.copy()
        #loop through and multiply
        for pair, value in pairs.items():
            for add in rules[pair]:
                new_pairs[add] += value
        pairs = new_pairs

    for pair in pairs.keys():
        for letter in pair:
            counts[letter] += pairs[pair]
    counts[f]-=1
    counts[l]+=1
    for count in counts.keys():
        counts[count] = counts[count]//2
    return counts

if __name__ == '__main__':
    with open('inputs/i14') as f:
        i = [line.rstrip() for line in f.readlines()]
    template, rules = process_input(i)
    counts = step(template, rules, 10)
    print(max(counts.values()) - min(counts.values()))
    counts = step(template, rules, 40)
    print(max(counts.values()) - min(counts.values()))



