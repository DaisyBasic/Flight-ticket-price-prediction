from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
# pip install chromedriver-autoinstaller
import chromedriver_autoinstaller as AutoChrome
import shutil
from selenium.webdriver.chrome.options import Options
import csv

def chromedriver_update():
    chrome_ver      = AutoChrome.get_chrome_version().split('.')[0]

    current_list    = os.listdir(os.getcwd()) 			# 현재 경로의 모든 객체들
    chrome_list = []
    for i in current_list:
        path = os.path.join(os.getcwd(), i) 			# 현재 경로의 모든객체의 전체경로
        if os.path.isdir(path): 				# 그 경로가 폴더인지 확인
            if 'chromedriver.exe' in os.listdir(path): 		# 폴더면 안에 chromedriver.exe가 있는지 확인
                chrome_list.append(i) 				# 있는경우 chrome_list에 추가

    old_version = list(set(chrome_list)-set([chrome_ver])) 	# 그중에 최신버전은 제외

    for i in old_version:
        path = os.path.join(os.getcwd(),i) 			# 구버전이 있는 폴더의 경로 
        shutil.rmtree(path) 					# 그 경로 삭제

    if not chrome_ver in current_list: 				# 최신버전 폴더가 현재 경로에 없으면
        AutoChrome.install(True) 				# 크롬드라이버 설치
    else : pass 						# 아니면 무시


def selenium_test():
    chrome_ver = AutoChrome.get_chrome_version().split('.')[0] # 최신 드라이버가 들어있는 폴더명
    path = os.path.join(os.getcwd(),chrome_ver)
    path = os.path.join(path,'chromedriver.exe')
    print(path)
    URL = 'https://www.koreanair.com/kr/ko'
    driver = webdriver.Chrome(str(path))
    driver.get(url=URL)
    
    while(True):
        pass

# Selenium 
options = Options()
#지정한 user-agent로 설정합니다.
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
options.add_argument('user-agent=' + user_agent)

options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
# options.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
# options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
# options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
# options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
# options.add_argument('--mute-audio') #브라우저에 음소거 옵션을 적용합니다.
# options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.

# 1. 대한항공 이동
browser = webdriver.Chrome()
browser.get("https://www.koreanair.com/booking/select-flight/departure")
time.sleep(4)

# 2. 도착지 선택
destination_btn_XPATH = '/html/body/app-root/div/ke-search/ke-basic-layout/div[1]/div/div[1]/div/div[2]/div/ke-search-ow-rt/div[1]/div[1]/div/div/div[1]/ke-airport-selector/div/button[2]'
destination_btn = browser.find_element(By.XPATH, destination_btn_XPATH)
destination_btn.click()

# 3. 도착지 입력
destination_name = browser.find_element(By.CLASS_NAME, 'auto-search__text')
destination_name.send_keys("멜버른")
destination_name.send_keys(Keys.ENTER)

# 4. 편도로 선택
one_way_btn = browser.find_elements(By.CLASS_NAME, 'selection')
one_way_btn[1].click()

# 5. 날짜 선택
date_btn = browser.find_element(By.CLASS_NAME, 'booking-new__datepicker')
date_btn.click()
flight_date = browser.find_elements(By.XPATH, "//span[text()='14']")
flight_date[4].click()
confirm_btn = browser.find_element(By.CLASS_NAME, 'dialog__buttons-area')
confirm_btn.click()

# 6. 항공편 검색 
confirm_btn2 = browser.find_element(By.CLASS_NAME, 'booking-new__search')
confirm_btn2.click()
# browser.implicitly_wait(10)
time.sleep(6)

html = browser.page_source
# print(html)

# 데이터 가져오기 & bs4
import requests
from bs4 import BeautifulSoup

# headers = {"User-Agent": "자신의 user-agent 입력"}
# res = requests.get(url, headers=headers)
# res.raise_for_status() # 혹여나 문제 발생시 오류를 보여주고 프로그램 종료

# # 응답 코드 확인 (정보를 잘 받아 왔는지 또는 접근 권한, 서버 문제 등을 확인하기 위함) - User Agent 참고
# # 200 이면 정상, 403이면 접근 권한이 없음. (웹 스크래핑 어려움)
# if res.status_code == requests.codes.ok:
#     print("정상. [응답코드 ", res.status_code, "]")
# else:
#     print("문제 발생. [에러코드 ", res.status_code, "]")

# 가져온 html문서를 lxml parser를 통해서 BeautifulSoup 객체로 만듬
soup = BeautifulSoup(html, "html.parser") # html.parser

# flight_time = soup.find_all("span", attrs={"class":"flight__time"})
# print(flight_time)

# for FT in flight_time:
#     for ft in FT:
#         print(ft)

<<<<<<< HEAD
# filename = "항공권.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="") # 무의미하게 중간 중간 줄바꿈을 해버림. 그래서 newline=""을 해주면 이는 해결된다.
# writer = csv.writer(f) 

# title = "도착 시간  출발 시간".split("\t")
# print(type(title))
# writer.writerow(title)

