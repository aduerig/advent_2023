# https://adventofcode.com/2023
import pathlib

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

cards = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            card, rest = line.split(':')
            rest = rest.strip().split('|')
            winning, mine = rest[0].strip().split(), rest[1].strip().split()
            winning = set([int(x) for x in winning])
            mine = [int(x) for x in mine]
            times_won = 0
            for i in mine:
                if i in winning:
                    times_won += 1
            cards.append(times_won)

to_process = [1 for _ in range(len(cards))]
for id in range(len(cards)):
    proc = to_process[id]
    times_won = cards[id]
    for id2 in range(id + 1, id + 1 + times_won):
        to_process[id2] += proc
print(sum(to_process))

# part 1
# # https://adventofcode.com/2023
# import pathlib

# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# total = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if line:
#             card, rest = line.split(':')
#             rest = rest.strip().split('|')
#             winning, mine = rest[0].strip().split(), rest[1].strip().split()
#             winning = set([int(x) for x in winning])
#             mine = [int(x) for x in mine]
#             winners = 0
#             for i in mine:
#                 if i in winning:
#                     winners += 1
#             if winners:
#                 total += pow(2, winners - 1)

# print(total)