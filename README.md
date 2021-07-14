# notion-journal

* notionを便利につかうための自作ツール(予定)

## やりたいこと

* [org-journal](https://github.com/bastibe/org-journal) のように、日ごとの記事を作成したい
* 直前の記事から、完了していないTODOを最新の日に持ち越したい
  * org-journalではファイル間での項目移動だが、notionのSynced Blockで開始日とかにも残しておきたい

## 現状の問題

* まだ全然動いていない
* そもそも、Synced Blockが新機能なので、まだAPIが対応していない……。

## 依存

* [notion-client](https://github.com/ramnes/notion-sdk-py)
* [click(予定)](https://palletsprojects.com/p/click/)
