from bs4 import BeautifulSoup
from urllib import request, parse
from selenium import webdriver
import time
import re
from settings import WEB_DRIVER_PATH
import xlwt

DATE = 0
TITLE = 1
TEXT = 2


def make_basic_url(city, town, start_1, end_1, start_2, end_2):
    print('make_basic_url')
    base_url = 'https://search.naver.com/search.naver?where=news'
    query = '&query='+ '%2B' + parse.quote(city) +'%20%2B' +parse.quote(town)
    url2 = '&sm=tab_opt&sort=1&photo=0&field=0&reporter_article=&pd=3'
    period= '&ds=' + start_1 + '&de=' + end_1
    url3 = '&docid=&nso=so%3Add%2Cp%3A'
    period2 = 'from' + start_2 + 'to' + end_2
    url4 = '%2Ca%3Aall&mynews=0&mson=0&refresh_start=0&related=0'

    final_url = base_url + query + url2 + period + url3+ period2 + url4
    return final_url
"""
city = 시,도
town = 구, 군
start_1 = yyyy.mm.dd
end_1 = yyyy.mm.dd
start_2 = yyyymmdd
end_2 = yyyymmdd
"""

def get_news_urls(city, town, start_1, end_1,start_2, end_2, driver):
    print('get_news_urls')
    basic_url = make_basic_url(city, town, start_1, end_1, start_2, end_2)
    news = []
    index = 1
    flag = True
    regex_href = r'.*https:\/\/m\.blog\.naver\.com\/(\w*\/\d*'
    while(flag):
        # index에 해당하는 url
        url = basic_url + str(index)

        driver.get(url)
        html = driver.page_source
        bs = BeautifulSoup(html, 'html5lib')
        links = bs.select('.bx a')
        for single_link in links:
        # single_link가 https://m.blg.naver.com을 포함하면 그걸 가져오자
            href = re.findall(regex_href, str(single_link))
            if href != None and href !=[]:
                if href in blog_postings:
                    flag = False
                    break;
                else:
                    blog_postings.append(href)
        index += 15
    return blog_postings
