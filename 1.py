# https://adventofcode.com/2023
import pathlib

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
with open(data_file) as f:
    s = 0
    for line in f.readlines():
        first = None
        last = '0'
        line = line.strip()
        
        
        for index, c in enumerate(line):
            num = None
            if c.isnumeric():
                num = c
            else:
                rest = line[index:]
                for index, letter in enumerate(l):
                    if rest.startswith(letter):
                        num = str(index + 1)
                        break
            if num:
                if first is None:
                    first = num
                last = num

        if first is None:
            first = '0'

        s += int(first + last)
print(s)


# part 1
# import pathlib

# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# with open(data_file) as f:
#     s = 0
#     for line in f.readlines():
#         first = None
#         last = '0'
#         line = line.strip()
#         for c in line:
#             if c.isnumeric():
#                 if first is None:
#                     first = c
#                 last = c

#         if first is None:
#             first = '0'

#         s += int(first + last)
# print(s)