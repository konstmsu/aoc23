from collections import defaultdict
from pathlib import Path
import re
from typing import DefaultDict, Dict, List, Set, Tuple

lines = (Path(__file__).parent / "input").read_text().splitlines(keepends=False)

# part 1
lines = ["." + l + "." for l in lines]
empty_line = "." * len(lines[0])
lines = [empty_line] + lines + [empty_line]

# 523641 is too high
s = 0
for i, line in enumerate(lines):
    for match in re.finditer("\\d+", line):
        value = int(match.group())
        start, end = match.span()
        for j in range(i - 1, i + 2):
            adjacent_symbol = re.search("[^0-9.]", lines[j][start - 1 : end + 1])
            if adjacent_symbol:
                break

        if adjacent_symbol:
            s += value

print(f"{s=}")

# part 2
star_numbers: DefaultDict[Tuple[int, int], List[Tuple[int, int]]] = defaultdict(list)
number_values: Dict[Tuple[int, int], int] = dict()

for i, line in enumerate(lines):
    for number in re.finditer("\\d+", line):
        value = int(number.group())
        ns = number.span()
        number_pos = i, ns[0]
        number_values[number_pos] = int(number.group())
        for j in range(i - 1, i + 2):
            for star in re.finditer("\\*", lines[j][ns[0] - 1 : ns[1] + 1]):
                star_pos = j, ns[0] - 1 + star.span()[0]
                star_numbers[star_pos].append(number_pos)

# print(f"{number_values=}")
# print(f"{star_numbers=}")

s = 0
for star_pos, number_poses in star_numbers.items():
    if len(number_poses) == 2:
        s += number_values[number_poses[0]] * number_values[number_poses[1]]

print(f"{s=}")
