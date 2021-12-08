import requests
import xml.etree.ElementTree as elemTree
from bs4 import BeautifulSoup
import pprint
import json

gyeonggi_cityID_file=open("metadata/city/gyeonggi_cityID.json", "r", encoding="UTF-8")
gyeonggi_cityID = json.load(gyeonggi_cityID_file)

routenum = input("노선 번호 입력... ")
regionname = input("지역명 입력... ")
regionnum = gyeonggi_cityID[regionname]
param1 = {
    'serviceKey': "1234567890",
    'keyword': routenum
}
param2 = {
    'serviceKey': "1234567890",
    'areaId': regionnum,
    'keyword': routenum
}

url1 = "http://openapi.gbis.go.kr/ws/rest/busrouteservice"
url2 = "http://openapi.gbis.go.kr/ws/rest/busrouteservice/area"
url3 = "http://openapi.gbis.go.kr/ws/rest/busrouteservice/info"
res1 = requests.get(url1, params=param1)

tmpsoup = BeautifulSoup(res1.text, 'html.parser')

i=0

#print(soup.select('resultMessage')[0].text)
while True:
    try :
        routeID = tmpsoup.select("routeId")[i].text

        param3 = {
            'serviceKey': "1234567890",
            'routeId': routeID
        }

        res3 = requests.get(url3, params=param3)
        #pprint.pprint(res3.text)
        soup = BeautifulSoup(res3.text, 'html.parser')
        regionName = soup.select('regionName')[0].text
        routeName = soup.select('routeName')[0].text
        if regionname in regionName and routenum == routeName:
            companyName = soup.select('companyName')[0].text
            startStationName = soup.select('startStationName')[0].text
            endStationName = soup.select('endStationName')[0].text

            print(f"{regionName}을 통과하는 {routeName}번 버스에 대한 정보입니다.")
            print(f"{companyName}에서 운행하는 {routeName}번 버스는 {startStationName}에서 {endStationName}까지 운행합니다.")
        i+=1
    except:
        break
