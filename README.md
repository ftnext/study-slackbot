## 自習用にPythonでSlack Botを作成(2017/11/11)
### 環境
* Python 3.6.3
* slackbot==0.5.1

### 参考にさせていただいた記事
* [PythonのslackbotライブラリでSlackボットを作る](https://qiita.com/sukesuke/items/1ac92251def87357fdf6)
* [PythonでSlackBOTを作る](http://cppx.hatenablog.com/entry/2017/09/18/214518)
### 手順
* 環境構築
    * slackbotインストール
* Bot用のアカウント準備
    * Slackアカウント作成
    * Legacy Token取得
* Botのコードの初期設定
---
### 手順(2017/11/12)
* 返答の高機能化
    * respond_toの利用
    * listen_toの利用
---
### 手順(2017/11/14)
* Slackの投稿のリンクを使い、案内を表示する機能を実装
    * 案内のカスタマイズ
        * 案内の追加
        * 案内の削除
---
### 手順(2017/11/21)
* SlackアカウントからBot Integrationに切り替え
* herokuにデプロイ
    * 参考[Python × Herokuで作る 雑談slack bot](https://www.slideshare.net/dcubeio/python-heroku-slack-bot)
        * API Tokenを環境変数に設定
        * heroku用設定ファイル作成

*以上をmasterブランチに反映*
