import sys
from datetime import datetime
from pathlib import Path
import urllib.request


def main(argv: list[str]):
    day = int(argv[1]) if len(argv) == 2 else datetime.today().day
    day_dir = (Path(__file__).parent / f"d{day:02d}").absolute()
    if day_dir.exists():
        print(f"{day_dir} already exists")
        return 1
    day_dir.mkdir(parents=True)
    urllib.request.urlretrieve(
        f"https://adventofcode.com/2023/day/{day}/input", day_dir / "input"
    )


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
