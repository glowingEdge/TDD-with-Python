# TDD-with-Python
클린 코드를 위한 테스트 주도 개발
HTML 버전은 무료로 업데이트하고 있다. 한글판과 소스 코드 차이점을 참고할 때에 1차적으로는 <a href=https://www.obeythetestinggoat.com/pages/book.html#toc>여기</a>를 참고하고, 그 외 변경사항들을 아래 정리.<br>
(+추가) 책의 8장, 온라인 버전의 9장부터는 서로 다른 점도 쌓이고, 그나마 최신의 코드들을 참고할 수 있는 온라인 버전으로 진행하는게 더 편했다.(비록 영어임에도)

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


#### Chapter 6
#### p. 116
    class Item(models.Model):
        text = models.TextField(default='')
        list = models.ForeignKey(List, default=None)

위와 같이 ForeignKey 설정 후 makemigrations 실행 시, 아래와 같은 에러가 발생한다.

    ...
    TypeError: __init__() missing 1 required positional argument: 'on_delete'

어떤 오류인지 감이 오는데, 책에선 아무렇지 않게 넘어갔다. 어느 버전인지는 모르겠지만 Django에서 필수로 지정한듯 하다. 다음과 같이 수정한다.

     class Item(models.Model):
        text = models.TextField(default='')
        list = models.ForeignKey(List, on_delete=models.SET_DEFAULT, default=None)

#### p.119
책이 쓰여질 때와 url pattern을 작성하는 법이 변경됐기 때문에 아래와 같이 url을 사용한다.<br>
(' path '는 ' .+ ' 를 대신하기 위해서 사용했지만, 실제로는 ' int ' 써야할 것이다.) <br>
  <a href="https://consideratecode.com/2018/05/02/django-2-0-url-to-path-cheatsheet"/>path()사용에 관한 좋은 글</a>

-책 코드

    urlpatterns = [
        url(r'^$', views.home_page, name='home'),
        url(r'^lists/new$', views.new_list, name='new_list'),
        url(r'^lists/(.+)/$', views.view_list, name='view_list'),
    ]

-변경한 코드

    urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/<path:list_id>/', views.view_list, name='view_list'),
    path('lists/new', views.new_list, name='new_list'),
    path('admin/', admin.site.urls),
]
