from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
# headless : GUI(Graphic user interface) 없이 실행
# >> 실제 브라우저 창이 눈에 보이지 않게 실행됨

# chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
# selenium 에서 크롬 웹 드라이버를 자동으로 다운로드 및 설치

# 웹드라이버 설정
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 10) # 최대한 10초 기다리겠다!

# CSS_SELECTOR : 유연한 구조 / CLASS_NAME : 단일
# CLASS 중복 기준으로 보면 될 듯하다.

# 주소 위치로 이동
keyword_list = ['애플','삼성전자','TSMC']

for kw in keyword_list:
    url = f"https://www.google.com/search?q={kw}+주가"
    
    driver.get(url)
    
    # wait
    # WebDriverWait(driver, timeout)
    # EC.presence_of_element_located
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.DoxwDb'))).text
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.IsqQVc'))).text
    high_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최고"]'))).text
    low_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최저"]'))).text
    
    #knFDje
    currency = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.knFDje'))).text
    
    # 화폐단위 표시 조건
    if currency == "KRW":
        price = price+"원"
        high_price = high_price + "원"
        low_price = low_price + "원"
    elif currency == "USD":
        price = price+"$"
        high_price = high_price + "$"
        low_price = low_price + "$"
    elif currency == "TWD":
        price = price+"TWD"
        high_price = high_price + "TWD"
        low_price = low_price + "TWD"

    # 데이터 출력
    print(f'주식명 : {name}')
    print(f'현재 가격 : {price}')
    print(f'최고 가격 : {high_price}')
    print(f'최저 가격 : {low_price}')
    print('-'*30,'\n')

driver.quit()