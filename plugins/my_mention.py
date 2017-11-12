from slackbot.bot import respond_to     # @botname: で反応するデコーダ

@respond_to('だんない')
def mention_dannnai(message):
    # @Bot だんない に対して返答する
    message.reply('ありがとうございます:taco:')
    message.react('grinning')
