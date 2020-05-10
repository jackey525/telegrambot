from telegram.ext import Updater, CommandHandler
from playsound import playsound

def hello(bot, update):
    update.message.reply_text(
        'hello, {}'.format(update.message.from_user.first_name))
    playsound('/Users/jackey/Downloads/song.mp3')

def play(bot, update):
    update.message.reply_text('play now')
    bot.send_audio(chat_id=1071195608, audio=open('/Users/jackey/Downloads/song.mp3', 'rb'))
    #playsound('/Users/jackey/Downloads/song.mp3')

def file_handler(bot, update):
    bot.send_document(chat_id=1071195608, document=open('/Users/jackey/Downloads/GameClient_CDN_List.txt', 'rb'))
    update.message.reply_text('uploadload now')

def download_handler(bot, update):    
    update.message.reply_text('start')
    msg = update.message
    file_id =msg.reply_to_message.document.get_file()    
    file_id.download()
    update.message.reply_text('end')

updater = Updater('1218300637:AAEjauTmz9JaJoodoD3l5Vtq91QoUKp1wr8')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('playsound', play))
updater.dispatcher.add_handler(CommandHandler('upload', file_handler))
updater.dispatcher.add_handler(CommandHandler('qq', download_handler))

updater.start_polling()
updater.idle()
