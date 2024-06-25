#!/usr/bin/env python3

import argparse
import bisect
import csv
import json
from pathlib import Path


class Parsed:
    def __init__(self, d: list[list[str]]):
        self.offsets: list[int] = []
        self.surfs: list[str] = []
        self.readings: list[str] = []
        self.pronunces: list[str] = []

        offset = 0
        for items in d:
            self.offsets.append(offset)
            assert len(items[0]) > 0
            assert len(items) == 3, items
            surf: str = items[0]
            offset += len(surf)

            self.surfs.append(surf)
            self.readings.append(items[1])
            self.pronunces.append(items[2])

    def get(self, offset: int, surf: str) -> tuple[str, str]:
        idx: int = bisect.bisect_left(self.offsets, offset)
        length = len(surf)
        cnt: int = 0
        rest: int = length
        while rest > 0:
            rest -= len(self.surfs[idx + cnt])
            cnt += 1
        assert rest == 0, (offset, surf, rest)
        surf_got: str = "".join(self.surfs[idx : idx + cnt])
        assert surf_got == surf, f"{surf} != {surf_got}"
        return (
            "".join(self.readings[idx : idx + cnt]),
            "".join(self.pronunces[idx : idx + cnt]),
        )


def operation(path_in: Path, path_parsed: Path, path_out: Path) -> None:
    with path_parsed.open() as inf:
        tmp: list[list[str]] = []
        r = csv.reader(inf, delimiter="\t")
        for items in r:
            if len(items) == 1 and items[0] == "EOS":
                continue
            tmp.append(items)
        parsed = Parsed(tmp)

    with path_in.open() as inf:
        d = json.load(inf)

    offset: int = 0
    for item in d["annotation"]:
        s = item["data"]["text_level0"]
        if len(s) == 0:
            continue

        _, pron = parsed.get(offset, s)
        offset += len(s)
        item["data"]["kana_level0"] = pron

    with path_out.open("w") as outf:
        outf.write(json.dumps(d, ensure_ascii=False, indent=2))
        outf.write("\n")


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, required=True)
    oparser.add_argument("--parsed", "-p", type=Path, required=True)

    oparser.add_argument("--output", "-o", type=Path, default="/dev/stdout", required=False)
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(opts.input, opts.parsed, opts.output)


if __name__ == "__main__":
    main()
