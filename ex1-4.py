#필요한 화폐 개수를 알려주는 프로그램
money=int(input("물건값을 입력하세요(1만원 이하):"))
hundred=money%1000
ten=hundred%100
print(money," 원을 계산하려면")
print("1000원 지폐 ",int(money/1000),"장")
print("100원 동전",int(hundred/100),"개")
print("10원 동전",int(ten/10),"개")