from pymongo import MongoClient
import scrapy
import transform


def connect(dataBaseName, collectionName):
    client = MongoClient()
    db = client.get_database('Scrapy')
    collection = db.get_collection('Train')

    return collection


if __name__ == '__main__':

    url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime'
    data = {
        '_csrf': '3baae0b6-f9b8-4dda-ab63-268d47e0b8d5',
        'startStation': '2200-大甲',
        'endStation': '3300-臺中',
        'transfer': 'ONE',
        'rideDate': '2020/04/15',
        'startOrEndTime': 'true',
        'startTime': '00:00',
        'endTime': '23:59',
        'trainTypeList': 'ALL',
        'query': '查詢'
    }
    
    tool = scrapy.Scrapy(url, data)
    info = tool.getData()
    pipeline = transform.TransForm(info)
    data_many_dict = pipeline.convert()

    con = connect('Scrapy', 'Train')
    con.insert_many(data_many_dict)