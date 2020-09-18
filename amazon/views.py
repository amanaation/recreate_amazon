from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import unidecode
import re

# Create your views here.

def render_page(request):

    domain = "google"
    url = "google.com"

    request_url = str(request.build_absolute_uri())
    url = request_url.replace("http://localhost:8000","https://"+url)
    s = requests.Session()

    headers = {
        'authority': url,
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
    with open("amazon/templates/"+domain+".html","w") as file:
        file.write(unidecode.unidecode(r.text))

    return render(request, domain+".html")
    #'''
def google(request):


    return HttpResponse(request.build_absolute_uri() )
