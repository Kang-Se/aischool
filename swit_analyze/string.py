# 파이썬 문자열, 리스트, 딕셔너리 다루기 마스터해보자

import json

dict = {}
max = 0
with open('./swit_chat.json', 'r',encoding="UTF8") as jsonfile:
    swit_chat_data = json.load(jsonfile)
    process_data = swit_chat_data["data"]
    for i in range(0,len(process_data)):
        if(process_data[i]["user_name"] in dict.keys()):
            new_dict = {process_data[i]["user_name"] : dict[process_data[i]["user_name"]] + 1}
            dict.update(new_dict)
        else:
            new_dict = {process_data[i]["user_name"] : 1}
            dict.update(new_dict)

for name,count in dict.items():
    if(max < count):
        max = count
        target_name = name
        target_count = count
print(f"가장 많이 쓴 사람 : {target_name} 횟수는 : {target_count}회")
# swit_chat_data 에 담긴 데이터는 실제 광주인공지능사관학교 스윗의 데이터이다.
# 문제 :
# 가장 많이 글을 쓴 채팅을 작성한 사람은 누구일까..?

# 힌트 ) 유저 별 content 수를 세서 누가 가장 많이썼을지 알아보기