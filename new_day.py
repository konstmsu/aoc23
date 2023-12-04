import logging
import zoneinfo
import os
import subprocess
import sys
import traceback
import webbrowser
from datetime import datetime
from functools import cached_property
from pathlib import Path

import requests
import structlog

logger = structlog.get_logger()


class AocWebsite:
    @cached_property
    def _cookies(self):
        return {
            "session": os.environ["ADVENT_OF_CODE_SESSION_COOKIE"],
        }

    def get(self, url: str):
        logger.debug(f"GET {url}")
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
    return parse_sample(response.text)


def main():
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    )
    now = datetime.now(zoneinfo.ZoneInfo("EST"))
    year = now.year
    day = now.day
    day_dir = (Path(__file__).parent / f"d{day:02d}").absolute()
    if day_dir.exists():
        logger.warning(f"{day_dir} already exists")
        return 1
    day_dir.mkdir(parents=True)
    input_data = AocWebsite().get(f"https://adventofcode.com/2023/day/{day}/input")
    input_txt = day_dir / "input.txt"
    input_txt.write_bytes(input_data.content)
    logger.info(f"Written {input_txt}")
    main_py = day_dir / "__main__.py"
    main_py.write_text(
        """from pathlib import Path
                                       
lines = (Path(__file__).parent / "sample.txt").read_text().splitlines(keepends=False)
print(f"{lines=}")
"""
    )
    logger.info(f"Created {main_py}")
    subprocess.run(["open", main_py], check=True)
    try:
        sample_txt = day_dir / "sample.txt"
        sample_txt.write_text(extract_sample(year=year, day=day))
        logger.info(f"Written {sample_txt}")
    except:
        traceback.print_exception()
    webbrowser.open(f"https://adventofcode.com/2023/day/{day}")


if __name__ == "__main__":
    sys.exit(main() or 0)
