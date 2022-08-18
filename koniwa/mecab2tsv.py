#!/usr/bin/env python3

import argparse
import csv
from pathlib import Path


def operation(path_in: Path, path_out: Path) -> None:
    with path_in.open() as inf, path_out.open("w") as outf:
        r = csv.reader(inf)
        for items in r:
            if len(items) == 1:
                outf.write("EOS\n")
                continue

            surf: str = items[0].split("\t")[0]
            furigana: str = "xx"
            if len(items) > 21:
                furigana = items[22]  # 仮名形出現形
                if len(furigana) == 0:
                    furigana = surf

            pron: str = "xx"
            if len(items) > 9:
                pron: str = items[9]  # 発音形出現形
                if len(pron) == 0:
                    pron = surf

            outf.write(f"{surf}\t{furigana}\t{pron}\n")


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
