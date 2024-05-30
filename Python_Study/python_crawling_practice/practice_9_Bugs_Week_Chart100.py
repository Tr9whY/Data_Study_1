from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

# 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
# 브라우저를 자동화한 후 >> browser window 창 유지
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

#excludeSwitches: 불필요한 로깅 메시지 >> 브라우저에서 제외

driver = webdriver.Chrome(options=chrome_options)

# 원하는 웹페이지로 이동
path = ("https://music.bugs.co.kr/chart/track/week/total")
driver.get(path)

# CSS_SELECTOR :
# 벅스 뮤직 주간 순위 매겨보기
bugs_title = [x.text for x in driver.find_elements(By.CLASS_NAME, 'title')][3:]
bugs_artist = [y.text for y in driver.find_elements(By.CLASS_NAME, 'artist')][1:]
bugs_album = [z.text for z in driver.find_elements(By.CLASS_NAME, 'album')][2:]

for num , (temp_1, temp_2 , temp_3) in enumerate(zip(bugs_title,bugs_artist, bugs_album)):
    print(f'주간 {num+1} 순위 \n 곡 : {temp_1} \n 아티스트 : {temp_2} \n 앨범 : {temp_3} 입니다.','\n')


# DF 생성
data = {
    '주간 순위': list(range(1, len(bugs_title) + 1)),
    '곡': bugs_title,
    '아티스트': bugs_artist,
    '앨범': bugs_album
}
df= pd.DataFrame(data)

csv_file_path = 'Bugs_Week_Chart100.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')


driver.quit()


