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
            return t + value - f

def trace(start: int):
    value = start
    for  layer in (maps):
        nv = get_next(layer, value)
        value = value if nv is None else nv
    return value

# print(f"{seeds=}")
# print(f"{maps=}")
best = min(seeds, key=trace)
print(f"{best=}, {trace(best)=}")

# 1 part answer 289863851