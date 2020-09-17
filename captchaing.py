from io import BytesIO 
import lxml.html 
from PIL import Image
import requests

def load_captcha(html): 
   tree = lxml.html.fromstring(html)
   img_data = tree.cssselect('img')[0].get('src') 
   print(img_data)
   #img_data = img_data.partition(',')[-1]
   img = requests.get(img_data).text
   print(img)
   binary_img_data = img_data.decode(img) 
   file_like = BytesIO(binary_img_data) 
   img = Image.open(file_like) 
   return img

data = open("amazon.html").read()

print(load_captcha(data))
