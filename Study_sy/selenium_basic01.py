from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


browser = webdriver.Chrome()
browser.get("https://www.naver.com/")

# elem = browser.find_element_by_class_name("link_login") 이거 이제 동작 안함. 아래 코드로 실행
elem = browser.find_element(By.CLASS_NAME, "link_login")
# print("Element 객체:", elem)
elem.click()
browser.back()

# browser.back()
# browser.forward()
# browser.refresh() 

elem = browser.find_element(By.ID, "query")
elem.send_keys("시나모롤")
elem.send_keys(Keys.ENTER)

elem = browser.find_elements(By.TAG_NAME, "a") # elements로 하면 여러 element값을 가져옴
# print("'a' Elements: ", elem)

# for e in elem:
#     print(e.get_attribute('href'))

browser.get("https://www.daum.net/")
elem = browser.find_element(By.NAME, 'q')
elem.send_keys("시나모롤")
elem.send_keys(Keys.ENTER)
browser.back()

elem = browser.find_element(By.NAME, 'q')
elem.send_keys("시나모롤")

elem = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[3]")
# print(elem)
elem.click()
browser.close() # 현재 열려있는 탭만 닫음
browser.quit() # 전부 닫음.
# exit() 파이썬 콘솔 종료.
