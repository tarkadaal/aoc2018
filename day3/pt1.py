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

expected_result = 4

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


def calculate_coords(xpos, ypos, xlength, ylength, coord_dict):
    for j in range(1, ylength+1):
        for i in range(1, xlength+1):
            coord = (xpos+i, ypos+j)
            if coord not in coord_dict:
                coord_dict[coord] = 0
            coord_dict[coord] += 1


def solve(data):
    coord_dict = dict()
    for line in data:
        calculate_coords(line.xpos, line.ypos, line.xlength, line.ylength, coord_dict)
    
    # count all entries in dict with value of 2 or more
    # equivalent to:
    # total_collision = 0
    # for line in coord_dict:
    #     if coord_dict[line] > 1:
    #         total_collision += 1
    # return total_collision
    return sum([x > 1 for x in coord_dict.values()])


def run_test():
    return solve([parse_line(x) for x in sample_data]) == expected_result

def main(filename):
    print('Day 3 exercise 1!')
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
