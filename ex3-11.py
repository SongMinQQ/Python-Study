movie={'미비포유','해리포터','맘마미아','어바웃타임','라라랜드'}
discount={"학생할인":3000,"지역할인":4000,"회원할인":5000}
price=12000
disprice=0
print('''=======영화  목록=======
미비포유
해리포터
맘마미아
어바웃타임
라라랜드
=========================''')
while True:
    select=input("예매할 영화를 선택해 주세요. : ")
    if select in movie:
        print("%s를 선택했습니다."%(select))
        break
    else:
        print("예매할 수 없는 영화입니다.")
while True:
    people=int(input("관람 인원수를 입력해 주세요. : "))
    if people<0:
        print("관람 인원수는 양수만 입력 가능합니다.")
    elif (people%1)>0:
        print("관람 인원수는 정수만 입력 가능합니다.")
    else:
        print("관람할 인원수는 %d명입니다."%(people))
        break
price=price * people
use=input("할인권을 사용하려면 y, 금액 확인으로 넘어가려면 n을 입력해 주세요. : ")
while True:
    if use == 'y':
        name=input("할인권 이름을 입력해 주세요. : ")
        if name in discount.keys():
            disprice=discount[name] * people
            print("할인이 적용되었습니다.")
            break
        else:
            print("존재하지 않는 할인권입니다.")
            name=input("할인권을 다시 입력하려면 y, 금액 확인으로 넘어가려면 n을 입력해 주세요. : ")
    if use == 'n':
        print("할인권을 사용하지 않았습니다.")
        break
total=price - disprice
print('''\n\n\n<예매 상세 내역>
=============================''')
print("영화 제목: %s"%(select))
print("관람 인원: %d명"%(people))
print("합계 금액: %d"%(price))
print("할인 금액: %d"%(disprice))
print("-----------------------------")
print("실 결제액: %d"%(total))
print("=============================")
