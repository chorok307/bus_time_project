import requests
import xml.etree.ElementTree as elemTree
from bs4 import BeautifulSoup
import pprint

routenum = input("노선 번호 입력... ")
regionnum = input("지역번호 입력... ")
bus_route_id = '100100070'
param1 = {
    'serviceKey': "1234567890",
    'keyword': str(routenum)
}
param2 = {
    'serviceKey': "1234567890",
    'areaId': regionnum,
    'keyword': routenum
}
url1 = "http://openapi.gbis.go.kr/ws/rest/busrouteservice"
url2 = "http://openapi.gbis.go.kr/ws/rest/busrouteservice/area"
res = requests.get(url2, params=param2)
pprint.pprint(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

i = 0
print(soup.select('queryTime')[0].text)
while soup.select('regionName')[0]:
    try :
        regionName = soup.select("regionName")[i].text
        routeName = soup.select('routename')[i].text
        if routeName == routenum:
            print(f"{routeName}번 버스는 {regionName}을 통과합니다.")
        i += 1
    except :
        break
