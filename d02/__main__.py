from pathlib import Path

lines = (Path(__file__).parent / "input").read_text().splitlines(keepends=False)
# lines = (Path(__file__).parent / "sample").read_text().splitlines(keepends=False)

games = [
    [
        [(int((a := c.split(" "))[0]), a[1]) for c in cs.split(", ")]
        for cs in l.split(": ")[1].split("; ")
    ]
    for l in lines
]

# part 1
ids = 0
for i, game in enumerate(games):
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for s in game:
        for count, color in s:
            maxes[color] = max(maxes[color], count)

    if maxes["red"] <= 12 and maxes["green"] <= 13 and maxes["blue"] <= 14:
        ids += i + 1

print(f"{ids=}")

# part 2
su = 0
for i, game in enumerate(games):
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for s in game:
        for count, color in s:
            maxes[color] = max(maxes[color], count)

    pwr = maxes["red"] * maxes["green"] * maxes["blue"]
    su += pwr

print(f"{su=}")
