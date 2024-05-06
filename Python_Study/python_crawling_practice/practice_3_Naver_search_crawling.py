from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# 브라우저를 자동화한 후 >> browser window 창 유지
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

#excludeSwitches: 불필요한 로깅 메시지 >> 브라우저에서 제외

driver = webdriver.Chrome(options=chrome_options)

# 원하는 웹페이지로 이동

#keyword = input("뉴스 키워드 입력해 주세요.")
#path = (f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}") #f string : {}
path = ("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=멀티캠퍼스")
driver.get(path)

# css 선택자 사용, 원하는 클래스를 가진 웹 요소 접근
# 매일경제
# sp_nws1 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press
# 
# class="dsc_wrap"
# 
where_new = [x.text for x in driver.find_elements(By.CLASS_NAME, 'info.press')][:5]
title_1 = [y.text for y in driver.find_elements(By.CLASS_NAME, 'dsc_wrap')][:5]


for title,brand in zip(title_1,where_new):
    print(brand,'-',title,'\n')

driver.quit()