#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

from schema import Annotation, Span


def operation(path_in: Path, path_out: Path, offset: float, only_print: bool) -> None:
    with path_in.open() as inf, path_out.open("w") as outf:
        for paragraph in json.load(inf)[0]:
            pdata = paragraph[0]
            buf = ""
            buf_start = None

            for idx, part in enumerate(pdata):
                m = part[1]
                if m is None:
                    m = part[0]
                m = m.strip()
                if only_print:
                    outf.write(m)
                    continue

                start = int(part[2]) / 1000 + offset
                end = int(part[3]) / 1000 + offset

                buf += m
                if buf_start is None:
                    buf_start = start
                if ("、" not in m and "。" not in m) and idx != len(pdata) - 1:
                    continue

                ant = Annotation(
                    start=buf_start,
                    end=end,
                    data=Span(
                        text_level0=buf,
                        kana_level0="xx",
                    ),
                )

                buf = ""
                buf_start = None

                outf.write(json.dumps(ant.dict(), ensure_ascii=False))
                outf.write(",\n")


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, default="/dev/stdin", required=False)
    oparser.add_argument("--output", "-o", type=Path, default="/dev/stdout", required=False)
    oparser.add_argument("--offset", type=float, default=0.0)
    oparser.add_argument("--print", action="store_true")
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(opts.input, opts.output, opts.offset, opts.print)


if __name__ == "__main__":
    main()
