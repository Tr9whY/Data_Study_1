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
path = "https://www.google.com/search?q=%EC%97%94%EB%B9%84%EB%94%94%EC%95%84+%EC%A3%BC%EA%B0%80"
driver.get(path)

# css 선택자 사용, 원하는 클래스를 가진 웹 요소 접근
# #rcnt > div.XqFnDf > div > div > div.wPNfjb > div > div.hHq9Z > div > div > div.MDY31c > div.QpPSMb > div > div
# #rso > div:nth-child(1) > div > div > div:nth-child(2) > div
element = driver.find_element(By.CSS_SELECTOR,'.PZPZlf.ssJ7i.B5dxMb').text
print(element)
print('-'*30)
location = driver.find_element(By.CSS_SELECTOR,'.IsqQVc.NprOob.wT3VGc').text
print(f'{element}의 주가는 현재 {location}달러 입니다.')
print('-'*30)

# 창 닫기
driver.quit()      
