import argparse
import json
import unicodedata
import wave
from pathlib import Path
from typing import Optional

from tqdm import trange
from vosk import KaldiRecognizer, Model, SetLogLevel

from koniwa.schema import Annotation, Span


def data2line(data) -> Optional[str]:
    result = data.get("result")
    if result is None or len(result) == 0:
        return None

    span = Span(
        text_level0=unicodedata.normalize("NFKC", data["text"].replace(" ", "")),
        kana_level0="xxx",
    )
    ant = Annotation(
        start=result[0]["start"],
        end=result[-1]["end"],
        data=span,
    )
    return ant.json(ensure_ascii=False, sort_keys=True)


def writeResult(data, outf):
    if data.get("result") is not None:
        line = data2line(data)
        if line is not None:
            outf.write(line)
            outf.write("\n")


def operation(
    path_in: Path,
    path_model: Path,
    interval: int,
    path_out: Path,
) -> None:
    SetLogLevel(-1)
    with path_out.open("w") as outf, wave.open(str(path_in), "rb") as wf:
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format mono PCM.")
            exit(1)

        model = Model(str(path_model))
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        #         rec.SetPartialWords(True)

        total: int = int(wf.getnframes() / interval)
        for _ in trange(total):
            data = wf.readframes(interval)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                writeResult(json.loads(rec.Result()), outf)
        #     else:
        #                 writeResult(json.loads(rec.PartialResult()), outf)
        writeResult(json.loads(rec.FinalResult()), outf)


def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument("--input", "-i", type=Path, required=True)
    oparser.add_argument("--model", "-m", type=Path, required=True)
    oparser.add_argument("--output", "-o", type=Path, default="/dev/stdout")
    oparser.add_argument("--interval", "-v", type=int, default=4000)
    return oparser.parse_args()


def main() -> None:
    opts = get_opts()
    operation(opts.input, opts.model, opts.interval, opts.output)


if __name__ == "__main__":
    main()
