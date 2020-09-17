import requests

response = requests.get('chrome://settings/clearBrowserData')
print(response.text)
