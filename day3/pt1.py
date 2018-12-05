#!/usr/bin/python3

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2



from sys import argv

tests = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]

answer = 4


def parse_line(line):
    '''
    >>> parse_line('#1 @ 1,3: 4x4')
    
    '''
    pass


def parse(filename):
    file_data = open(filename).read()
    return [x for x in file_data.split()]


def calculate_coords(xpos, ypos, xlength, ylength):
    coord_set = set()
    collision_count = 0

    for (j in range(1, ylength+1))
        for(i in range(1, xlength+1))
            coord = (xpos+i, ypos+j)
            if coord in coord_set
                collision_count += 1;
            else
                coord_set.add()

    return collision_count


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
