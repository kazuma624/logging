# file_config

## 実行

```sh
$ pwd
/path/to/file_config

$ python app.py
2021/07/23 23:06:06.42  [DEBUG] app.py main: This is debug log
2021/07/23 23:06:06.43  [INFO] app.py main: Start
2021/07/23 23:06:07.45  [INFO] app.py main: Counter: 0
2021/07/23 23:06:08.48  [INFO] app.py main: Counter: 1
2021/07/23 23:06:09.52  [INFO] app.py main: Counter: 2
2021/07/23 23:06:10.52  [INFO] app.py main: Counter: 3
2021/07/23 23:06:11.57  [INFO] app.py main: Counter: 4
2021/07/23 23:06:12.62  [INFO] app.py main: Counter: 5
2021/07/23 23:06:13.67  [INFO] app.py main: Counter: 6
2021/07/23 23:06:14.68  [INFO] app.py main: Counter: 7
2021/07/23 23:06:15.72  [INFO] app.py main: Counter: 8
2021/07/23 23:06:16.76  [INFO] app.py main: Counter: 9
2021/07/23 23:06:16.77  [WARNING] app.py main: Counter: 10 stop
```

## 備考

* 標準出力と log/ 以下にログファイルが出力される
* config/logging.conf の内容を読み込む
    * ファイルの記法は ConfigParser で読み取れる形
* 辞書型で持っている設定値を `logging.config.dictConfig()` で読み込む
* logger オブジェクト生成時に指定したファイル名で、次のルールでローテートする
    * 3ファイルまでバックアップ
    * バックアップファイルの名前は `(元ファイル).YYYY-mm-dd_HH-MM-SS`
    * 5秒おきにファイルを作り替え

この辺りの設定は↓でやっている

```conf
[handler_fileHandler]
class=handlers.TimedRotatingFileHandler
level=DEBUG
formatter=myFormatter
args=('log/example.log',)
kwargs={'backupCount': 3, 'interval': 5, 'when': 'S'}
```
