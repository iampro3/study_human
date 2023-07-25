# 콘솔창에 pip install xmltodict 
#입력하기xmltodict
import requests, xmltodict, json

# mxml을 json으로 변환하기
key="URJUZFjggq5yt19sh7Du6Fp0X0SzscOj6Zo0TeNcVlsvFYc%2FbojdKw3wpMISPhs5zNw%2FTaAnabSPgUVIKJng8w%3D%3D"
url="http://apis.data.go.kr/B551182/nonPaymentDamtInfoService/getNonPaymentItemCodeList?pageNo=1&numOfRows=10&ServiceKey={}".format(key)

content = requests.get(url).content
dict =xmltodict.parse(content)
jsonString=json.dumps(dict['response']['body'],ensure_ascii=False)
jsonObj = json.loads(jsonString)


#print(len(jsonObj['items']))
for item in jsonObj['items']['item']:
    print(item)
    #print(item['divCd1Nm'])