#!/usr/bin/python3

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2



from sys import argv
from collections import namedtuple
import re

Claim = namedtuple('Claim', ['id', 'xpos', 'ypos', 'xlength', 'ylength'])

sample_data = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]

expected_result = 3

def parse_line(line):
    '''
    >>> parse_line('#1 @ 1,3: 4x7')
    Claim(id=1, xpos=1, ypos=3, xlength=4, ylength=7)
    >>> parse_line('#150 @ 90,952: 15x18')
    Claim(id=150, xpos=90, ypos=952, xlength=15, ylength=18)
    '''
    id_string = re.findall(r'#\d+', line)[0]
    id = int(re.findall(r'\d+', id_string)[0])
    xy_string = re.findall(r'\d+,\d+', line)[0]
    x,y= [int(x) for x in xy_string.split(',')]
    wh_string = re.findall(r'\d+x\d+', line)[0]
    w, h = [int(x) for x in wh_string.split('x')]
    return Claim(id,x,y,w,h)


def parse(filename):
    file_data = open(filename).read()
    return [parse_line(x) for x in file_data.split('\n') if x]


def calculate_coords(claim, coord_dict, claim_dict):
    for j in range(1, claim.ylength+1):
        for i in range(1, claim.xlength+1):
            coord = (claim.xpos+i, claim.ypos+j)
            if coord not in coord_dict:
                coord_dict[coord] = []
            coord_dict[coord].append(claim)
            if len(coord_dict[coord]) > 1:
                claim_dict[claim.id] = False
                for c in coord_dict[coord]:
                    claim_dict[c.id] = False


def solve(data):
    coord_dict = dict()
    claim_dict = dict()
    for claim in data:
        claim_dict[claim.id] = True
        calculate_coords(claim, coord_dict, claim_dict)
    
    # results = []
    # for key, value in claim_dict.items():
    #     if value:
    #         results.append(key)
    # return results[0]

    return [k for k, v in claim_dict.items() if v][0]


def run_test():
    return solve([parse_line(x) for x in sample_data]) == expected_result

def main(filename):
    print('Day 3 exercise 2!')
    if run_test():
        data = parse(filename)
        print("Result is: {}".format(solve(data)))
        print('Yay!')
    else:
        print('We be fucked')


if __name__ == '__main__':
    name = argv[1]
    filename = 'input_' + name + '.txt'
    main(filename)
