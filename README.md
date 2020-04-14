# 台鐵火車資訊查詢

## 為何做 (心路歷程)
作為學習爬蟲技術的一道較為簡單的題目，爬取靜態網頁，分析其中的tag，找尋想要的資訊  
主要功能:設定起始點、目的地、時間查詢所有符合的資料，並且整理資料上傳到資訊庫  
## 使用到的Libary
爬蟲:requests、bs4  
處理資料:pandas  
資料庫:pymongo  
## 程式分析
程式分為三個部分:爬蟲、處理資料、上傳資料庫 

*爬蟲的部分:
```
url = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime"
response = requests.post(url, data)
soup = BeautifulSoup(response.text, "html.parser")
``` 
使用post的方式帶著某些資料 (data)，就可以得到資料
data範例
``` 
data = {
        '_csrf': '3baae0b6-f9b8-4dda-ab63-268d47e0b8d5', 
        'startStation': '2200-大甲', #起始點
        'endStation': '3300-臺中', #目的地
        'transfer': 'ONE', #直達
        'rideDate': '2020/04/14', #日期
        'startOrEndTime': 'true', 
        'startTime': '00:00', #起始時間
        'endTime': '23:59', #到達時間
        'trainTypeList': 'ALL', 
        'query': '查詢'
    }
``` 

```
timeTable = []
count = []
# 名稱
result = soup.find('tbody').find('tr')
for i in result('th'):
    count.append(i.text.replace('\n', ''))
timeTable.append(count)

#search result
result = soup.find_all(class_="trip-column")
for i in result:
    count = []
    tds = i("td")
    for p in tds:
        count.append(p.text.replace('\n', ''))
    timeTable.append(count)
```
## 執行方式
