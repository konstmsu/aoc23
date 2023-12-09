from pathlib import Path

from d07 import (
    hand_power,
    hand_power_secondary,
    card_powers,
    result2,
)

lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)
# print(f"{lines=}")

hands = [((p := line.split(" "))[0], int(p[1])) for line in lines]
# print(f"{hands=}")

hands.sort(
    key=lambda h: (hand_power(h[0]), hand_power_secondary(h[0], card_powers)),
    reverse=False,
)
result = sum((i + 1) * h[1] for i, h in enumerate(hands))
# print(f"{result=}")

# 252441121 is too high
# 252431121 is too high
# 251431121 is too high
# 248559379 is correct


# part 2
print(f"{result2(lines)=}")
