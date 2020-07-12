import requests 
from bs4 import BeautifulSoup

request = requests.get("https://www.google.com/")
print(request)
print(request.status_code)
print(request.headers)