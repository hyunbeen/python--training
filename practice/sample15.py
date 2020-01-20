import urllib.request
import json
from pprint import pprint

ServiceKey = "968a50ddc90f47c28437e5b81533888e"
url = "https://openapi.gg.go.kr/WtrArbrtmEntrncStus?Key=" + ServiceKey + "&Type=json&pIndex=1&pSize=2"
# print(dir(urllib))
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    dict = json.loads(response_body.decode('utf-8'))
    pprint(dict)
    WtrArbrtmEntrncStusList = list(dict.get('WtrArbrtmEntrncStus'))
    WtrArbrtmEntrncStusRow = WtrArbrtmEntrncStusList[1]
    
    WtrArbrtmEntrncStusDay = list(WtrArbrtmEntrncStusRow.get('row'))
    
    print(pprint(WtrArbrtmEntrncStusDay[0]))
    
    print(WtrArbrtmEntrncStusDay[0].get("DE"))
else:
    print("Error Code:" + rescode)