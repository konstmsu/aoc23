from pathlib import Path
import re

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)

s = 0

for line in lines:
    parts: list[str] = re.split("[:|]", line)
    winning = [int(v) for v in re.findall("\d+", parts[1])]
    have = {int(v) for v in re.findall("\d+", parts[2])}
    print(f"{winning=}, {have=}")
    points = 0
    for h in have:
        if h in winning:
            points = (points * 2) or 1
            print(f"{h=} in {winning=} so {points=}")
    s += points

print(s)
