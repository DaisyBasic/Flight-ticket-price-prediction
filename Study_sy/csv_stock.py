import csv
from urllib import request
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # 무의미하게 중간 중간 줄바꿈을 해버림. 그래서 newline=""을 해주면 이는 해결된다.
writer = csv.writer(f) 

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", ... ] 뭐 이런 식으로 넣어진다.
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows =  soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue 
        data = [column.get_text().strip() for column in columns] # strip()를 통해 불필요한 공백을 제거
        # print(data)
        writer.writerow(data) # 데이터는 리스트 형태로 넣어줘야함.
