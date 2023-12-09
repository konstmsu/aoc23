from pathlib import Path
import re

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)

dirs = [{"L": 0, "R": 1}[d] for d in lines[0]]
mapping = {(m := re.findall("[A-Z]+", line))[0]: (m[1], m[2]) for line in lines[2:]}

s = "AAA"
count = 0
while s != "ZZZ":
    d = dirs[count % len(dirs)]
    s = mapping[s][d]
    count += 1
    print(s)

print(f"{count=}")
