from pathlib import Path
import pytest
from new_day import extract_sample, parse_sample


def test_parse_sample():
    assert (
        parse_sample(
            (Path(__file__).parent / "_test_data" / "sample2023-02.html").read_bytes()
        )
        == (Path(__file__).parent / "d02" / "sample").read_text()
    )


longrun = pytest.mark.skipif("not config.getoption('longrun')")


@longrun
def test_extract_sample():
    assert (
        extract_sample(2023, 2)
        == (Path(__file__).parent / "d02" / "sample").read_text()
    )
    assert (
        extract_sample(2023, 3)
        == (Path(__file__).parent / "d03" / "sample").read_text()
    )
    assert (
        extract_sample(2023, 4)
        == (Path(__file__).parent / "d04" / "sample.txt").read_text()
    )
