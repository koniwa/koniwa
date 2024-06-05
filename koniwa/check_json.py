#!/usr/bin/env python3

import argparse
import json
import sys
import traceback
from pathlib import Path

from koniwa.schema import Data, Stat


def operation(path_dir: Path, write: bool) -> tuple[Stat, bool]:
    assert path_dir.is_dir()

    stat = Stat()
    ok: bool = True

    def get_series_name(path_json, path_root) -> str:
        cand: Path = path_json.parent
        while cand.parent != path_root:
            cand = cand.parent
        return cand.name

    for path_in in path_dir.rglob("*.json"):
        with path_in.open() as inf:
            d_raw = inf.read()

        try:
            d: Data = Data.model_validate_json(d_raw)
        except Exception as e:
            ok = False
            print(f"{path_in}: {e}")
            print(traceback.format_exc())
            continue

        series_name: str = get_series_name(path_in, path_dir)
        stat.add(series_name, d.meta)

        d_formatted = (
            json.dumps(
                json.loads(d.model_dump_json()),
                ensure_ascii=False,
                indent=4,
            )
            + "\n"
        )
        if d_raw == d_formatted:
            continue

        if write:
            with path_in.open("w") as outf:
                outf.write(d_formatted)
        else:
            print(f"{path_in}: Not formatted")
            ok = False
    return stat, ok


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, required=True)
    oparser.add_argument("--output", "-o", default="/dev/stdout", type=Path)
    oparser.add_argument("--write", "-w", action="store_true")
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    stat, ok = operation(opts.input, opts.write)

    with opts.output.open("w") as outf:
        outf.write(
            json.dumps(
                stat.model_dump(),
                ensure_ascii=False,
                indent=4,
            )
            + "\n"
        )

    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
