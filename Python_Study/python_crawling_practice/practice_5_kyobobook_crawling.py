from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])


driver = webdriver.Chrome(options=chrome_options)

path = ("https://product.kyobobook.co.kr/bestseller/online?period=001&page=1&per=50")
driver.get(path)

# prod_item, prod_info, prod_author, price
# 
# 
# 

title = [y.text for y in driver.find_elements(By.CLASS_NAME,'prod_info')][:10]
author = [z.text for z in driver.find_elements(By.CLASS_NAME,'prod_author')][:10]
price = [k.text for k in driver.find_elements(By.CLASS_NAME,'price')][:10]

for index, (a,b,c) in enumerate(zip(title,author,price)):
    if index == 0:
        print("베스트 셀러")
    print(f'{index+1}, {a} \n {b} \n {c} \n ', end='\n')



driver.quit()