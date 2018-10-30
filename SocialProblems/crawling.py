import requests
from bs4 import BeautifulSoup

##변수 정의##
date = ''
page =30
page_news = [0,0,0]
sector = 0
s=''
title_news1 = []
title_news2 = []
title_news3 = []
url_news1 =[]
url_news2 =[]
url_news3 =[]
number=0

for row in range(page) : #pagex23 중첩 리스트 생성
    title_news1 += [[0]*23]
    title_news2 += [[0]*23]
    title_news3 += [[0]*23]
  
##함수 정의##  
def Crawling_news (url):    #url받고 크롤링동작하는 함수
    global date,number
    global url_news1,url_news2,url_news3
    url +=date+"&page=0"
    pre_dt_tag = 0
    
   
    for i in range(1,page) :    #1~50페이지까지 크롤링
        if i<=10 :
            count = 1
        else : count = 2
        
        url = url[0:-count]
        s=str(i)
        url+=s

        if sector==0 :
            url_news1.append(url)
 
        elif sector==1 :
            url_news2.append(url)

        elif sector==2 :
            url_news3.append(url)
    
    
        
        print(url,'\n---------------------------------------------------------------------------------------')
        #여기까지 url 받아오기

        r=requests.get(url) # 홈페이지 접속
        c=r.content # content(내용) 받아옴
        soup=BeautifulSoup(c,"html.parser") # beautiful soup를 사용할수 있게 만들어 줌/ html 내용 저장돼있음

        body_tag = soup.find("body")    # body 라는 태그를 찾아 body_tag이라는 변수에 저장
        dt_tag = body_tag.find_all("dt",{"class":""})   # dt 태그안에 헤드라인 들어있음
        
        if dt_tag ==pre_dt_tag: # 마지막 페이지까지 크롤링 했을경우 크롤링 중지
            print("\n마지막 페이지 입니다\n")
            break
        
        pre_dt_tag = dt_tag
        page_news[sector] += 1 #크롤링한 뉴스페이지의 수를 저장
        
        k=0
        for j in dt_tag :

            
            title = j.text.replace("\t","").replace("\n","")    #text는 태그 뺀 텍스트 부분만 가져옴   .replace("바꿀것","바뀐것"). 필요없는 부분 지움
            title = title[2:-1]
            if (len(title)>3):
                if (sector==0):
                    title_news1[(i-1)][k] = str(number)+'. '+title #의미있는 헤드라인 들어있는 범위는 [i][0~19]
                    number +=1
                    
                elif (sector==1):
                    title_news2[(i-1)][k] = str(number)+'. '+title
                    number +=1
                    
                elif (sector==2):
                    title_news3[(i-1)][k] = str(number)+'. '+title
                    number +=1
                    
            k += 1
            
def crawling_date (s) : #s에 날짜를 입력받고 데이터 크롤링 시작
    global date
    global sector
    global number
    date = s
    news = ["http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=101&date=",
            "http://news.naver.com/main/list.nhn?mode=LS2D&sid2=259&sid1=101&mid=shm&date=",
            "http://news.naver.com/main/list.nhn?mode=LS2D&sid2=258&sid1=101&mid=shm&date="
            ]

    for index in news:
        Crawling_news(index)
      #  number -=20
        sector +=1
    
    print(page_news[0],"\n")
    print(page_news[1],"\n")
    print(page_news[2],"\n")
    
    sector=0        #다시 동작 될때를 위해 0으로 다시 초기화
    number =0

