import random
from d07 import compare_equal_power, hand_power, card_powers, hand_power2, result2
from pathlib import Path


def test_compare_equal_power():
    assert compare_equal_power("33332", "2AAAA") > 0
    assert compare_equal_power("77888", "77788") > 0
    assert compare_equal_power("QQQJA", "T55J5") > 0


def test_compare_equal_power2():
    for a, b in zip(card_powers, card_powers[1:]):
        assert compare_equal_power(a, b) > 0
        assert compare_equal_power(b, a) < 0
        if a != "K" and b != "K":
            assert compare_equal_power(f"K{a}", f"K{b}") > 0
            assert compare_equal_power(f"K{a}", f"A{b}") < 0


def test_power():
    assert hand_power("AAAAA") == 10
    assert hand_power("AA8AA") == 9
    assert hand_power("23332") == 8
    assert hand_power("TTT98") == 7
    assert hand_power("23432") == 6
    assert hand_power("A23A4") == 5
    assert hand_power("23456") == 4

    assert hand_power("Q2Q2Q") == 8
    assert hand_power("QQQJA") == 7


def test_power2():
    for _ in range(1000):
        hand = "".join(random.choices(card_powers, k=5))
        print(f"{hand_power(hand)=}")
        print(f"{hand_power2(hand)=}")
        assert hand_power(hand) <= hand_power2(hand)


def test_result2():
    def lines(test_name: str):
        return (
            (Path(__file__).parent / test_name).read_text().splitlines(keepends=False)
        )

    assert result2(lines("sample.txt")) == 5905
    assert result2(lines("sample2.txt")) == 6839
