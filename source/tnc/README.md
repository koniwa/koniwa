
# source/tnc

## 作成手順

青空文庫で公開されているテキストファイルから以下を除去．

- ヘッダ
- フッタ
- 先頭の空白
- ルビ
- ルビ境界記号``｜``
- 音声中で読み上げられない文字(章番号など)

 そして，[aozora_txt_cleaner](https://github.com/shirayu/aozora_txt_cleaner)でJIS外字指定文字は該当する漢字に置き換えています．
(例: ``※［＃「特のへん＋廴＋聿」、第3水準1-87-71］``→``犍``)

## ライセンス

Public Domain
