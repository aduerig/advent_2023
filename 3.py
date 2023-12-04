# https://adventofcode.com/2023
import pathlib
import regex

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

grid = []
with open(data_file) as f:
    for line in f.readlines():
        grid.append(line.strip())

symbols = {}
def next_to(x1, x2, y):
    added = set()
    for x in range(x1, x2):
        for n_x, n_y in [(x, y-1), (x, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)]:
            if n_x < 0 or n_y < 0 or n_x >= len(grid) or n_y >= len(grid) or (n_y, n_x) in added:
                continue
            if grid[n_y][n_x] == '*':
                added.add((n_y, n_x))
                if (n_y, n_x) not in symbols:
                    symbols[(n_y, n_x)] = []
                symbols[(n_y, n_x)].append(int(grid[y][x1:x2]))


for y in range(len(grid)):
    for occurence in regex.finditer(r'\d+', grid[y]):
        x1, x2 = occurence.start(), occurence.end()
        next_to(x1, x2, y)

total = 0
for sym in symbols.values():
    if len(sym) == 2:
        total += sym[0] * sym[1]
print(total)


# part 1
# # https://adventofcode.com/2023
# import pathlib
# import regex


# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# field = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         field.append(line)


# def is_symbol(s):
#     return not s.isnumeric() and not s == '.'

# def next_to(field, x1, x2, y):
#     for x in range(x1, x2):
#         for n_x, n_y in [(x, y-1), (x, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)]:
#             if n_x < 0 or n_y < 0 or n_x >= len(field) or n_y >= len(field):
#                 continue
            
#             if is_symbol(field[n_y][n_x]):
#                 return True
#     return False

# total = 0
# for y in range(len(field)):
#     for match in regex.finditer(r'\d+', field[y]):
#         x1, x2 = match.start(), match.end()
#         if next_to(field, x1, x2, y):
#             total += int(field[y][x1:x2])
# print(total)