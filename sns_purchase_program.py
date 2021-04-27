member_list=[]
timeline_list = []
loginid=''
purchase_num=0
purchase_product=[]

class Member:
    #멤버값 초기화
    def __init__(self,name,id,password,profile_info,purchase_num,purchase_product):
        self.name=name
        self.id=id
        self.password=password
        self.profile_info=profile_info
        self.purchase_num=purchase_num
        self.purchase_product=purchase_product

    #멤버 정보 보여주기
    def show_member_info(self):
        print("이름: ", self.name)
        print("이메일: ", self.id)
        print("프로필 설명: ", self.profile_info)
        print("구매 횟수: ",self.purchase_num)

    def add_purchase(self,product_name):
        self.purchase_product.append(product_name)
        self.purchase_num+=1


#회원정보입력
def input_member_info():
    name=input('이름: ')
    id=input('이메일: ')
    if member_list !=[]: #멤버가 있을 때만 아이디 중복 확인
        for i in range(len(member_list)):
            if id==member_list[i].id: #이미 존재하는 아이디인 경우
                print('ERROR:이미 존재하는 아이디입니다.')
                return input_member_info()
    password=input('비밀번호: ')
    profile_info=input('프로필설명: ')
    member = Member(name, id, password, profile_info,purchase_num,purchase_product)
    print('\n')
    print(name , "님 회원가입이 완료되었습니다. \n")
    return member

#회원가입
def create_member():
    print('\n회원 정보를 입력하세요\n')
    member=input_member_info() #회원정보입력으로 객체 생성
    member_list.append(member) #생성된 객체를 member_list에 추가
    print('\n*회원가입정보 확인* ')
    member.show_member_info()

#회원정보 업데이트
def update_member_info():
    print('ATTENTION:정보를 수정하면 이전에 작성한 글을 삭제할 수 없습니다')
    ask_pw=input('본인 확인을 위해 비밀번호를 입력해주세요: ')
    for i in range(len(member_list)):
        if member_list[i].id==loginid: #로그인한 아이디의 비밀번호와 입력한 비밀번호가 일치한지 확인
            if member_list[i].password==ask_pw:
                print('\n회원정보 수정을 위해 정보를 입력해주세요')
                name = input("이름: ")
                id = input("아이디: ")
                password = input("비밀번호: ")
                info = input("프로필 설명: ")
                member = Member(name, id, password, info,purchase_num,purchase_product) #입력받은 값으로 객체 생성
                return member #객체 리턴
            else:
                print('ERROR:비밀번호가 일치하지 않습니다\n')
                return update_member_info()

#구매 메소드
def add_purchase_product():
    product_name=input('구매하실 제품 이름을 입력해주세요: ')
    for i in range(len(member_list)):
        if member_list[i].id==loginid:
            member_list[i].add_purchase(product_name) #loginid가 있는 위치에 product_name을 저장
            print('\n구매해주셔서 감사합니다')

import datetime
#input_timeline,remove_timeline,add_good_response,input_message
class Timeline:
    #리뷰 타임라인 초기화
    def __init__(self,writer,product,posttitle,post,postpw,tag):
        self.writer=writer
        now=datetime.datetime.now()
        self.posttime='{0}년 {1}월 {2}일 {3}시 {4}분'.format(now.year,now.month,now.day,now.hour,now.minute)
        self.product=product
        self.posttitle=posttitle
        self.post=post
        self.postpw=postpw
        self.tag=tag

    like_num=0
    message=""
    message_num=0

    #좋아요 추가 메서드
    def add_like_response(self):
        self.like_num+=1
    #댓글 추가 메서드
    def add_message(self,message):
        self.message=self.message+'\n'+message
        self.message_num+=1

    #리뷰 타임라인 메서드
    def show_timeline(self):
        print('\n')
        print("게시자: ", self.writer,"\t게시일자 및 시간: ", self.posttime)
        print("구매 제품: ",self.product)
        print("제목: ", self.posttitle)
        print("내용: ", self.post)
        print("태그: ", self.tag)
        print("좋아요 수: ", self.like_num)
        print("댓글 수: ", self.message_num)
        print(self.message)
        print("\n----------------------------------")

