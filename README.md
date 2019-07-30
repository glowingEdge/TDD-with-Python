# -TDD-with-Python
클린 코드를 위한 테스트 주도 개발

## 책과 다른 부분

### 개발 환경
 - Windows 10
 - PyCharm IDE
 - Python 3.7 
 - Django 2.1
 - selenium 3.141.0

### 변경된 부분
#### Chapter 1
#### p. 5
 처음 Webdriver 테스트 케이스에서, Firefox 대신 Chrome을 이용하였고, Chrome Webdirver를 설치해주었다. (http://chromedriver.chromium.org/downloads) <br><br>
Functional_test.py 에서 webdriver 를 가져올 땐 다음과 같이 .exe까지 명시해준다.

    browser = webdriver.Chrome("C:\\User\\GlowingEdge\\chromedriver.exe")


#### Chapter 3
#### p. 28
django.core에 있던 urlresolvers는 v1.1에 있던 모듈이다.<br>

    from django.core.urlresolvers import resolve
    -> from django.urls import resolve

#### p. 31, 33
위와 마찬가지로 url() method 의 경우 path() 를 써야 한다.<br><br>

테스트 케이스 작성도 아래처럼 path() 사용법을 참고한다.<br>
url pattern 변경점도 참고한다. <a href=https://blog.illustudio.co.kr/2018/01/29/django-2-0-%EC%97%90%EC%84%9C-%EB%8B%AC%EB%9D%BC%EC%A7%84-%EC%A0%90%EB%93%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%95%99%EC%8A%B5%EC%A4%91>(링크)</a>

    url(r'^$', 'lists.views.home_page', name='home')
    -> path('', liists.views.home_page, name='home')

