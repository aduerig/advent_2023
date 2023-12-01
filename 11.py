# https://adventofcode.com/2023
import pathlib

from helpers import * 

filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')

with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        