import json

data = '''
{
    "resultList": [
        {
            "B.Y.P.M.C": "651",
            "B.Y.P.M.P": "0.03",
            "gubun": "충청남도",
            "B.M.P.M.P": "-0.01",
            "woman": "1016516",
            "B.M.P.M.C": "-126",
            "humanCnt1": "2062273",
            "humanCnt2": "2063050",
            "humanCnt3": "2062924",
            "man": "1046408",
            "familyCnt": "873322"
        }
    ]
}
'''

# JSON 데이터 파싱
json_data = json.loads(data)

# "resultList"에서 첫 번째 요소 선택
result = json_data["resultList"][0]

# "gubun" 값 출력
gubun = result["gubun"]
print("구분:", gubun)
