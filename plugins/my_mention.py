from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ

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
