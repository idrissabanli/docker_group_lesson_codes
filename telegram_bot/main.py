import telegram
import requests

def main():
    bot = telegram.Bot(token="1296124970:AAFAlv-Z8g00H_KuKwPBgeJJvXRzNxLiDl0")
    while True:
        echo(bot)

update_id = None

def echo(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if update.message:
            message = update.message.text
            print(message)
            if 'salam' in message:
                update.message.reply_text('Eleykum salam')
            if 'cat' in message.lower():
                sticker = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
                bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker)
 
if __name__ == '__main__':
    main()