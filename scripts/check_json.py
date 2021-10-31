#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

from schema import Data, Stat


def operation(path_dir: Path, write: bool) -> Stat:
    assert path_dir.is_dir()

    stat = Stat()

    for path_in in path_dir.rglob("*.json"):
        with path_in.open() as inf:
            d_raw = inf.read()

        try:
            d: Data = Data.parse_raw(d_raw)
        except Exception as e:
            stat.ok = False
            print(f"{path_in}: {e}")
            continue

        stat.update(d.meta)

        d_formatted = d.json(ensure_ascii=False, indent=4) + "\n"
        if d_raw == d_formatted:
            continue

        if write:
            with path_in.open("w") as outf:
                outf.write(d_formatted)
        else:
            print(f"{path_in}: Not formatted")
            stat.ok = False
    return stat


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, required=True)
    oparser.add_argument("--output", "-o", default="/dev/stdout", type=Path)
    oparser.add_argument("--write", "-w", action="store_true")
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    stat: Stat = operation(opts.input, opts.write)

    with opts.output.open("w") as outf:
        outf.write(stat.json(ensure_ascii=False, indent=4) + "\n")

    if not stat.ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
