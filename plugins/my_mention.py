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
@respond_to('いま|今|現在.*案内')
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
    # 説明文ファイル中に現在の案内リストを入れる
    explain = explain.format(current_links)
    message.reply(explain, in_thread=True)

@respond_to('案内.*追加')
def add_link_list(message):
    global link_list
    if len(link_list) == 3:
        reply_msg = '案内リストが3件あり、これ以上追加できません'
    else: # len(link_list) <= 2
        text = message.body['text']
        # リンクの前にスペースを含ませるよう案内しているので、スペースで分割する
        splited_text = text.strip().split(' ')
        if len(splited_text) <= 1:
            reply_msg = 'リンクが含まれていないようです。案内リストに追加できませんでした'
        elif len(splited_text) >= 3:
            reply_msg = '複数のリンクが渡されたようです。申し訳ありませんが、一度に一つしか追加できません'
        else: # len(splited_text) == 2
            add_link = splited_text[1]
            # add_linkは<url>という形式になっている
            # リンクがteam内の投稿かどうか確認する
            assumed_pattern = '<https://nikkie-project.slack.com/archives/'
            if not assumed_pattern in add_link:
                reply_msg = 'このteam内のリンクではないようです。このteamの投稿のリンクにしてください'
            else:
                #<url>という形式から先頭の<と末尾の>を除く
                add_link = add_link[1:len(add_link)-1]
                link_list.append(add_link)
                reply_msg = '案内リストに追加しました'
    message.reply(reply_msg, in_thread=True)

@respond_to('案内.*削除')
def delete_link_from_list(message):
    global link_list
    if len(link_list) == 0:
        reply_msg = '案内リストは0件です。削除できません'
    else: # len(link_list) >= 1 and len(link_list) <= 3
        text = message.body['text']
        # 削除する数字番号の前にスペースを含ませるように案内しているので、スペースで分割する
        splited_text = text.strip().split(' ')
        if len(splited_text) <= 1:
            reply_msg = '削除するリンクが指定されていないようです。削除できませんでした'
        elif len(splited_text) >= 3:
            reply_msg = '複数のリンクが指定されたようです。申し訳ありませんが、一度に一つしか削除できません'
        else: # len(splited_text) == 2
            delete_link_no = splited_text[1]
            if not isinstance(delete_link_no, int):
                reply_msg = '削除するリンクが整数で指定されていないようです。整数値で指定してください'
            else: # isinstance(delete_link_no, int) = True
                # リストの範囲外のリンクが指定された場合
                if int(delete_link_no) > len(link_list):
                    reply_msg = '指定したリンクはありません。0から{}の間の整数で指定してください'.format(len(link_list)-1)
                else:
                    link_list.pop(int(delete_link_no)-1)
                    reply_msg = '案内リストから削除しました'
    message.reply(reply_msg, in_thread=True)
