# handler

## 実行

```sh
$ pwd
/path/to/handler

$ python app.py
2021/07/23 23:41:21.510 [DEBUG] app.py main: This is debug log
2021/07/23 23:41:21.510 [INFO] app.py main: Started
2021/07/23 23:41:21.510 [WARNING] app.py main: Some warining
2021/07/23 23:41:21.510 [INFO] app.py main: Finished
```

## 備考

* ハンドラを定義する
* 出力先を複数設定して振り分ける際に、主に利用する
* ここでは出力先は一つだけなので、特に使うメリットはない（デメリットもない）
