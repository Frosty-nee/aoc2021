#! python

import utils
import math

def process_input(i):
    return [list(map(int,b)) for b in i]


def find_most_common_bits(l):
    mcbits = []
    for pos, _ in enumerate(l[0]):
        total = 0
        for bina in l:
            total += bina[pos]
        mcbits.append(math.floor(total/len(l)+.5))
    return mcbits

def find_least_common_bits(l):
    return [1-b for b in find_most_common_bits(l)]

def solve_p1(i):
    def find_gamma(l):
        return int(''.join(list(map(str, l))),2)
    def find_epsilon(l):
        l = [1-b for b in l]
        return(find_gamma(l))
    g = find_gamma(find_most_common_bits(i))
    e = find_epsilon(find_most_common_bits(i))
    return e*g

def solve_p2(i):
    def find_ogr(il, cbf):
        cb = cbf(il)
        for pos, _ in enumerate(cb):
            reduced_list = [line for line in il if line[pos] == cb[pos]]
            il = reduced_list
            cb = cbf(il)
            if len(il) == 1:
                break
        return il[0]


    ogr = int(''.join(map(str,find_ogr(i, find_most_common_bits))),2)
    cosr = int(''.join(map(str,find_ogr(i, find_least_common_bits))),2)
    return (ogr *cosr)




if __name__ == '__main__':
    i = process_input(utils.process_raw_input('i3'))
    print(solve_p1(i))
    print(solve_p2(i))
