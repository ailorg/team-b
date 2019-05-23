PSI-Basic

# 初期設定
パッケージのインストール
```
$ npm install
$ pip install flask
```
 
# 起動方法
ファイルに変更があるたびにビルド
```
$ npm run watch
```
Flaskを開始
```
$ FLASK_APP=app.py FLASK_DEBUG=1 flask run
```
Windowsの場合
```
$ set FLASK_APP=app.py
$ set FLASK_DEBUG=1
$ flask run
```

# その他
webpackerでサーバー起動 （ブラウザに localhost:8080 と入力）
```
$ npm run dev
```

ビルドして本番環境を用意
```
$ npm run build
```