from pathlib import Path

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)
maps = []

seeds = [int(v) for v in lines[0].split(": ")[1].split(" ")]
for line in lines[1:]:
    if not line.strip():
        continue
    if "map" in line:
        maps.append([])
    else:
        maps[-1].append([int(v) for v in line.split(" ")])


def get_next(layer: list[int], value: int):
    for t, f, n in layer:
        if f <= value < f + n:
            return t + value - f, f + n - value


def trace(start: int):
    value = start
    for layer in maps:
        nv = get_next(layer, value)
        if nv:
            value = nv[0]
    return value


# print(f"{seeds=}")
# print(f"{maps=}")
best = min(seeds, key=trace)
print(f"{best=}, {trace(best)=}")

# 1 part answer 289863851


def trace2(start: int):
    value = start
    min_ff = 1_000_000_000_000
    for layer in maps:
        nv = get_next(layer, value)
        if nv:
            value = nv[0]
            min_ff = min(min_ff, nv[1])
    return value, min_ff


min_loc = 1_000_000_000_000
for i in range(len(seeds))[::2]:
    f, t = seeds[i : i + 2]
    j = 0
    while j < t:
        v = f + j
        loc, ff = trace2(v)
        min_loc = min(min_loc, loc)
        j += ff

print(f"{min_loc=}")
# part 2 answer is min_loc=60568880