# data_rows =  soup.find("ul", attrs={"class":"flight__items"}).find("li").find_all("div")
# for row in data_rows:
#     columns = row.find_all("span")
#     if len(columns) <= 1: # 의미 없는 데이터는 skip
#         continue 
#     data = [column.get_text().strip() for column in columns] # strip()를 통해 불필요한 공백을 제거
#     print(data)
#     writer.writerow(data) # 데이터는 리스트 형태로 넣어줘야함.


date = 14
transfer_list = []
data_dic = {'date' : [],
            'time1' : [],
            'time2' : [],
            'duration' : [],
            'transfer' : [],
            'flight_number1' : [],
            'flight_number2' : [],
            'price' : []}
# features = ['date', 'time1', 'time2', 'duration', 'transfer', 'flight_number1', 'flight_number2', 'price']



if browser.current_url == "https://www.koreanair.com/booking/select-flight/departure":
    flight_date = date
    flight_time = browser.find_elements(By.CLASS_NAME, "flight__time")
    flight_duration = browser.find_elements(By.CLASS_NAME, "flight__duration")
    flight_transfer = browser.find_elements(By.CLASS_NAME, "flight__stop")
    flight_number = browser.find_elements(By.CLASS_NAME, "flight__number")
    flight_fares = browser.find_elements(By.CLASS_NAME, "flight__fare")
    

    for i in range(len(flight_fares)):
        data_dic['date'].append(flight_date)
        data_dic['duration'].append(flight_duration[i].text)
        data_dic['transfer'].append(flight_transfer[i].text)
        data_dic['price'].append(flight_fares[i].text)
    
    for i in range(0,len(flight_time), 2):
        data_dic['time1'].append(flight_time[i].text)
        data_dic['time2'].append(flight_time[i+1].text)
        data_dic['flight_number1'].append(flight_number[i].text)
        data_dic['flight_number2'].append(flight_number[i+1].text)

i = 1
while i != len(flight_fares)+1:
    try:
        flight_transfer = browser.find_element(By.XPATH, "/html/body/app-root/div/ke-selection-flight/ke-basic-layout/div[1]/div/div[2]/div[2]/ke-air-offer-bounds-cont/ke-air-offer-bounds-pres/div/div[2]/ul/li[{}]/div[1]/a/div[1]/div/div[3]/div[1]/ke-flight-desc-item/span[3]".format(i))
        # print(flight_transfer) 
        transfer_list.append("O")
        i += 1 
    except:
        transfer_list.append("X")
        i += 1
print(transfer_list)

print(data_dic)
=======
filename = "항공권.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # 무의미하게 중간 중간 줄바꿈을 해버림. 그래서 newline=""을 해주면 이는 해결된다.
writer = csv.writer(f) 

title = "최/고값	출발시각	출발시간	출발지	출발지	도착시각	도착시각	도착시각	걸리는날짜	도착지  도착지  소요시간  소요시간  경유  경유  항공기이름  뭐야  항공기이름  항공기이름2  최/고운임  최저금액  최/고  금액  오잉".split("\t")
print(type(title))
writer.writerow(title)

data_rows =  soup.find("ul", attrs={"class":"flight__items"}).find("li").find_all("div")
for row in data_rows:
    columns = row.find_all("span")
    if len(columns) <= 1: # 의미 없는 데이터는 skip
        continue 
    data = [column.get_text().strip() for column in columns] # strip()를 통해 불필요한 공백을 제거
    print(data)
    writer.writerow(data) # 데이터는 리스트 형태로 넣어줘야함.

# date = 14
# data_dic = {'date' : [],
#             'time1' : [],
#             'time2' : [],
#             'duration' : [],
#             'transfer' : [],
#             'flight_number1' : [],
#             'flight_number2' : [],
#             'price' : []}
# features = ['date', 'time1', 'time2', 'duration', 'transfer', 'flight_number1', 'flight_number2', 'price']

# if browser.current_url == "https://www.koreanair.com/booking/select-flight/departure":
#     flight_date = date
#     flight_time = browser.find_elements(By.CLASS_NAME, "flight__time")
#     flight_duration = browser.find_elements(By.CLASS_NAME, "flight__duration")
#     flight_transfer = browser.find_elements(By.CLASS_NAME, "flight__stop")
#     flight_number = browser.find_elements(By.CLASS_NAME, "flight__number")
#     flight_fares = browser.find_elements(By.CLASS_NAME, "flight__fare")
    
#     for i in range(len(flight_fares)):
#         data_dic['date'].append(flight_date)
#         data_dic['duration'].append(flight_duration[i].text)
#         data_dic['transfer'].append(flight_transfer[i].text)
#         data_dic['price'].append(flight_fares[i].text)
    
#     for i in range(0,len(flight_time), 2):
#         data_dic['time1'].append(flight_time[i].text)
#         data_dic['time2'].append(flight_time[i+1].text)
#         data_dic['flight_number1'].append(flight_number[i].text)
#         data_dic['flight_number2'].append(flight_number[i+1].text)

# print(data_dic)
>>>>>>> 85cb9cefa026dc990cf84fc1700b1ab0ca91288d

# import pandas as pd
# data_df = pd.DataFrame(data_dic)
# data_df.to_excel("3.xlsx")