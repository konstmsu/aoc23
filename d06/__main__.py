from pathlib import Path
import re

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)
print(f"{lines=}")


def get_numbers(line):
    return [int(v) for v in re.findall("\d+", line)]


tt = get_numbers(lines[0])
dd = get_numbers(lines[1])

print(f"{tt=}, {dd=}")


def count(time: int, distance: int):
    count = 0
    for i in range(time + 1):
        dist = i * (time - i)
        if dist > distance:
            count += 1

    return count


prod = 1
for time, distance in zip(tt, dd):
    prod *= count(time, distance)

print(f"{prod=}")
