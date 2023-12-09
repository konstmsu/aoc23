from functools import cache
from pathlib import Path
import re

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)

dirs = [{"L": 0, "R": 1}[d] for d in lines[0]]
mapping = {(m := re.findall("[0-9A-Z]+", line))[0]: (m[1], m[2]) for line in lines[2:]}


def part1():
    s = "AAA"
    count = 0
    while s != "ZZZ":
        d = dirs[count % len(dirs)]
        s = mapping[s][d]
        count += 1
        print(s)

    print(f"{count=}")


# part 2


def part2():
    @cache
    def advance(start: str, pointer: int, count: int) -> str:
        s = start
        for i in range(count):
            d = dirs[(pointer + i) % len(dirs)]
            s = mapping[s][d]
            # print(s)

        return s

    @cache
    def dist_to_z(start: str, pointer: int) -> int:
        count = 0
        pos = start
        while True:
            pos = advance(pos, pointer, 1)
            count += 1
            pointer = (pointer + 1) % len(dirs)
            if pos[-1] == "Z":
                return count

    ghosts = [k for k in mapping.keys() if k[-1] == "A"]
    d2 = 0
    pointer = 0
    counter = 0
    while any(g[-1] != "Z" for g in ghosts):
        d = max(dist_to_z(g, pointer) for g in ghosts)
        d2 += d
        counter += 1
        if counter % 100000 == 0:
            print(d2)
        ghosts = [advance(g, pointer, d) for g in ghosts]
        pointer = (pointer + d) % len(dirs)


part2()

# 12926477700000 is too low
