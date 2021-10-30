#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
from typing import List

from pydantic import BaseModel, validator


class Span(BaseModel):
    text_level0: str
    kana_level0: str
    text_level1: str
    text_level2: str
    kana_level2: str
    kana_level3: str
    memo: str


class Annotation(BaseModel):
    start: float
    end: float
    data: Span


class Meta(BaseModel):
    series: str
    album: str
    title: str

    date: str
    speaker: str

    licenser_sound: str
    license_sound: str
    licenser_text: str
    license_text: str

    url: str
    url_sound: str
    note: str

    @validator("license_sound", "license_text")
    def license(cls, v):
        allowed = ["PDM", "CC0 1.0", "CC BY 4.0", "CC BY 3.0", "CC BY 2.1 JP"]
        if v not in allowed:
            raise ValueError(f"Invalid license: {v}")
        return v

    @validator("licenser_sound", "licenser_text")
    def licenser(cls, v):
        if len(v.strip()) == 0:
            raise ValueError(f"Invalid licenser: {v}")
        return v


class Data(BaseModel):
    annotation: List[Annotation]
    meta: Meta


def operation(path_dir: Path, write: bool) -> bool:
    assert path_dir.is_dir()
    ok = True

    for path_in in path_dir.rglob("*.json"):
        try:
            d: Data = Data.parse_file(path_in)
        except Exception as e:
            ok = False
            print(f"{path_in}: {e}")
            continue

        if write:
            with path_in.open("w") as outf:
                outf.write(d.json(ensure_ascii=False, indent=4))
                outf.write("\n")
    return ok


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, required=True)
    oparser.add_argument("--write", "-w", action="store_true")
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    ok: bool = operation(opts.input, opts.write)
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
