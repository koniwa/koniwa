
# 声庭 (Koniwa): An open collection of annotated voices in Japanese language

[![CI](https://github.com/koniwa/koniwa/actions/workflows/ci.yml/badge.svg)](https://github.com/koniwa/koniwa/actions/workflows/ci.yml)
[![CodeQL](https://github.com/koniwa/koniwa/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/koniwa/koniwa/actions/workflows/codeql-analysis.yml)
[![Typos](https://github.com/koniwa/koniwa/actions/workflows/typos.yml/badge.svg)](https://github.com/koniwa/koniwa/actions/workflows/typos.yml)
<br>
[![Progress](https://koniwa.github.io/koniwa/badge/total.progress.svg)](https://koniwa.github.io/koniwa/stat.json)
[![Annotated Duration](https://koniwa.github.io/koniwa/badge/total.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json)

## 概要

声庭 (Koniwa) は利用・修正・再配布が自由でオープンな音声とアノテーションのコレクションです．  
（商用目的での利用も可能です．）

アノテーション作業は始まったばかりです．
皆様のコントリビューションをお待ちしております．

## ファイルリンク

- sound: 音声データ [[Google Drive]](<https://drive.google.com/drive/folders/1edUnYJpT8y0ZmAQSE_fJPQ6VnNBS6qWA>)
- source: 参考データ [[Google Drive]](<https://drive.google.com/drive/folders/1yLZtynAznjVepfAgEVFtbiP0xhCGMmo2>) [[GitHub]](source): 原文などアノテーション時の参考になる資料
- data: 書誌情報・アノテーションデータ [[GitHub]](data)
    - [Schema](koniwa/schema.py)

## シリーズ

本コレクションは現在以下のオープンな音声データを利用しています．
公開に関わってくださった皆様に深く感謝いたします．

| 名前 | 音声ライセンス | テキストライセンス | 概要 | 時期 | アノテーション状況 |
| --- | --- | --- | --- | --- | --- |
| ``amagasaki``<br>[![Duration](https://koniwa.github.io/koniwa/badge/amagasaki.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) | [兵庫県 尼崎市](https://www.city.amagasaki.hyogo.jp/)の[ラジオ番組](https://www.city.amagasaki.hyogo.jp/op_data/1000916/1001317/1001355.html) (FMあまがさき)<br>『いなむら市長の「ひと咲き まち咲き あまがさき」』<br>(2014年11月より『いなむら市長の「い～なこの街 あまがさき」』に改題) | 2011年4月〜2015年11月 | [![Progress](https://koniwa.github.io/koniwa/badge/amagasaki.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/amagasaki.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |
| ``free_culture_2012``<br>[![Duration](https://koniwa.github.io/koniwa/badge/free_culture_2012.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.ja) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.ja) | [J-WAVE](https://www.j-wave.co.jp/)のラジオ番組 [J-WAVE 360° Forum 〜Seek and Find〜](https://soundcloud.com/jwave360) | 2012年8月 | [![Progress](https://koniwa.github.io/koniwa/badge/free_culture_2012.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/free_culture_2012.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |
| ``higashiyodogawa``<br>[![Duration](https://koniwa.github.io/koniwa/badge/higashiyodogawa.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) |[大阪市 東淀川区](https://www.city.osaka.lg.jp/higashiyodogawa/)の[「広報ひがしよどがわ」 音声版](https://www.city.osaka.lg.jp/higashiyodogawa/category/3274-1-0-0-0-0-0-0-0-0.html) | 2017年11月〜2021年7月 | [![Progress](https://koniwa.github.io/koniwa/badge/higashiyodogawa.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/higashiyodogawa.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |
| ``librivox``<br>[![Duration](https://koniwa.github.io/koniwa/badge/librivox.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | Public Domain | Public Domain |[LibriVox.org](https://librivox.org/)の収録作品<br>歌など一部のものは除外している | - | [![Progress](https://koniwa.github.io/koniwa/badge/librivox.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/librivox.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |
| ``minato``<br>[![Duration](https://koniwa.github.io/koniwa/badge/minato.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) |[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) | [大阪市 港区](https://www.city.osaka.lg.jp/minato/)の[「広報みなと」 音声版](https://www.city.osaka.lg.jp/minato/category/3179-4-0-0-0-0-0-0-0-0.html) | 2019年5月〜2020年12月 | [![Progress](https://koniwa.github.io/koniwa/badge/minato.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/minato.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |
| ``nishiyodogawa``<br>[![Duration](https://koniwa.github.io/koniwa/badge/nishiyodogawa.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) | [大阪市 西淀川区](https://www.city.osaka.lg.jp/nishiyodogawa/)の[『広報紙「きらり☆にしよど」 音声版』](https://www.city.osaka.lg.jp/nishiyodogawa/category/3258-6-0-0-0-0-0-0-0-0.html)| 2018年8月〜2021年7月 | [![Progress](https://koniwa.github.io/koniwa/badge/nishiyodogawa.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/nishiyodogawa.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |
| ``roudoku_toshokan``<br>[![Duration](https://koniwa.github.io/koniwa/badge/roudoku_toshokan.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | [CC BY 2.1 JP](https://creativecommons.org/licenses/by-sa/2.1/jp/) | Public Domain | [池田英生氏](http://nergui.sakura.ne.jp/who.html)の[朗読図書館](http://nergui.sakura.ne.jp/library.html)配信の朗読音声 | - | [![Progress](https://koniwa.github.io/koniwa/badge/roudoku_toshokan.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/roudoku_toshokan.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |
|``tnc``<br>[![Duration](https://koniwa.github.io/koniwa/badge/tnc.duration_total.svg)](https://koniwa.github.io/koniwa/stat.json) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.ja) | Public Domain | [テレビ西日本](https://www.tnc.co.jp/)のアナウンサーによる[朗読音声](https://www.tnc.co.jp/forchildren/roudoku) | 2020年3月 | [![Progress](https://koniwa.github.io/koniwa/badge/tnc.progress.svg)](https://koniwa.github.io/koniwa/stat.json)<br>[![Annotated Duration](https://koniwa.github.io/koniwa/badge/tnc.duration_done.svg)](https://koniwa.github.io/koniwa/stat.json) |

## Licence

## 原文・音声のライセンス

本コレクション内の音声は以下のいずれかでライセンスされているもののみを含めることにしています．

- パブリックドメイン
    - Public Domain
    - CC0
- クリエイティブ・コモンズ
    - CC BY

## アノテーションや文書のライセンス

以下は全て[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)でライセンスします

- 二次的著作物に該当するアノテーションのうち二次的著作部分
- アノテーションのコメント・アノテーションマニュアルなどの本レポジトリ内の一次著作物（プログラムを除く）

## プログラムのライセンス

プログラムはApache License 2.0でライセンスします．

## Maintainer

- [shirayu](https://github.com/shirayu)
