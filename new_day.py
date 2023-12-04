from functools import cached_property
import sys
from datetime import datetime
from pathlib import Path
import requests
import os
import traceback
import webbrowser


class AocWebsite:
    @cached_property
    def _cookies(self):
        return {
            "session": os.environ["ADVENT_OF_CODE_SESSION_COOKIE"],
        }

    def get(self, url: str):
        print(f"GET {url}")
        return requests.get(
            url,
            cookies=self._cookies,
        )


def parse_sample(html: str):
    from bs4 import BeautifulSoup

    doc = BeautifulSoup(html, features="html.parser")

    return doc.select_one("pre > code").text


def extract_sample(year: int, day: int):
    response = AocWebsite().get(f"https://adventofcode.com/{year}/day/{day}")
    html = response.text
    (Path(__file__).parent / "_test_data" / f"sample{year}-{day:02d}.html").write_bytes(
        response.content
    )
    return parse_sample(html)


def main(argv: list[str]):
    year = datetime.today().year
    day = int(argv[1]) if len(argv) == 2 else datetime.today().day
    day_dir = (Path(__file__).parent / f"d{day:02d}").absolute()
    if day_dir.exists():
        print(f"{day_dir} already exists")
        return 1
    day_dir.mkdir(parents=True)
    input_data = AocWebsite().get(
        f"https://adventofcode.com/2023/day/{day}/input",
    )
    (day_dir / "input.txt").write_bytes(input_data.content)
    (day_dir / "__main__.py").write_text(
        """from pathlib import Path
                                       
lines = (Path(__file__).parent / "input.txt").read_text().splitlines(keepends=False)
"""
    )
    try:
        extract_sample(year=year, day=day)
    except:
        traceback.print_exception()
    webbrowser.open(f"https://adventofcode.com/2023/day/{day}")


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
