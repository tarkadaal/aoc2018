#!/usr/bin/python3
from sys import argv


tests = [
    ([+1, -2, +3, +1], 3),
    ([+1, +1, +1], 3),
    ([+1, +1, -2], 0),
    ([-1, -2, -3], -6)
]

def parse(filename):
    file_data = open(filename).read()
    return [int(x) for x in file_data.split()]

def solve(data):
    result = 0
    for number in data:
        result = result + number
    return result

def run_test(test):
    return solve(test[0]) == test[1]

def run_all_tests():
    return all([run_test(x) for x in tests])

def main(filename):
    print('Day 1 exercise 1!')
    if run_all_tests():
        data = parse(filename)
        print("Result is: {}".format(solve(data)))
    else:
        print('We be fucked')

if __name__ == '__main__':
    name = argv[1]
    filename = 'input_' + name + '.txt'
    main(filename)

