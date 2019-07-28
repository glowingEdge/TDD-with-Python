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
처음 Webdriver 테스트 케이스에서, Firefox 대신 Chrome을 이용하였고, Chrome Webdirver를 설치해주었다. (http://chromedriver.chromium.org/downloads) <br><br>
Functional_test.py 에서 webdriver 를 가져올 땐 다음과 같이 .exe까지 명시해준다.

    browser = webdriver.Chrome("C:\\User\\GlowingEdge\\chromedriver.exe")

