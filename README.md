# ちょっとした監視カメラ

### センサーで動くものを検知して写真を撮る

そしてすぐにLINEで写真とともに通知される

### 使い方

監視しておきたい対象の物の近くにサメの口の中に入ったセンサーを近くに置くだけ
動きがあり次第センサーが反応して写真が送られてくる。

### インストールが必要なライブラリ

`import requests`

`import cv2`

### 必要な電子パーツ等

- 超音波センサーHC-SR04
- カモフラージュとなるハード
- Raspberry Pi(今回使用したものはRaspberry Pi4のmodel b)
- 熱を逃がすためのファン
- カメラモジュール(今回使用したものはRasberry Pi Camera V2)
- モバイルバッテリー

### 参考文献

[sozorablog 監視カメラの作り方|Pythonでカメラモジュールを自在に操作](https://sozorablog.com/camera_shooting/)

[sozorablog 【Python入門】LINEに自動でメッセージを送る（活用事例あり）](https://sozorablog.com/pythonline/)

[パソコン工房 Raspberry Piとカメラモジュールを接続する](https://www.pc-koubou.jp/magazine/17276)

[電気設計人.com【ラズパイ電子工作】超音波センサで距離を読み取る方法(HC-SR04)](https://denkisekkeijin.com/raspberrypi/pi-ultrasound/)
