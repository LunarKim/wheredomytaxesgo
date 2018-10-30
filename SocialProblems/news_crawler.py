# coding: utf-8
import requests
from bs4 import BeautifulSoup, NavigableString


def get_string(parent):
    l = []
    for tag in parent:
        if isinstance(tag, NavigableString):
            l.append(tag.string)
        else:
            l.extend(get_string(tag))
    return l

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; ko-KR))',
}
response = requests.get(
"https://search.naver.com/search.naver?where=news&query=%2B서울시%20%2B강남구&sm=tab_opt&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2018.10.01&de=2018.10.28&docid=&nso=so%3Add%2Cp%3Afrom20181001to20181028%2Ca%3Aall&mynews=0&mson=0&refresh_start=0", headers=headers)
html = response.text

soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')

for li in soup.find('ul', {'class':'type01'}).findAll('li'):
    link = li.find('dt').find('a')
    print(link.text)
    print(link['href'])
    print(get_string(li.find('dd'))[0])
