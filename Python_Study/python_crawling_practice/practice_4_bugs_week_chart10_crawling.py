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
path = ("https://music.bugs.co.kr/chart/track/week/total")
driver.get(path)

# CSS_SELECTOR :
# 벅스 뮤직 주간 순위 매겨보기
bugs_title = [x.text for x in driver.find_elements(By.CLASS_NAME, 'title')][3:14]
bugs_artist = [y.text for y in driver.find_elements(By.CLASS_NAME, 'artist')][1:11]
bugs_album = [z.text for z in driver.find_elements(By.CLASS_NAME, 'album')][2:13]

for num , (temp_1, temp_2 , temp_3) in enumerate(zip(bugs_title,bugs_artist, bugs_album)):
    print(f'주간 {num+1} 순위 \n 곡 : {temp_1} \n 아티스트 : {temp_2} \n 앨범 : {temp_3} 입니다.','\n')

driver.quit()


