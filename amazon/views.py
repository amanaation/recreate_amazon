from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import unidecode
import re
import requests # to get image from the web
import shutil # to save it locally
from PIL import Image
import pytesseract

# Create your views here.

def extract_image(request):

    with open("amazon/templates/amazon.html","r") as file:
        text = file.read()

    image_url = re.findall('<img src=\"(.*?)\"\>', text)[0]

    filename = image_url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open("Captcha.jpg",'wb') as f:
            shutil.copyfileobj(r.raw, f)

        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        # Create an image object of PIL library
        image = Image.open('Captcha.jpg')

        # pass image into pytesseract module
        # pytesseract is trained in many languages
        image_to_text = pytesseract.image_to_string(image, lang='eng')
        image_to_text = re.sub(r'[^a-zA-Z]+', '', image_to_text)
        # Print the text
        return  HttpResponse(unidecode.unidecode(image_to_text))


        #return  HttpResponse('Image sucessfully Downloaded: ',filename)
    else:
        return  HttpResponse('Image Couldn\'t be retreived')


    #return  HttpResponse("<h1>"+image_url+"</h1>")


def render_page(request):

    request_url = str(request.build_absolute_uri())
    
    url = request_url.replace("http://localhost:8000","https://www.medium.com")
    #return HttpResponse(url )
    #'''
    s = requests.Session()
    #url = "https://www.amazon.com/"

    headers = {
        'authority': 'www.medium.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = s.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    #print(r.text)
    with open("amazon/templates/medium.html","w") as file:
        file.write(unidecode.unidecode(r.text))

    return render(request, "medium.html")
    #'''
def google(request):


    return HttpResponse(request.build_absolute_uri() )
