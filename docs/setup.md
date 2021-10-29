
# Setup

```bash
sudo apt install libffi
poetry install --no-dev --no-root
```

## 読みの付与

```bash
cat data/tnc/text/tnc__nezuminoyomeiri.txt \
    | bunkai | sed 's/│/\n/g' | mecab -d ~/local/lib/mecab/dic/unidic-cwj-3.1.0 | poetry run python3 ./scripts/mecab2tsv.py > ./data/tnc/annotation/tnc__nezuminoyomeiri.parsed.tsv
```
