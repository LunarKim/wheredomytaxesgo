from tkinter import*

import nltk
from konlpy.tag import Twitter
from matplotlib import font_manager,rc
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import webbrowser
import crawling

t= Twitter()


all_news = " " 
page_t=[0,0,0]
search_index = []
url_t1 =[]
url_t2 =[]
url_t3 =[]


def Window_new() :
    global all_news
    global box_head_all
    global box_head_search
    global k
    global url_t1,url_t2,url_t3
    window2 = Toplevel()    #자식 윈도우창 만듬
    window2.geometry('600x510')
    window2.title("주식정보 종합 프로그램")

    
    u_frame = Frame(window2, width = 100, height=100, bd = 2, relief = SUNKEN)  #프레임을 3개로 나눔
    e_frame = Frame(window2, width = 100, height=40, bd = 2, relief = SUNKEN)
    d_frame = Frame(window2, width = 100, height=100, bd = 2, relief = SUNKEN)
    f_frame = Frame(window2, width = 100, height=40, bd = 2, relief = SUNKEN)
    b_frame = Frame(window2, width = 100, height=100, bd = 2, relief = SUNKEN)

    u_frame.pack(side = TOP, fill=X, padx = 5,pady = 5)    #프레임 위치
    e_frame.pack(fill=X, padx = 5,pady = 5)
    d_frame.pack(fill=X, padx = 5,pady = 5)
    f_frame.pack(fill=X, padx = 5,pady = 5)
    b_frame.pack(fill=X, padx = 5,pady = 5)
    
    
    b_keyword = Button(u_frame, width =15, text='Hot한 키워드', command = Hotkeyword) 
    b_cancel = Button(u_frame, width =15, text ='되돌아가기', command = window2.destroy)

    b_keyword.pack(side = LEFT, fill = Y, padx = 5,pady = 5)
    b_cancel.pack(side = LEFT, fill =Y, padx = 5,pady = 5)

    Label(u_frame, font=('맑은 고딕',10), text = '  자료가 나오지 않을경우 되돌아가기를\n눌러 날짜와 기업을 확인해 주세요').pack(side = LEFT)
    Label(e_frame, font=('맑은 고딕',15), text = '전체 기사 제목 (더블클릭시 뉴스홈으로 연결 됩니다.)').pack()
    Label(f_frame, font=('맑은 고딕',15), text = '검색한 기업관련 기사 제목 (더블클릭시 뉴스홈으로 연결 됩니다.)').pack()

    scrollbar = Scrollbar(d_frame)  #스크롤바 만들기
    scrollbar2 = Scrollbar(b_frame)
    
    scrollbar.pack(side = RIGHT,fill=Y)   #스크롤바 위치
    scrollbar2.pack(side = RIGHT,fill=Y)

    
    box_head_all = Listbox(d_frame, width =85, yscrollcommand = scrollbar.set)  #리스트박스 클래스 생성, yscrollcommand 스크롤과 리스트박스 방향 연동
    scrollbar.config(command = box_head_all.yview)  #마우스로 스크롤바 움직이게 함

    box_head_search = Listbox(b_frame, width =85, yscrollcommand = scrollbar2.set)   #검색한 기업의 기사 담을 리스트 박스
    scrollbar2.config(command = box_head_search.yview)

    k=0
    del search_index[:]
    
    for i in range(0 ,page_t[0]-1) :    #크롤링한 내용들을 리스트 박스에 저장
        for j in range(0,20) :
            if(crawling.title_news1[i][j]):
                box_head_all.insert(END, crawling.title_news1[i][j])

                if not(e2_input.get()=="") and (e2_input.get() in crawling.title_news1[i][j]) :
                    box_head_search.insert(END, crawling.title_news1[i][j])
                    search_index.append(k)

                all_news +=crawling.title_news1[i][j]
                k +=1
               
                    
    for i in range(0 ,page_t[1]-1) :
        for j in range(0,20) :
            if(crawling.title_news2[i][j]):
                box_head_all.insert(END,crawling.title_news2[i][j])

                if not(e2_input.get()=="") and (e2_input.get() in crawling.title_news2[i][j]) :
                    box_head_search.insert(END, crawling.title_news2[i][j])
                    search_index.append(k)

                all_news +=crawling.title_news2[i][j]
                k +=1

    for i in range(0 ,page_t[2]-1) :
        for j in range(0,20) :
            if(crawling.title_news3[i][j]):
                box_head_all.insert(END, crawling.title_news3[i][j])

                if not(e2_input.get()=="") and (e2_input.get() in crawling.title_news3[i][j]) :
                    box_head_search.insert(END, crawling.title_news3[i][j])
                    search_index.append(k)
                    
                all_news +=crawling.title_news3[i][j]
                k+=1

    box_head_all.bind("<Double-Button-1>",popbrowser)   #더블클릭 하면 연결된 url 띄움
    box_head_search.bind("<Double-Button-1>",popbrowser)

    
    box_head_all.pack(side = LEFT, fill = X)    #리스트박스 위치
    box_head_search.pack(side = LEFT, fill = X)

 

    
