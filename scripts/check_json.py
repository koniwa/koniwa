#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import List

from pydantic import BaseModel


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


class Data(BaseModel):
    annotation: List[Annotation]
    meta: Meta


def operation(path_dir: Path) -> None:
    assert path_dir.is_dir()

    for path_in in path_dir.rglob("*.json"):
        d: Data = Data.parse_file(path_in)
        with path_in.open("w") as outf:
            outf.write(d.json(ensure_ascii=False, indent=4))
            outf.write("\n")


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, required=True)
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(opts.input)


if __name__ == "__main__":
    main()
