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
    ('abcdef', False, False),
    ('bababc', True, True),
    ('abbcde', True, False),
    ('abcccd', False, True),
    ('aabcdd', True, False),
    ('abcdee', True, False),
    ('ababab', False, True)
]

checksum = 12

def parse(filename):
    file_data = open(filename).read()
    return [x for x in file_data.split()]

def count_chars(data):
    result = {}
    for char in data:
        if char not in result:
            result[char] = 0
        result[char] = result[char] + 1
    return result

def has_two_matching(results):
    return 2 in results.values()

def has_three_matching(results):
    return 3 in results.values()

def solve(data):
    total_two = 0
    total_three = 0
    for line in data:
        counts = count_chars(line)
        if has_two_matching(counts):
            total_two += 1
        if has_three_matching(counts):
            total_three += 1
    return total_three * total_two

def alt_solve(data):
    all_counts = [count_chars(x) for x in data]
    all_twos = [has_two_matching(x) for x in all_counts].count(True)
    all_threes = [has_three_matching(x) for x in all_counts].count(True)
    return all_twos * all_threes

def run_test(test):
    data, expected_two_match, expected_three_match =  test
    counts = count_chars(data)
    actual_two_match = has_two_matching(counts)
    actual_three_match = has_three_matching(counts)
    return actual_two_match == expected_two_match and actual_three_match == expected_three_match

def run_all_tests():
    return all([run_test(x) for x in tests]) and checksum == alt_solve([x[0] for x in tests])


def main(filename):
    print('Day 2 exercise 1!')
    if run_all_tests():
        data = parse(filename)
        print("Result is: {}".format(alt_solve(data)))
    else:
        print('We be fucked')


if __name__ == '__main__':
    name = argv[1]
    filename = 'input_' + name + '.txt'
    main(filename)
