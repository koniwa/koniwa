#!/usr/bin/env python3

from datetime import date
from enum import Enum
from typing import Dict, List, Optional

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


class StatusAnnotation(str, Enum):
    done = "done"
    annotating = "annotating"


class Meta(BaseModel):
    duration: float

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

    status_annotation: Optional[StatusAnnotation]
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


class SubStat(BaseModel):
    duration: float = 0
    duration_done: float = 0
    num_file: int = 0
    num_file_done: int = 0

    def add(self, meta: Meta):
        self.duration += meta.duration
        self.num_file += 1
        if meta.status_annotation == "done":
            self.duration_done += meta.duration
            self.num_file_done += 1


class Stat(BaseModel):
    total: SubStat = SubStat()
    series: Dict[str, SubStat] = {}

    def add(self, name: str, meta: Meta):
        self.total.add(meta)
        if name not in self.series:
            self.series[name] = SubStat()
        self.series[name].add(meta)
