# https://adventofcode.com/2023
import pathlib

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
            nums = list(map(int, line.split()))
            maps[-1].append(nums)


def search(map_index, wanted, wanted_length):
    if map_index == -1:
        for start, end in seed_ranges:
            if wanted >= start and wanted < end:
                return wanted
        return float('inf')

    print(f'Searching on map {map_index}: Looking for a number in {wanted}-{wanted + wanted_length}')
    best = float('inf')
    for dest, source, length in maps[map_index]:
        offset = dest - source
        attempt = offset + search(map_index - 1, source, length)
        if attempt >= wanted and attempt < wanted + wanted_length and attempt < best:
            best = attempt
    return best

print(search(len(maps) - 1, 0, float('inf')))