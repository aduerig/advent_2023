# https://adventofcode.com/2023
import pathlib

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')



def possible(first, id):
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for s in ok.strip().split(';'):
        for thing in s.split(','):
            num, color = thing.strip().split(' ')
            colors[color] = max(colors[color], int(num))
    return colors['red'] * colors['green'] * colors['blue']


lol = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            first, ok = line.split(':')
            _, id = first.strip().split(' ')
            g = possible(first, id)
            print(g)
            lol += g
print(lol)



# part 1
# https://adventofcode.com/2023
# import pathlib

# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# colors = {
#     'red': 12,
#     'green': 13,
#     'blue': 14,
# }

# def possible(first, id):
#     for s in ok.strip().split(';'):
#         for thing in s.split(','):
#             num, color = thing.strip().split(' ')
#             if colors[color] < int(num):
#                 return 0
#     return int(id)


# lol = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             first, ok = line.strip(':')
#             _, id = first.strip().split(' ')
#             lol += possible(first, id)
# print(lol)