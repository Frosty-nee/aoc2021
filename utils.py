def process_raw_input(s):
    s = 'inputs/'+s
    with open(s) as t:
        return [line.strip().rstrip() for line in t.readlines()]
