from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
import re

link_list = ['https://nikkie-project.slack.com/archives/C7ZPKC2RM/p1510391262000028']

@respond_to('だんない')
def thank_you_for_dannnai(message):
    # @Bot だんない に対してお礼を言う
    message.reply('ありがとうございます:taco:')
    message.react('grinning')

@listen_to('はじめまして')
def guide_to_new_menber(message):
    # チャネルに投稿された はじめまして に反応し、
    # アーカイブのリンクを貼ってチャネルの案内をする
    global link_list
    guide = 'このチャネルの使い方はこちらをご覧ください\n'
    guide += '\n'.join(link_list)
    message.reply(guide)

@listen_to('案内.*変更')
@listen_to('案内.*変え')
def how_to_change_guide(message):
    # チャネルに投稿された 案内の変更に関する文言 に反応し、
    # 変更方法の案内をスレッドで返す
    explain_file = open('plugins/explain.txt', 'r')
    explain = explain_file.read()
    index = 0
    current_links = ''
    global link_list
    for link in link_list:
        current_links += '{0} : {1}\n'.format(index, link)
        index += 1
    # 説明文ファイル中のリンクリスト部分に現在のリンクリストを入れる
    explain = explain.format(current_links)
    message.reply(explain, in_thread=True)
