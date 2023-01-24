import os
from time import time
import telebot
from telebot.handler_backends import BaseMiddleware
import threading as thr
from mss import mss, tools
import pyautogui as pg
from telebot import types

try:
    from dotenv import load_dotenv  # pip install python-dotenv
    load_dotenv()
except ImportError:
    pass  # fall back to variables exported in the shell


class Middleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message']

    def pre_process(self, message, data):
        print('pre_process, msg: ', message.text)

    def post_process(self, message, data, exception=None):
        if exception:
            print(exception)


class TelegramBot:
    bot = telebot.TeleBot(os.environ["TELEGRAM_BOT_TOKEN"], use_class_middlewares=True)
    sct = mss()
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    def __init__(self, name='Oleksii', default_region=None):
        self.name = name
        self.default_region = default_region or {'top': 0, 'left': 0, 'width': pg.size()[0], 'height': pg.size()[1]}

        self.bot.setup_middleware(Middleware())

        @self.bot.message_handler(commands=['scr'])
        def send_screenshot(message):
            self.send_screenshot()

        markup = types.ReplyKeyboardMarkup(row_width=2)
        screenshot_btn = types.KeyboardButton('get screenshot')
        # itembtn2 = types.KeyboardButton('v')
        markup.add(screenshot_btn)
        # markup.add(screenshot_btn, itembtn2)
        self.bot.send_message(self.chat_id, 'Has been started', reply_markup=markup)

        # @self.bot.edited_message_handler(func=lambda m: True)
        # def message_handler(message: types.Message):
        #     # print(dict(message))
        #     userMessage = message.text
        #     if userMessage == "get screenshot":
        #         print('it is scr')
        #         self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
        #                                    text='Some text, for example')
        # self.send_screenshot()

        @self.bot.message_handler(func=lambda m: True)
        def message_handler(message: types.Message):
            userMessage = message.text
            if userMessage == "get screenshot":
                self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                self.send_screenshot()

        infinity_polling = thr.Thread(target=self.bot.infinity_polling)
        infinity_polling.daemon = True
        infinity_polling.start()

    def stop_polling(self):
        self.send_message('+ Has been finished')
        self.bot.stop_polling()

    def send_message(self, msg: str):
        send_message = thr.Thread(target=self.bot.send_message, args=[self.chat_id, msg])
        send_message.start()

    def send_screenshot(self, region=None, msg: str = None):
        if msg is not None:
            send_message = thr.Thread(target=self.bot.send_message, args=[self.chat_id, msg])
            send_message.start()
        screenshot = self.sct.grab(region or self.default_region)
        png = tools.to_png(screenshot.rgb, screenshot.size)
        send_photo = thr.Thread(target=self.bot.send_photo, args=[self.chat_id, png])
        send_photo.start()


if __name__ == '__main__':
    tb = TelegramBot(default_region={'top': 25, 'left': 0, 'width': 2925, 'height': 1110})

    tb.send_message('hi')

    pg.sleep(20)
    tb.send_message('by')

    tb.stop_polling()
    # @bot.message_handler(commands=['start'])
    # def function_name(message):
    #     bot.reply_to(message, "This is a message handler")
    #     print(message.chat.id)

    # screenshot = sct.grab({'top': 0, 'left': 0, 'width': 3440, 'height': 1440})
    # # screenshot = sct.grab({'top': 350, 'left': 350, 'width': 700, 'height': 400})
    #
    # png = tools.to_png(screenshot.rgb, screenshot.size)
    # print(time())
    # # bot.send_photo("675391544", png)
    # send_photo = thr.Thread(target=bot.send_photo, args=["675391544", png])
    # send_photo.start()
    # print(time())

    # bot.infinity_polling()
