# https://adventofcode.com/2023
import pathlib
import time

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')


seed_ranges = []
maps = []
with open(data_file) as f:
    seeds = f.readline().split(':')[-1].strip().split()
    for seed_index in range(0, len(seeds), 2):
        start, length = int(seeds[seed_index]), int(seeds[seed_index + 1])
        seed_ranges.append((start, (start + length) - 1))

    _ = f.readline()
    for line in f.readlines():
        line = line.strip()
        if line.count('-') == 2:
            if maps and len(maps[-1]) != 50: # padding so we can numpy array
                maps[-1] += [(-1, -1, -1)] * (50 - len(maps[-1]))
            maps.append([])
            continue
        elif line:
            nums = list(map(int, line.split()))
            maps[-1].append(nums)
if len(maps[-1]) != 50:
    maps[-1] += [(-1, -1, -1)] * (50 - len(maps[-1]))


total_to_process = 0
for start, end_inclusive in seed_ranges:
    total_to_process += (end_inclusive - start) + 1
print(f'Total seeds to process: {total_to_process:,}')


# attempt at JIT to speed up
import numpy as np
from numba import jit

start_time = time.time()

@jit(nopython=True)
def traverse_maps(maps, state):
    for map in maps:
        for dest, source, length in map:
            if dest == -1:
                break
            offset = state - source
            if offset > -1 and offset < length:
                state = dest + offset
                break
    return state

@jit(nopython=True)
def get_lowest(seed_ranges, maps):
    lowest = 2147483647 # numba doesn't know about float('inf') 
    for start, end_inclusive in seed_ranges:
        for state in range(start, end_inclusive + 1):
            lowest = min(lowest, traverse_maps(maps, state))
    return lowest
print_green(f'Lowest location: {get_lowest(np.array(seed_ranges), np.array(maps))}')
print(f'Took {time.time() - start_time:.2f} seconds')


# part 2 slow (works but is too slow)
# start_time = time.time()
# lowest = float('inf')
# processed = 0
# for seed_range_index, (start, end_inclusive) in enumerate(seed_ranges):
#     print_blue(f'Starting seed range {seed_range_index}/{len(seed_ranges) - 1}')
#     for state in range(start, end_inclusive + 1):
#         if processed % 100000 == 0 and processed > 0:
#             print_yellow(f'Processed {processed:,} nums in {time.time() - start_time:.2f} seconds, {total_to_process - processed:,} remaining, lowest: {lowest}, per second: {processed / (time.time() - start_time):,.0f}, will finish in {((total_to_process - processed) / (processed / (time.time() - start_time))) / 60 / 60:.2f} hours')
#         for map in maps:
#             for dest, source, length in map:
#                 offset = state - source
#                 if offset > -1 and offset < length:
#                     state = dest + offset
#                     break
#         processed += 1
#         lowest = min(lowest, state)
# print_green(f'Lowest location: {lowest}')



# part 1
# # https://adventofcode.com/2023
# import pathlib

# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# maps = []
# with open(data_file) as f:
#     seeds = f.readline().split(':')[-1].strip().split()
#     _ = f.readline()
#     for line in f.readlines():
#         line = line.strip()
#         if line.count('-') == 2:
#             maps.append([])
#             continue
#         elif line:
#             nums = list(map(int, line.split()))
#             maps[-1].append(nums)


# lowest = float('inf')
# for seed_index, state in enumerate(map(int, seeds)):
#     print_blue(f'Starting seed {seed_index}')
#     for map_index, map in enumerate(maps):
#         for dest, source, length in map:
#             offset = state - source
#             if offset > -1 and offset < length:
#                 state = dest + offset
#                 break
#     print_cyan(f'Ending seed {seed_index}, location of {state}')
#     lowest = min(lowest, state)
# print_green(f'Lowest location: {lowest}')