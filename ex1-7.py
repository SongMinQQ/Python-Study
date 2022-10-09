m=int(input("키를 입력하세요 : "))
kg=int(input("몸무게를 입력하세요 : "))
bmi=kg/(m*0.01*m*0.01)#cm을 m단위로 변환시켜 줘야함
if bmi>=25:
    print("bmi 지수가",bmi,"이므로 비만입니다.")
elif 25>bmi>=23:
    print("bmi 지수가",bmi,"이므로 과체중입니다.")
elif 23>bmi>=18.5:
    print("bmi 지수가",bmi,"이므로 정상 체중입니다.")
else:
    print("bmi 지수가",bmi,"이므로 저체중입니다.")