import requests
from bs4 import BeautifulSoup

class Scrapy():
    def __init__(self, url, data):
        self.url = url
        self.data = data
    
    def getData(self):
        response = requests.post(self.url, self.data)
        soup = BeautifulSoup(response.text, "html.parser")

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

        return timeTable

    