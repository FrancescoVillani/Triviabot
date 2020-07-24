from time import sleep
import json

try:
    from telethon import TelegramClient
    from googletrans import Translator
    from PIL import ImageGrab
    import pytesseract
except ImportError:
    with open('requirements.txt', 'r') as file:
        for line in file:
            pip(['install', line])



with open("C:/Users/theow/Desktop/keys.json", 'r') as f:
    data = json.load(f)
    group_id = data["group_id"]
    api_id = data["api_id"]
    api_hash = data["api_hash"]
    f.close()

questionSize = (0,200,1920,1080)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


client = TelegramClient('C:/Users/theow/Desktop/davide.session', api_id, api_hash)
translator = Translator()


def trans(text):
    return translator.translate(text, dest='en').text

def QMagic(img):
    img = img.crop(questionSize)
    q = pytesseract.image_to_string(img)
    q = q.replace("can", "").replace("\n","")
    return q

def AMagic(img, i):
    pass

with client:
    sleep(3)
    screenshot = ImageGrab.grab()
    question = QMagic(screenshot)
    #answers = [AMagic(screenshot, i) for i in range(3)]
    client.loop.run_until_complete(client.send_message(group_id, question))