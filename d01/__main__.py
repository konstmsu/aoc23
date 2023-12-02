from pathlib import Path
import re


with open(Path(__file__).parent / "input") as f:
    lines = f.readlines()

# 52155 too low
# 52302 no

s = 0
digits = [
    (d, i + 1)
    for i, d in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    )
] + [(str(i), i) for i in range(1, 10)]
for l in lines:
    l = l.strip()
    print(l)
    first = min(digits, key=lambda s: len(l) if (i := l.find(s[0])) < 0 else i)[1]
    last = max(digits, key=lambda s: l.rfind(s[0]))[1]

    n = first * 10 + last
    print(n)
    s += int(n)

print(s)
