# https://adventofcode.com/2023
import pathlib
import time

from helpers import * 

data_file = pathlib.Path(__file__).parent.joinpath('5.dat')

seed_ranges = []
maps = []
with open(data_file) as f:
    seeds = f.readline().split(':')[-1].strip().split()
    for index in range(0, len(seeds), 2):
        start, length = int(seeds[index]), int(seeds[index + 1])
        seed_ranges.append((start, (start + length) - 1))
    for line in f.readlines():
        if line.count('-') == 2:
            maps.append([])
        elif line.strip():
            dest, source, length = list(map(int, line.split()))
            maps[-1].append([[source, (source + length) - 1], dest - source])


def range_intersection(r1, r2):
    start, end = max(r1[0], r2[0]), min(r1[1], r2[1])
    if start < end:
        return [start, end]


def range_difference(r1, r2):
    intersection = range_intersection(r1, r2)
    if intersection is None:
        return [r1]

    r1_start, r1_end = r1
    int_start, int_end = intersection
    remaining = []
    if int_start != r1_start:
        remaining.append([r1_start, int_start - 1])
    if int_end != r1_end:
        remaining.append([int_end + 1, r1_end])
    return remaining


def apply_rules(rules, ranges):
    ranges_in_mapping = []
    for r1 in ranges:
        for r2, offset in rules:
            intersection = range_intersection(r1, r2)
            if intersection is not None:
                ranges_in_mapping.append([intersection, offset])

    ranges_outside_mapping = ranges
    for (subtract_range, _) in ranges_in_mapping:
        building = []
        for range in ranges_outside_mapping:
            for difference in range_difference(range, subtract_range):
                building.append(difference)
        ranges_outside_mapping = building
    return ranges_outside_mapping + [[start + offset, end + offset] for (start, end), offset in ranges_in_mapping]


start_time = time.time()
for rules in maps:
    seed_ranges = apply_rules(rules, seed_ranges)
print_green(f'{min(seed_ranges)[0]} - took {time.time() - start_time:.5f} seconds')



# weird search attempt, i think this is trash
# # https://adventofcode.com/2023
# import pathlib

# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath('5.dat')


# seed_ranges = []
# maps = []
# with open(data_file) as f:
#     seeds = f.readline().split(':')[-1].strip().split()
#     for seed_index in range(0, len(seeds), 2):
#         start, length = int(seeds[seed_index]), int(seeds[seed_index + 1])
#         seed_ranges.append((start, start + length))
#     for line in f.readlines():
#         line = line.strip()
#         if line.count('-') == 2:
#             maps.append([])
#         elif line:
#             maps[-1].append(list(map(int, line.split())))

# for rules in maps:
#     rules.sort()

# def search(map_index, wanted, wanted_length):
#     if map_index == -1:
#         for start, end in seed_ranges:
#             potential = max(start, wanted)
#             if potential < min(end, wanted + wanted_length):
#                 return potential
#         return float('inf')

#     # print(f'Searching on map {map_index}: Looking for a number in {wanted}-{wanted + wanted_length}')
#     best = float('inf')
#     for dest, source, length in maps[map_index]:
#         offset = dest - source
#         attempt = offset + search(map_index - 1, source, length)
#         if attempt == float('inf'):
#             continue
#         print(f'{map_index} Got {attempt} from {offset}, {best=}, {wanted=}, {wanted_length=}, {dest=}, {source=}, {length=}')
#         if attempt < best:
#             if attempt >= wanted and attempt < wanted + wanted_length:
#                 best = attempt
#     return best

# print(search(len(maps) - 1, 0, float('inf')))