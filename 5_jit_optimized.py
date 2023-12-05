# https://adventofcode.com/2023
import pathlib
import time

import numpy as np
from numba import jit, prange

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath('5.dat')


seed_ranges = []
maps = []
with open(data_file) as f:
    seeds = f.readline().split(':')[-1].strip().split()
    for seed_index in range(0, len(seeds), 2):
        start, length = int(seeds[seed_index]), int(seeds[seed_index + 1])
        seed_ranges.append((start, start + length))
    for line in f.readlines():
        line = line.strip()
        if line.count('-') == 2:
            maps.append([])
        elif line:
            maps[-1].append(list(map(int, line.split())))

for rules in maps:
    rules.sort(key=lambda x: x[1])

actual_num_rules = [len(rules) for rules in maps]
for index in range(len(maps)):
    maps[index] += [[0, 0, 0]] * (45 - len(maps[index]))

start_time = time.time()

# 41.48 seconds
@jit(nopython=True, parallel=True, fastmath=True, nogil=True)
def get_lowest(actual_num_rules, seed_ranges, maps):
    minimizer = 2147483647
    for seed_range_index in prange(len(seed_ranges)):
        for state in prange(seed_ranges[seed_range_index][0], seed_ranges[seed_range_index][1]):
            for map_index in range(len(maps)):
                for rule_index in range(actual_num_rules[map_index]):
                    relevant = maps[map_index][rule_index]
                    if relevant[1] > state:
                        break
                    if state < relevant[1] + relevant[2]:
                        state += relevant[0] - relevant[1]
                        break
            minimizer = min(minimizer, state)
    return minimizer

ans = get_lowest(np.array(actual_num_rules), np.array(seed_ranges), np.array(maps))
print_green(f'Lowest location: {ans}. Took {time.time() - start_time:.2f} seconds')


# more readable
# 66.21 seconds
# @jit(nopython=True, parallel=True, fastmath=True, nogil=True)
# def get_lowest(actual_num_rules, seed_ranges, maps):
#     minimizer = 2147483647
#     for seed_range_index in prange(len(seed_ranges)):
#         start, end = seed_ranges[seed_range_index]
#         for state in prange(start, end):
#             for map_index, rules in enumerate(maps):
#                 for rule_index in range(actual_num_rules[map_index]):
#                     dest, source, length = rules[rule_index]
#                     if source > state:
#                         break
#                     if state < source + length:
#                         state += dest - source
#                         break
#             minimizer = min(minimizer, state)
#     return minimizer