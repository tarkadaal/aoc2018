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

sample_data = [
    [1,3,4,4],
    [3,1,4,4],
    [5,5,2,2]
]

expected_result = 4


def parse_line(line):
    '''
    >>> parse_line('#1 @ 1,3: 4x4')
    
    '''
    pass


def parse(filename):
    file_data = open(filename).read()
    return [x for x in file_data.split()]


def calculate_coords(xpos, ypos, xlength, ylength, coord_set):
    
    collision_count = 0

    for j in range(1, ylength+1):
        for i in range(1, xlength+1):
            coord = (xpos+i, ypos+j)
            if coord in coord_set:
                collision_count += 1;
            else:
                coord_set.add(coord)

    return collision_count

# def solve(data):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             result = solve_one(data[i], data[j])
#             if len(result) == len(data[0]) - 1:
#                 return result
def solve(data):
    coord_set = set()
    total_collision = 0
    for line in data:
        total_collision += calculate_coords(line[0], line[1], line [2], line[3], coord_set)
    
    return total_collision

def run_test():
    return solve(sample_data) == expected_result

def main(filename):
    print('Day 3 exercise 1!')
    if run_test():
        #data = parse(filename)
        #print("Result is: {}".format(solve(data)))
        print('Yay!')
    else:
        print('We be fucked')


if __name__ == '__main__':
    name = argv[1]
    filename = 'input_' + name + '.txt'
    main(filename)
