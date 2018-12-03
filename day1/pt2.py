#!/usr/bin/python3
from sys import argv
from functools import reduce


tests = [
    ([+1, -2, +3, +1], 2),
    ([+1, -1], 0),
    ([+3, +3, +4, -2, -4], 10),
    ([-6, +3, +8, +5, -6], 5),
    ([+7, +7, -2, -7, -4], 14),
]


def parse(filename):
    file_data = open(filename).read()
    return [int(x) for x in file_data.split()]



def solve(data):
    result = 0
    i = 0
    s = set([0])
    while True:
        index = i % len(data)
        number = data[index]
        result = result + number
        if result in s:
            print(result)
            return result
        s.add(result)
        i = i + 1


def run_test(test):
    return solve(test[0]) == test[1]


def run_all_tests():
    return all([run_test(x) for x in tests])


def main(filename):
    print('Day 1 exercise 2!')
    if run_all_tests():
        data = parse(filename)
        print("Result is: {}".format(solve(data)))
    else:
        print('We be fucked')


if __name__ == '__main__':
    name = argv[1]
    filename = 'input_' + name + '.txt'
    main(filename)
