#!/usr/bin/env python3

import argparse
from pathlib import Path

from schema import Data


def operation(path_in: Path, path_out: Path) -> None:
    d = Data.parse_file(path_in)
    part = []
    for span in d.annotation:
        part.append(span.data.text_level0)
    text = "".join(part).replace("。", "。\n")
    print(text)


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, default="/dev/stdin", required=False)
    oparser.add_argument("--output", "-o", type=Path, default="/dev/stdout", required=False)
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(opts.input, opts.output)


if __name__ == "__main__":
    main()
