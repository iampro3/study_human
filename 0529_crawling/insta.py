# pip install selenium

# pip install BeautifulSoup4

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/

baseUrl ='https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

#h driver = webdriver.Chrome() 지우고 대체함
# options=webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitched', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# options = Options()
# options.page_load_strategy = 'normal'
# driver = webdriver.Chrome(options=options)


#driver = webdriver.Chrome(e xecutable_path="C:/ks/study_human/0529_crawling/chromedriver.exe")
#driver = webdriver.Chrome()
driver.get("https://google.com")

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

insta = soup.select('._aagu')  # 인스타에서 1개 이미지
# insta = soup.select('._aabd._aa8k._aanf')  # 인스타에서 1개 이미지

print(insta)
driver.close()

#print(url)
#https://weezzle.tistory.com/1961
#https://dahaha.tistory.com/76
# 실패함 : 드라이버 버전 불일치라고 뜨는데, 해결 안 됨
#https://www.inflearn.com/chats/529856/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80%EC%9D%B4-%EB%B2%84%EC%A0%BC%EC%97%85%EC%9D%84-%ED%95%B4%EC%84%9C-%EC%83%88%EB%A1%9C%EC%9A%B4-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%BD%94%EB%93%9C%EB%A1%9C-%EC%A0%84%EC%B2%B4-%EC%BD%94%EB%93%9C-%EA%B3%B5%EC%9C%A0%ED%95%A9%EB%8B%88%EB%8B%A4
