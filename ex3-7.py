menu={"물":[700,1],"콜라":[1000,3],"사이다":[1000,0],"과일 주스":[1000,4]}
price=0
print('''=======음료수 목록=======
물              700원
콜라           1000원
사이다         1000원
과일 주스       800원
=========================''')
total=int(input("자판기에 넣을 금액을 입력해 주세요. : "))
select=input("마시고 싶은 음료를 입력해 주세요. : ")
if select in menu:
    if menu[select][1]==0:
        print("품절입니다.")
    price=menu[select][0]
    if total>price:
        print("%s의 가격은 %d원입니다.\n주문이 완료되었습니다."%(select,price))
        print("잔액은 %d원입니다."%(total-price))
    else:
        print("액수가 부족합니다.")
else:
    print("존재하지 않는 메뉴입니다.")