#!/usr/bin/env python3

import argparse
import sys
from datetime import date
from pathlib import Path
from typing import List, Optional

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
    album: Optional[str]
    title: str
    chapter_number: Optional[int]
    chapter_name: Optional[str]

    part: Optional[int]

    date: Optional[date]
    speaker: Optional[str]

    licenser_sound: str
    license_sound: str
    licenser_text: str
    license_text: str

    url: str
    url_sound: str

    status_annotation: Optional[str]
    note: str

    @validator("license_sound", "license_text")
    def license(cls, v):
        allowed = ["Public Domain", "CC0 1.0", "CC BY 4.0", "CC BY 3.0", "CC BY 2.1 JP"]
        if v not in allowed:
            raise ValueError(f"Invalid license: {v}")
        return v

    @validator("licenser_sound", "licenser_text")
    def licenser(cls, v):
        if len(v.strip()) == 0:
            raise ValueError(f"Invalid licenser: {v}")
        return v

    @validator("status_annotation")
    def status(cls, v):
        if v is not None:
            if v not in ["annotating", "done"]:
                raise ValueError(f"Invalid status: {v}")
        return v


class Data(BaseModel):
    annotation: List[Annotation]
    meta: Meta

    @validator("meta")
    def status(cls, v, values):
        size_annotation: int = len(values["annotation"])
        if v.status_annotation is None:
            if size_annotation != 0:
                raise ValueError("Size of annotation is not 0")
        else:
            if size_annotation == 0:
                raise ValueError("Size of annotation should not be 0")
        return v


def operation(path_dir: Path, write: bool) -> bool:
    assert path_dir.is_dir()
    ok = True

    for path_in in path_dir.rglob("*.json"):
        with path_in.open() as inf:
            d_raw = inf.read()

        try:
            d: Data = Data.parse_raw(d_raw)
        except Exception as e:
            ok = False
            print(f"{path_in}: {e}")
            continue

        d_formatted = d.json(ensure_ascii=False, indent=4) + "\n"
        if d_raw == d_formatted:
            continue

        if write:
            with path_in.open("w") as outf:
                outf.write(d_formatted)
        else:
            print(f"{path_in}: Not formatted")
            ok = False
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
