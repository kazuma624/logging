# logging
logging 周りのサンプル

logging.conf とかファイル出力とかログファイルのローテートなどのサンプルを置いておく

## サンプル集

ディレクトリ名に現れてない分も含め、それぞれテーマをいくつか設けてある

### basic_cofig

* `logging.basicConfig()` でごっそり設定を済ませるパターン

### multi_modules

* 複数モジュールある場合
* 出力先はコンソール

### file_config

* `logging.config.fileConfig()` を使う
* logging.conf から設定値を読み込むパターン

### file_config

* `logging.config.dictConfig()` を使う
* logging.yml から設定値を読み込むパターン
* あくまで辞書型変数から設定値を読み込む機能でしかないので、 YAML ファイルからの読み込みは半分おまけ（外部ライブラリも使うし）

### handler

* コンソールに出力するハンドラーを定義

### time_based_rotation

* コンソールとファイルに出力するハンドラーを定義
* ファイルに出力する方は一定時間ごとにローテートされる

### size_based_rotation

* コンソールとファイルに出力するハンドラーを定義
* ファイルに出力する方は一定容量ごとにローテートされる
