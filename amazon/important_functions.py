import re

def extract_image(requests):

    with open("amazon/templates/youtube.html","w") as file:
        text = file.read()

    image_url = re.findall("<img src=(.*?)\>", text)

    return  HttpResponse(image_url)
