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
path = ("https://finance.naver.com/sise/sise_rise.naver")
driver.get(path)

# 네이버 국내증시 상승 크롤링 해보기


temp_title= driver.find_elements(By.CLASS_NAME, 'tltle')
temp_info = driver.find_elements(By.CLASS_NAME, 'number')
temp_raise = driver.find_elements(By.CLASS_NAME, 'tah.p11.red01')

for temp_1, temp_2 , temp_3 in zip(temp_title[:5],temp_info[:5], temp_raise[:5]):
    temp_a = temp_1.text
    temp_b = temp_2.text
    temp_c = temp_3.text
    print(f'{temp_a}은 {temp_b}원 으로 등락률 {temp_c} 입니다.')

driver.quit()