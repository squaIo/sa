# ちょっとした監視カメラ



### 必要な電子パーツ等

- 超音波センサーHC-SR04
- カモフラージュとなるハード
- Raspberry Pi(今回使用したものはRaspberry Pi4のmodel b)
- 熱を逃がすためのファン
- カメラモジュール(今回使用したものはRasberry Pi Camera V2)
- モバイルバッテリー


### カメラモジュールを使う際の注意


> Raspberry Piの中でカメラを有効にする

1. デスクトップから"設定"をクリック
1. "Raspberry Piの設定"
1. "インターフェイス"
1. "カメラ"
1. "OK"を押して設定が完了


> Raspberry pi本体とカメラモジュールをつなぐ際にリボンケーブルを挿し込む向きに気を付ける

1. Raspberry Piの黒いロック部分を持ち上げる
1. 黒いロック部分にリボンケーブルの裏側が来るように挿し込む(端子がHDMIポート側に来る)
1. リボンケーブルを挿し込んだら持ち上げた黒いロックを押し込む

> ライブラリーのライブラリーのインストール

Pythonで画像を扱うために、"Open CV"というライブラリーをラズパイにインストールする。

ターミナルを開いてコマンドを一行ずつ実行していく

1. pipを最新のバージョンに

`sudo python -m pip install --upgrade pip`

2. OpenCVをバージョン指定でインストール

`sudo pip3 install opencv-python==4.5.1.48`

3. numpyライブラリを最新に

`pip install -U numpy`

パッケージリストを最新に

`sudo apt update`

「libatlas3-base」 パッケージをインストール

`sudo apt install libatlas3-base`

