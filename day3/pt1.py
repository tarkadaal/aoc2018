#!/usr/bin/python3

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2



from sys import argv
from collections import namedtuple
import re

Claim = namedtuple('Claim', ['id', 'x', 'y', 'width', 'height'])

tests = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]

answer = 4

def parse_line(line):
    '''
    >>> parse_line('#1 @ 1,3: 4x7')
    Claim(id=1, x=1, y=3, width=4, height=7)
    >>> parse_line('#150 @ 90,952: 15x18')
    Claim(id=150, x=90, y=952, width=15, height=18)
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
    return [parse_line(x) for x in file_data.split()]


# def solve_one(first, second):
#     return ''.join([f for f, s in zip(first, second) if f == s])


# def solve(data):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             result = solve_one(data[i], data[j])
#             if len(result) == len(data[0]) - 1:
#                 return result


def run_test():
    pass

def main(filename):
    print('Day 2 exercise 2!')
    if run_test():
        data = parse(filename)
        print("Result is: {}".format(solve(data)))
    else:
        print('We be fucked')


if __name__ == '__main__':
    name = argv[1]
    filename = 'input_' + name + '.txt'
    main(filename)
