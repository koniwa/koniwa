#!/usr/bin/env python3

from datetime import date
from enum import Enum
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


class Stat(BaseModel):
    total_duration: float = 0
    total_duration_done: float = 0
    ok: bool = True

    def update(self, meta: Meta):
        self.total_duration += meta.duration
        if meta.status_annotation == "done":
            self.total_duration_done += meta.duration
