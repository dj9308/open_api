from django.shortcuts import render, HttpResponse
import random
import requests

def index(request):
    # return HttpResponse('Welcome to Django')
    return render(request,'index.html')

def hola(request):
    # return HttpResponse('Hello, my name in juan')
    return render(request, 'hola.html')

def dinner(request):
    menus = ['피자','치킨','족발','라면']
    dinner = random.choice(menus)
    # return HttpResponse(f'오늘의 저녁 메뉴는 {dinner}입니다.')
    return render(request, 'dinner.html',{'menus':menus, 'dinner':dinner})

def lotto(request):
    numbers = range(1,46)
    my_lotto = random.sample(numbers,6)
    # return HttpResponse(f'오늘의 로또 추천번호는 {my_lotto}입니다.')
    return render(request, 'lotto.html',{'my_lotto':my_lotto})

def lotto2(request):
    URL_GetLottoNumber = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" # 현재 동행로또 주소
    sDrwNum = '882'
    resp = requests.get(URL_GetLottoNumber + sDrwNum)
    jsResult = resp.json()
    numbers = range(1,46)
    answer = 0
    while(True):
        my_lotto = random.sample(numbers,6)
        if(jsResult["drwtNo1"] in my_lotto):
            if(jsResult["drwtNo2"] in my_lotto):
                if(jsResult["drwtNo3"] in my_lotto):
                    if(jsResult["drwtNo4"] in my_lotto):
                        if(jsResult["drwtNo5"] in my_lotto):
                            if(jsResult["bnusNo"] in my_lotto):
                                break
        else:
            answer=answer+1
    return HttpResponse(f'{answer}')

def hello(request, name):
    return render(request, 'hello.html',{'name':name})

def introduce(request,name,age):
    return render(request,'introduce.html',{'name':name,'age':age})

def square(request,width,height):
    answer = width*height
    return render(request,'square.html',{'width':width,'height':height,'answer':answer})