from pathlib import Path

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)

nums = [[int(v) for v in line.split(" ")] for line in lines]


def part1():
    def process(line: list[int]):
        print(f"Starting {line}")

        vv = [list(line)]
        while any(v != 0 for v in vv[-1]):
            vv.append([b - a for a, b in zip(vv[-1], vv[-1][1:])])

        for i in reversed(range(len(vv) - 1)):
            vv[i].append(vv[i + 1][-1] + vv[i][-1])

        for line in vv:
            print(line)

        return vv

    result = sum(process(nn)[0][-1] for nn in nums)
    print(f"{result=}")


part1()
