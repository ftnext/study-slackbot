import os

# Bot IntegrationのAPI Tokenを環境変数に指定している
API_TOKEN = os.environ["API_TOKEN"]

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "抹茶！"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
