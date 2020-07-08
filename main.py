import json
import sub

student_group = dict()
with open("C:\\Users\\sejun\\Testvs\\students_info.json",encoding ="UTF8")as json_file:
    json_data = json.load(json_file)

    json_student=json_data["students"]
    json_interest = json_data["interest"]
    json_purpose = json_data["purpose"]

    sub.show_all_name(json_student) # 모든 학생 이름 정보 출력

    sub.student_reg(json_student,json_interest,json_purpose)

    sub.show_under_twenty(json_student)


with open("C:\\Users\\sejun\\Testvs\\students_info.json",'w',encoding ="UTF8")as json_rewrite:
    json.dump(json_data,json_rewrite,ensure_ascii=False,indent="\t")
