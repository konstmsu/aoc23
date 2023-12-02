import sys
from datetime import datetime
from pathlib import Path
import requests
import os


def main(argv: list[str]):
    day = int(argv[1]) if len(argv) == 2 else datetime.today().day
    day_dir = (Path(__file__).parent / f"d{day:02d}").absolute()
    if day_dir.exists():
        print(f"{day_dir} already exists")
        return 1
    day_dir.mkdir(parents=True)
    input_data = requests.get(
        f"https://adventofcode.com/2023/day/{day}/input",
        cookies={"session": os.environ["ADVENT_OF_CODE_SESSION_COOKIE"]},
    )
    (day_dir / "input").write_bytes(input_data.content)


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
