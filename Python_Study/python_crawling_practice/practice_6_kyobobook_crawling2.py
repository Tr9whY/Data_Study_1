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
#  #tabRoot > div.view_type_list.switch_prod_wrap > ol:nth-child(1) > li:nth-child(1) > div.prod_area.horizontal > div.prod_info_box > div.auto_overflow_wrap.prod_name_group > div > div > a > span
    
        

books = driver.find_elements(By.CLASS_NAME,'prod_item')
for index, book in enumerate(books):
    rank = index + 1
    title = book.find_element(By.CLASS_NAME,'prod_info').text
    author = book.find_element(By.CLASS_NAME,'prod_author').text
    price = book.find_element(By.CLASS_NAME,'price').text

    print(rank, title, author, price)
"""
#books = [x.text for x in driver.find_elements(By.CLASS_NAME,'prod_item')][:5]
#title = [y.text for y in driver.find_elements(By.CLASS_NAME,'prod_info')][:5]
#author = [z.text for z in driver.find_elements(By.CLASS_NAME,'prod_author')][:5]
#price = [k.text for k in driver.find_elements(By.CLASS_NAME,'price')][:10]

#for index, (a,b,c,d) in enumerate(zip(books,title,author,price)):
    #print(f'{index+1}, {a} \n {b} \n {c} \n {d} \n', end='\n')


#where_new = [x.text for x in driver.find_elements(By.CLASS_NAME, 'info.press')][:5]
#title_1 = [y.text for y in driver.find_elements(By.CLASS_NAME, 'dsc_wrap')][:5]


#for num ,(title,brand) in enumerate(zip(title_1,where_new)):
#    print(f'{num+1}번 : \n 출처: {brand} \n 내용 : {title}','\n')
"""
driver.quit()