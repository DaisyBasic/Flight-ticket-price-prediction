from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, 'link_login')
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, 'id').send_keys("id 입력")
browser.find_element(By.ID, 'pw').send_keys("pw 입력")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, 'log.login').click()
time.sleep(3)

# 5. id 새로 입력
browser.find_element(By.ID, 'id').send_keys("id 입력2")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit