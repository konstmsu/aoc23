from pathlib import Path
import re

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)

s = 0

for line in lines:
    parts: list[str] = re.split("[:|]", line)
    winning = [int(v) for v in re.findall("\\d+", parts[1])]
    have = {int(v) for v in re.findall("\\d+", parts[2])}
    # print(f"{winning=}, {have=}")
    points = 0
    for h in have:
        if h in winning:
            points = (points * 2) or 1
            # print(f"{h=} in {winning=} so {points=}")
    s += points

# print(s)

s = 0

winnings: list[set[int]] = []
haves: list[set[int]] = []
for line in lines:
    parts: list[str] = re.split("[:|]", line)
    winnings.append({int(v) for v in re.findall("\\d+", parts[1])})
    haves.append({int(v) for v in re.findall("\\d+", parts[2])})


n = len(lines)
matches = [0] * n

for i in range(n):
    for h in haves[i]:
        if h in winnings[i]:
            matches[i] += 1

ss = [[1] * n]

while any(ss[-1]):
    ss.append([0] * n)
    for i in range(n):
        for j in range(i + 1, i + matches[i] + 1):
            ss[-1][j] += ss[-2][i]

s = sum([sum(s) for s in ss])
print(f"{s=}")
# 9425061 is correct
