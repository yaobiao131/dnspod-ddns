import logging
from telegram import Bot
from telegram.utils import request
from config import read_config, save_config, check_config, cfg

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def send_message(message):
    request1 = request.Request(1, 'http://127.0.0.1:7890')
    bot = Bot(token=cfg['telegram_bot_api_token'], request=request1)
    bot.send_message(cfg['telegram_chat_id'], message)


def main():
    read_config()


if __name__ == '__main__':
    main()