#리뷰 타임라인 추가
def input_timeline():
    review_product=input('리뷰를 작성할 제품을 입력해주세요: ')
    buy=False
    for x in range(len(member_list)):
        if buy:
            break
        for y in range(len(purchase_product)):
            if member_list[x].purchase_product[y]==review_product:
                buy=True #review_product와 purchase_product에 저장된 제품이 일치하는 경우에만 리뷰를 작성할 수 있음
                break
        else:
            print('\nERROR:구매하지 않은 제품은 리뷰 작성을 할 수 없습니다.\n')
            return input_timeline()

    for i in range(len(member_list)):
        if member_list[i].id==loginid: #작성자는 이름으로 저장
            name=member_list[i].name
            product=review_product
            posttitle=input('제목: ')
            post=input('내용: ')
            postpw=input('비밀번호 입력: ')
            tag=input('태그 입력: ')
            for j in range(len(timeline_list)):
                if timeline_list[j].posttitle==posttitle: #제목이 중복되지 않게
                    print('ERROR:중복된 제목입니다. 다시 입력해주세요')
                    return input_timeline()
                else:
                    continue
            timeline=Timeline(name,product,posttitle,post,postpw,tag) #입력한 걸로 객체 생성해서 리스트에 추가
    return timeline


#리뷰 타임라인 삭제
def remove_timeline(loginid):
    remove_title=input('삭제할 글의 제목을 입력해주세요: ')
    remove_pw=input('삭제할 글의 비밀번호를 입력해주세요: ')
    while True:
        for i in range(len(timeline_list)):
            if timeline_list[i].posttitle==remove_title and timeline_list[i].postpw==remove_pw and timeline_list[i].writer==loginid:
                #리뷰 제목, 비밀번호, loginid가 모두 같아야 리뷰 삭제 가능
                del timeline_list[i]
                print('\n글이 삭제되었습니다\n')
                break
        return timeline_list


#좋아요 메소드
def add_good_response():
    title = input("좋아요 누를 리뷰의 제목: ")
    for i in range(len(timeline_list)):
        if timeline_list[i].posttitle==title:
            timeline_list[i].add_like_response()
            break

#댓글 입력 메소드
def add_message():
    title = input("댓글 작성할 리뷰의 제목: ")

    for i in range(len(timeline_list)):
        if timeline_list[i].posttitle==title:
            message = input("댓글 입력: ")
            for j in range(len(member_list)):
                if member_list[j].id==loginid:
                    timeline_list[i].add_message(member_list[j].name+":"+message)
                    break


#로그인 메뉴
def login():
    print("\n<로그인>")
    print('id는 입력하신 이메일입니다.')
    id=input('id: ')
    loginid=id #로그인한 id 저장
    pw=input("password: ") #입력한 id에 맞는 password인지 확인
    login_tf=False
    for i in range(len(member_list)):
        if member_list[i].id == id:
            if member_list[i].password == pw:
                login_tf=True
    if login_tf:
        return login_tf,loginid #main에서 받기 위해서
    else:
        print("\nERROR:아이디와 비밀번호가 일치하지 않습니다\n")
        return login()


#메인 메뉴 표시
def main_menu():
    print("\n<메인 메뉴>")
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 종료")
    print("----------------------------------")
    menu = input("메뉴를 선택하세요: ")
    if menu.isdigit():  #메뉴 선택은 숫자로만 가능
        if 1<=int(menu)<=3:
            return int(menu)
        elif int(menu) < 1 or int(menu) > 3:  #메뉴는 1~3까지의 숫자만 가능
            print('\nERROR:1부터 3까지의 숫자로 입력해주세요.\n')
    else:
        print("\nERROR:숫자로 입력해주세요\n")

