def show_all_name(json_student):
    print("모든 학생들의 이름 정보 :")
    for i in range(0,len(json_student)):
        print(json_student[i]["username"])

def show_under_twenty(json_student):
    print("20살 미만 학생 정보 출력 : ")
    for i in range(0,len(json_student)): # 20살 미만 이름정보 출력
        if(json_student[i]["age"]< 20 ):
             print(json_student[i]["username"])

def student_reg(json_student,json_interest,json_purpose):
    while(1):
        print("다음 추가할 학생 정보를 입력하세요 : ")
        nameid = input("nameid : ")
        if(nameid == ""): #공백정보
            print("아이디가 없습니다 다시입력하세요")
            continue
        password = input("password : ")
        age = int(input("age : "))
        username = input("username : ")
        interest = input("interest : ")
        purpose = input("purpose : ")
        break
    json_student.append({"userno" : str(len(json_student)+1) , "nameid" : nameid , "password" : password, "age" : age, "username" : username})
    json_interest.append({"userno" : str(len(json_interest)+1) , "interest" : interest})
    json_purpose.append({"userno" : str(len(json_purpose)+1) , "purpose" : purpose})
    print("성공적으로 회원등록 되었습니다.")