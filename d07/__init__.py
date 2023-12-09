from collections import Counter
from typing import Generator


def hand_power(hand: str):
    match sorted(Counter(hand).values(), reverse=True):
        case [5]:
            return 10
        case [4, 1]:
            return 9
        case [3, 2]:
            return 8
        case [3, *_]:
            return 7
        case [2, 2, *_]:
            return 6
        case [2, *_]:
            return 5
    return 4


card_powers = "AKQJT98765432"
card_powers2 = "AKQT98765432J"


def hand_power2(hand: str) -> int:
    if "J" not in hand:
        return hand_power(hand)

    def options() -> Generator[str, None, None]:
        popularity = Counter(hand).most_common(5)
        for card, count in popularity:
            h = hand.replace("J", card)
            yield h

    best = max(options(), key=lambda h: hand_power(h))
    print(f"{hand=}, {best=}")
    return hand_power(best)


def hand_power_secondary(hand: str, card_by_power_desc: str) -> tuple[int, ...]:
    pp = list(reversed(card_by_power_desc))
    return tuple(pp.index(h) for h in hand)


def compare_equal_power(aa: str, bb: str) -> int:
    if hand_power(aa) != hand_power(bb):
        raise ValueError(f"{aa=} {bb=}")
    return (
        1
        if hand_power_secondary(aa, card_powers) > hand_power_secondary(bb, card_powers)
        else -1
    )


def result2(input: list[str]) -> int:
    hands = [((p := line.split(" "))[0], int(p[1])) for line in input]
    hands.sort(
        key=lambda h: (hand_power2(h[0]), hand_power_secondary(h[0], card_powers2)),
        reverse=False,
    )
    print("hands")
    print("\n".join(map(str, hands)))
    result = sum((i + 1) * h[1] for i, h in enumerate(hands))
    return result
