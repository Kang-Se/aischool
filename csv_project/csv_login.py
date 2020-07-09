import csv

#인원수 count
def call_cnt(path):
    cnt = 0
    f = open(path,"r")
    rdr = csv.reader(f)
    line = rdr
    for i in line:
        cnt +=1
    return cnt

#입력
def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw


def dic_user_input():
    dic = {}
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        dic["id"] = id
        dic["pw"] = pw
        return dic
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        dic["id"] = id
        dic["pw"] = pw
        return dic

#회원 가입
def reg_user(id,pw,path,count):
    f = open(path,"a",newline='')
    wr = csv.writer(f)
    wr.writerow([count,id,pw])
    f.close()

def dic_reg_user(dict,path,count):
    f = open(path,"a",newline='')
    wr = csv.writer(f)
    wr.writerow([count,dict["id"],dict["pw"]])
    f.close()



def lap_id(id,path):
    f = open(path,"r")
    rdr = csv.reader(f)
    line = rdr
    for nline in line:
        if(id == nline[1]):
            f.close()
            print("중복되는 아이디입니다.")
            return False
    f.close()
    print("사용 가능한 아이디입니다.")
    return True

def dic_lap_id(dict,path):
    f = open(path,"r")
    rdr = csv.reader(f)
    line = rdr
    for nline in line:
        if(dict["id"] == nline[1]):
            f.close()
            print("중복되는 아이디입니다.")
            return False
    f.close()
    print("사용 가능한 아이디입니다.")
    return True

def login(id,pw,path):
    f = open(path,"r")
    rdr = csv.reader(f)
    line = rdr
    for nline in line:
        if(id == nline[1]):
            if(pw == nline[2]):
                f.close()
                return print("로그인 성공")
            else:
                f.close()
                return print("패스워드가 잘못되었습니다")
    f.close()
    return print("id가 잘못되었습니다.")



def userlist(path):
    f = open(path,"r")
    rdr = csv.reader(f)
    line = rdr
    print("현재 존재하는 유저 :")
    for nline in line:
        print("==",nline[1],"==")

def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()


def start():
    print('csv 로 데이터 다루기 로그인 예제')
    path = "C:\\Users\\sejun\\ai_school_projects\\new.csv"
    count = call_cnt(path)
    lap_flag = False
    #info_dic = {}
    signup_or_login = int(input('1 - 로그인 / 2 - 회원가입 : \n'))

    if signup_or_login == 1:
        id, pw = user_input()
        login(id,pw,path)
        userlist(path)

    elif signup_or_login == 2:
        while(lap_flag == False):
            id, pw = user_input()
            lap_flag = lap_id(id,path)
            #info_dic = dic_user_input()
            #lap_flag = dic_lap_id(info_dic,path)
            
        reg_user(id,pw,path,count)
        #dic_reg_user(info_dic,path,count)
    exitcheck()


start()


