
# ASRを利用したアノテーション準備

## text_level0のアノテーション

```bash
# パッケージ準備
poetry install -E asr

# モデルをダウンロードし解凍
# https://alphacephei.com/vosk/models

# wavフォーマットに変換
ffmpeg -i TARGET.mp3 -vn -ac 1 -ar 44100 -acodec pcm_s16le -f wav TARGET.wav

# 音声認識
poetry run python -m koniwa.asr -m ./vosk-model-ja-0.22 -i TARGET.wav -o TARGET.jsonl -v 100
```

生成された``TARGET.jsonl``を使って[Hachiue](https://github.com/koniwa/hachiue)上で修正する．

## kana_level0のアノテーション

- Hachiueからダウンロードしたjsonを使う