#로그인 상태에서 실행 가능한 메뉴
def sub_menu():
    print("\n<리뷰 타임라인>")
    for j in range(len(timeline_list)-1,-1,-1): #최근 순서대로 순차적으로
        timeline_list[j].show_timeline()
    print("\n<실행 가능 메뉴>")
    print('1. 본인 회원정보 수정')
    print('2. 제품 구매')
    print('3. 제품리뷰 글 작성 및 게시')
    print('4. 본인이 작성한 리뷰 글 삭제')
    print('5. 리뷰 글에 좋아요 입력')
    print('6. 리뷰 글에 댓글 입력')
    print('7. 다른 회원 정보 열람')
    print("8. 로그아웃")
    print("----------------------------------\n")
    menu = input("메뉴를 선택하세요: ")
    if menu.isdigit():
        if 1<=int(menu)<=8:
            return int(menu)
        else:
            print('\nERROR:1부터 8까지의 숫자로 입력해주세요\n')
    else:
        print('\nERROR:숫자로 입력해주세요\n')


#Main
while True:
    #main_menu 실행
    menu=main_menu()
    if menu==1:
        create_member()

    elif menu==2:
        if member_list != []: #멤버가 있는 경우
            login_tf,loginid=login() #로그인 성공 여부와 loginid 가져오기
            if login_tf:
                print('\n')
                print(loginid,"님 환영합니다")
            #sub_menu 실행
                menu_num = sub_menu()
                while True:
                    if menu_num==1:
                        print('1. 본인 회원정보 수정\n')
                        member=update_member_info()
                        for i in range(len(member_list)):
                            if member_list[i].id==loginid:
                                #현재 로그인한 아이디의 정보 수정
                                member_list[i]=member
                                print('\n수정이 완료되었습니다\n')
                                print('*수정된 회원정보*')
                                member_list[i].show_member_info()
                                menu_num=sub_menu()
                    elif menu_num==2:
                        print('2. 제품 구매\n')
                        add_purchase_product()
                        menu_num=sub_menu()

                    elif menu_num==3:
                        print('3. 제품리뷰 글 작성 및 게시\n')

                        for i in range(len(member_list)):
                            if member_list[i].purchase_num==0:
                                print('\nERROR:구매 내역이 없습니다. 제품을 구매한 회원만 리뷰를 남길 수 있습니다.\n')
                                break
                            else:
                                timeline=input_timeline()
                                timeline_list.append(timeline)
                                print("작성이 완료되었습니다.\n")
                                break
                        menu_num=sub_menu()

                    elif menu_num==4:
                        print('4. 본인이 작성한 리뷰 글 삭제\n')
                        ask=input('정말 삭제하겠습니까? (y/n)')
                        if ask=='y':
                            timeline_list=remove_timeline(loginid)
                            menu_num=sub_menu()
                        elif ask=='n':
                            menu_num=sub_menu()
                        else:
                            print('(y/n) 중에 선택해주세요')

                    elif menu_num==5:
                        print('5. 리뷰 글에 좋아요 입력\n')
                        add_good_response()
                        menu_num=sub_menu()

                    elif menu_num==6:
                        print('6. 리뷰 글에 댓글 입력\n')
                        add_message()
                        menu_num=sub_menu()

                    elif menu_num==7:
                        print('7. 다른 회원 정보 열람\n')
                        select_name=input('열람할 회원 이름을 입력하세요: ')
                        for i in range(len(member_list)):
                            if select_name==member_list[i].name:
                                member_list[i].show_member_info()
                            menu_num=sub_menu()

                    elif menu_num==8:
                        print("8. 로그아웃\n")
                        ask=input('로그아웃 하시겠습니까? (y/n)')
                        if ask=='y':

                            print('\n정상적으로 로그아웃되었습니다\n')
                            break
                        elif ask=='n':
                            menu_num=sub_menu()
                        else:
                            print('(y/n) 중에 선택해주세요')

                    else:
                        print('\n메뉴를 다시 입력해주세요\n')
                        menu_num=sub_menu()
                        continue

        else: #멤버가 없는 경우 회원가입 먼저
            print("\n등록된 회원이 없습니다. 회원가입을 먼저 진행해주세요.\n")

    elif menu == 3:
        a = input("종료하시겠습니까? (y/n): ")
        if a == "y":
            print("\n종료되었습니다.\n")
            exit()
    else:
        print("\n메뉴 입력을 다시 해주세요.\n")
        continue
