import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup, NavigableString

# 네이버 크롤링이 막혀있어서 새로운 클래스를 만들었다.
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open('http://httpbin.org/user-agent')

input_url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&ie=utf8&query=%EC%9D%B8%EC%A0%9C%EA%B5%B0"
source_code_from_url = opener.open(input_url)
soup = BeautifulSoup(source_code_from_url, "lxml", from_encoding = "utf-8")
item = soup.find_all('div', 'info')

article = soup.find('a')['href']
news_url = opener.open(article)
soup2 = BeautifulSoup(news_url, 'lxml', from_encoding = "utf-8")
article_body = soup2.find('div', id = "articleBodyContents")
dirt_text = article_body.find_all(text = True)
cleaned_text = re.sub('[a-zA-Z]', '', str(dirt_text))
