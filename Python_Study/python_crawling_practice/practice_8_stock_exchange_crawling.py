# 약간의 이슈가 있음. 나스닥 개장시간이라 애플 최고 , 최저가가 '-'로 표기...추후에 테스트 후 수정할 것..


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
# headless : GUI(Graphic user interface) 없이 실행.
# >> 실제 브라우저 창이 눈에 보이지 않게 실행됨.

# chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
# selenium 에서 크롬 웹 드라이버를 자동으로 다운로드 및 설치

# 웹 드라이버 설정
driver = webdriver.Chrome(service=service, options=chrome_options)

# WebDriverWait(driver, timeout)
wait = WebDriverWait(driver,20) # 10초 기다린다.

# 원으로 환전해볼까?

def twd_exchange():
    url = "https://www.google.com/search?q=twd+환율"
    driver.get(url)
    # data-ved="2ahUKEwjYiZOWrNiFAxU0klYBHY_wDT8QwKsBegQIBxAM"
    twd_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.DFlfde.SwHCTb'))).text
    twd_use_exchage = twd_element.split()[0]

    return float(twd_use_exchage.replace(',',''))
    
def doller_exchage():
    url = "https://www.google.com/search?q=달러+환율"
    driver.get(url)
    #knowledge-currency__updatable-data-column > div.ePzRBb > div > div.MWvIVe.egcvbb > input
    doller_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.DFlfde.SwHCTb'))).text
    doller_use_exchage = doller_element.split()[0]
    return float(doller_use_exchage.replace(',',''))
    
# CSS_SELECTOR : 유연한 구조 / CLASS_NAME : 단일
# CLASS 중복 기준으로 보면 될 듯하다.

# 주소 위치로 이동
keyword_list = ['애플','삼성전자','TSMC']

for key in keyword_list:
    url = f"https://www.google.com/search?q={key}+주가" #q 뒤에는 구글에서 서치..애플+주가 / 삼성전자+주가 / TSMC+주가
    
    driver.get(url) # 이전에는 path를 넣었엇다.
    
    # wait
    # WebDriverWait(driver, timeout)
    # EC.presence_of_element_located
    
    stock_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.DoxwDb'))).text                  # 꼭!!! .text 
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.IsqQVc'))).text                      # 현재가
    high_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최고"]'))).text  # 최고가
    low_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-attrid="최저"]'))).text  # 최저가
    
    currency = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.knFDje'))).text                    # 어떤 화폐인지..
    
    price = float(price.replace(',',''))
    # 최고 및 최저 현시각 나스닥 개장시간이라 '-'로 표기.
    # high_price = float(high_price.replace(',',''))
    # low_price = float(low_price.replace(',',''))

    # 화폐단위 표시 조건
    if currency == "KRW":
        price = str(price)+"원"
        high_price = high_price + "원"
        low_price = low_price + "원"
    elif currency == "USD":
        price = str(doller_exchage()*price) +"원"
        high_price = high_price + "$"
        low_price = low_price + "$"
    elif currency == "TWD":
        price = str(twd_exchange()*price)+"원"
        high_price = str(twd_exchange()*float(high_price.replace(',',''))) + "원"
        low_price = str(twd_exchange()*float(low_price.replace(',',''))) + "원"
    
    
    # 데이터 출력
    print(f'주식명 : {stock_name}')
    print(f'현재 가격 : {price}')
    print(f'최고 가격 : {high_price}')
    print(f'최저 가격 : {low_price}')
    print('-'*30,'\n')

driver.quit()