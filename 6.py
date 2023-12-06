# https://adventofcode.com/2023
import pathlib
import time

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

def process(f):
    return int(''.join(f.readline().split(':')[-1].strip().split()))

with open(data_file) as f:
    total_time, dist = process(f), process(f)

start_time = time.time()

def win(dist, total_time, hold_time):
    return bool(hold_time * (total_time - hold_time) > dist)

def binary_search(dist, total_time, want_to_win):
    left, right = 0, total_time - 1
    while left <= right:
        mid = (left + right) // 2
        if not (win(dist, total_time, mid) ^ want_to_win):
            right = mid - 1
        else:
            left = mid + 1
    return left

first_win = binary_search(dist, total_time, True)
last_win = binary_search(dist, total_time, False)
print(last_win - first_win)

# initial part 2 solve, takes 5.9 seconds
# ways = 0
# for hold_time in range(1, total_time):
#     remaining_time = total_time - hold_time
#     distance = hold_time * remaining_time
#     if distance > record:
#         ways += 1
        
# print_green(f'{ways}, took {time.time() - start_time} seconds')


# part 1
# # https://adventofcode.com/2023
# import pathlib

# from helpers import * 

# filepath = pathlib.Path(__file__)
# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# def process(f):
#     return list(map(int, f.readline().split(':')[-1].strip().split()))

# with open(data_file) as f:
#     times, records = process(f), process(f)

# ways = [0 for _ in times]
# for index, (total_time, record) in enumerate(zip(times, records)):
#     for hold_time in range(1, total_time):
#         remaining_time = total_time - hold_time
#         distance = hold_time * remaining_time
#         if distance > record:
#             ways[index] += 1

# product = ways[0]
# for way in ways[1:]:
#     product *= way
# print(product)