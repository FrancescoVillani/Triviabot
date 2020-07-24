from time import sleep
import json
import sys
import subprocess

try:

    from telethon import TelegramClient
    from googletrans import Translator
    from PIL import ImageGrab
    import pytesseract

except ImportError:

    subprocess.check_call([sys.executable,
                           '-m',
                           "pip",
                           "install",
                           "-r",
                           "requirements.txt"])


with open("C:/Users/theow/Desktop/keys.json", 'r') as f:
    data = json.load(f)
    group_id = data["group_id"]
    api_id = data["api_id"]
    api_hash = data["api_hash"]
    f.close()


questionSize = (360,552,650,620)
answerSize1, answerSize2, answerSize3, answerSize4 = 390, 635, 610, 660
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


client = TelegramClient('C:/Users/theow/Desktop/davide.session', api_id, api_hash)
translator = Translator()


def trans(text):
    return translator.translate(text, dest='en').text


def qmagic(img):
    img = img.crop(questionSize)
    q = pytesseract.image_to_string(img)
    q = q.replace("\n", " ")
    return q


def amagic(img, i):
    img = img.crop(answerSize1, answerSize2 + 43*i, answerSize3, answerSize4 + 43*i)
    a = pytesseract.image_to_string(img)
    return a


with client:
    sleep(3)
    screenshot = ImageGrab.grab()
    question = qmagic(screenshot)
#    question = "Chi ha recentemente battuto il record di presenze in serie A?"
#    answers = ["Gianluigi Buffon", "Fabio Quagliarella", "Giampaolo Pazzini"]
#   answers = [aMagic(screenshot, i) for i in range(3)]
    client.loop.run_until_complete(client.send_message(group_id, question))