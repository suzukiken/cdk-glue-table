+++
title = "GlueでAthena用テーブルを作る"
date = "2021-03-20"
tags = ["Glue", "Athena"]
+++

### テーブルはGlueで作る

Athenaで検索をしたいと思った場合、今までならマネジメントコンソールのAthenaのクエリ入力画面で`CREATE TABLE`してテーブルを作っていた。

それと同じことをCDKでやろうと思ったが、どうもAthenaのテーブルを作る機能が発見できない。

CDKではなくboto3の`start_query_execution`を使えばこんな風にテーブルを作ることができる
```
client.start_query_execution(
  QueryString='CREATE EXTERNAL TABLE...',
  ...
)
```
のだが、他がCDKでここだけboto3かよ、という気持ちもあって、どうすればいいかなあと思って調べたところ、そもそもAthenaのテーブルはGlueで管理するものらしいことがわかった。Athenaはあくまで処理の実行をするところであって、テーブルはGlueに書くの出そうだ。実際、CDKでGlueにテーブルを作るとAWSコンソールのAthenaの画面にテーブルが追加されクエリを実行できる。

[Githubのリポジトリ](https://github.com/suzukiken/cdkgluetable)

サンプルのテーブルは、このような内容のテキストファイルをデータソースとして想定している。
```
{"id": 1, "created": "1974-11-12 06:35:23", "name": "19R O46", "pcs": 8346}
{"id": 2, "created": "2019-01-10 19:25:27", "name": "GHS-5068", "pcs": 2978}
{"id": 3, "created": "1992-05-09 12:28:02", "name": "TAI-782", "pcs": 472}
```

これを適当な名前でテーブルに指定されているS3の場所に放り込むとAthenaで検索ができる。

### Athenaのテーブル名やコラム名の制限に注意:

[参考](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html)

> Table names and table column names in Athena must be lowercase
> Special characters other than underscore (_) are not supported. 