def Date_input () :
    global e_input
    crawling.crawling_date(str(e_input.get()))

    for i in range(0,3) :
        page_t[i] =crawling.page_news[i]
        crawling.page_news[i] = 0

        if i==0 :
            for j in range(0,page_t[i]-1) :
                url_t1.append(crawling.url_news1[j])
                print(url_t1[j])
        if i==1 :
            for j in range(0,page_t[i]-1) :
                url_t2.append(crawling.url_news2[j])
                print(url_t2[j])
        if i==2 :
            for j in range(0,page_t[i]-1) :
                url_t3.append(crawling.url_news3[j])
                print(url_t3[j])
    Window_new()


def Hotkeyword () : #워드클라우드 띄우는 함수
    nouns = t.nouns(all_news)

    trash = ["기업","금융","은행","정부","비율","공개","포토"]

    for i in nouns :
        if len(i)<2 :
            nouns.remove(i)
        for j in trash:
            if i==j :
                nouns.remove(j)
    

    
    ko = nltk.Text(nouns,name = "분석")

    ranking = ko.vocab().most_common(100)
    tmpdata = dict(ranking)

    wordcloud = WordCloud(font_path ="NotoSansCJKkr-Medium.otf",
                          relative_scaling=0.2,
                          background_color="white",).generate_from_frequencies(tmpdata)

    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def popbrowser(s) :
    try :   #전체 크롤링 리스트박스 클릭할때
        print(box_head_all.curselection()[0])
        print("click")

        x= int((box_head_all.curselection()[0])/20)
        print()

        if x < page_t[0]-1 :
            print(url_t1[x])
            print(x)
            print(page_t[0]-2)
            print('----------')
            webbrowser.open_new(url_t1[x])
            

        elif x < page_t[0]+page_t[1]-3 :
            x =x-(page_t[0]-1)
            print(url_t2[x])
            print(x)
            print(page_t[1]-2)
            print('----------')
            webbrowser.open_new(url_t2[x])
            
        elif x < page_t[0]+page_t[1]+page_t[2]-5:
            x = x-(page_t[0]+page_t[1]-3)
            print(url_t3[x])
            print(x)
            print(page_t[2]-2)
            print('----------')
            webbrowser.open_new(url_t3[x])

    except :    #검색한 기업 리스트 박스 클릭할때
        print(box_head_search.curselection()[0])
        print("click")
        print(search_index[box_head_search.curselection()[0]])

        x= int((search_index[box_head_search.curselection()[0]])/20)
        
        if x < page_t[0]-1 :
            webbrowser.open_new(url_t1[x])

        elif x < page_t[0]+page_t[1]-3 :
            x =x-(page_t[0]-1)
            webbrowser.open_new(url_t2[x])
            
        elif x < page_t[0]+page_t[1]+page_t[2]-5:
            x = x-(page_t[0]+page_t[1]-3)
            webbrowser.open_new(url_t3[x])

    
    
##main 문##    
window = Tk()   #부모 윈도우창 만듬
window.title("주식정보 종합 프로그램")
window.geometry("650x200")

l_explain1 = Label(window, font=('맑은 고딕',15), text = '날짜를 8자릿수로 입력해 주세요 ex)20180312')
l_explain2 = Label(window, font=('맑은 고딕',15), text = '주의사항: 날짜를 8자릿수로 입력하지 않을경우\n 오류가 발생할 수 있습니다.')
b_input = Button(window, text="검색", width = 7, command=Date_input)
e_input = Entry(window, font=('맑은 고딕',15), width =35)   #검색할 날짜
e2_input = Entry(window, font=('맑은 고딕',15), width =35)  #기업이름

Label(window, font=('맑은 고딕',15), text = '기사를 검색할 날짜와 기업의 이름을 입력해 주세요').grid(row =0,column=1)
l_explain1.grid(row =1,column=1)

Label(window, text = '검색할 날짜 :').grid(row =2,column =0)
e_input.grid(row =2,column =1)

Label(window, text = '검색할 기업(키워드) :').grid(row =3,column =0)
e2_input.grid(row =3,column =1)
b_input.grid(row =3,column =2)

l_explain2.grid(row =4,column=1)

    
window.mainloop()
