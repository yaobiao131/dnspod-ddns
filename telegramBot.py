import logging
from telegram import Bot
from config import read_config, cfg

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def send_message(message):
    bot = Bot(token=cfg['telegram_bot_api_token'])
    bot.send_message(cfg['telegram_chat_id'], message)


def main():
    read_config()


if __name__ == '__main__':
    main()
