from login import TELEGRAPH_API_KEY
import requests
from telegraph import Telegraph
telegraph = Telegraph(access_token = TELEGRAPH_API_KEY)
from datetime import  datetime

def now():
    now = datetime.now()
    return str(now.strftime("%d.%m.%Y %H:%M"))

class Picsum:
    def __init__(self):
        pass
    def load_data(self):
        pass
    def save_photo(self, file):
        telegraph.upload_file(file)

# with open('dataset/photos/0404.jpg', 'rb') as file:
#     respons = telegraph.upload_file(file)
#     print(respons)