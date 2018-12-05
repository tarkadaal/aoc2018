#!/usr/bin/python3

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
# Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.


from sys import argv

tests = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz',
]

answer = 'fgij'


def parse(filename):
    file_data = open(filename).read()
    return [x for x in file_data.split()]

def solve_one(first, second):
    return ''.join([f for f, s in zip(first, second) if f == s])

def solve(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            result = solve_one(data[i], data[j])
            if len(result) == len(data[0]) - 1:
                return result

def run_test():
    result = solve(tests)
    print(result)
    return answer == result


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
