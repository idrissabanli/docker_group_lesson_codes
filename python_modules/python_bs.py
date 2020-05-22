from bs4 import BeautifulSoup
import requests

response = requests.get('https://oxu.az/')

soup = BeautifulSoup(response.text, features="html.parser")

news_list = soup.findAll("div", {"class": "title"})

for news in news_list:
    print(news.text)


