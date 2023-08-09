import json
from collections import OrderedDict

file_data = OrderedDict()

# 키와 값은 큰따옴표("")나 작은따옴표('') 중 아무거나 선택하여 표현할 수 있음
file_data["name"] = "Yucori"
file_data["living in"] = {"country": "Korea", "city": "Seoul"}
file_data["year"] = 2023

#print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
# 출력할 때는 json.dumps이지만 만들 때에는 json.dump를 사용함
# indent="\t"를 작성하지 않으면 json 파일이 한 줄로 출력됨

with open('./과제/230809_json.json', 'r') as f:
  json_data = json.load(f)
print(json.dumps(json_data, indent="\t"))

#with open('230809_json.json', 'w', encoding="utf-8") as make_file:
#  json.dump(file_data, make_file, ensure_ascii=False, indent="\t")