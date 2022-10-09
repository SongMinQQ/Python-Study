a=int(input("첫 번째 과목의 점수를 입력하세요 : "))
b=int(input("두 번째 과목의 점수를 입력하세요 : "))
c=int(input("세 번째 과목의 점수를 입력하세요 : "))
average=(a+b+c)/3
if ((a+b+c)/3)>=50:
    print("평균 점수는 "+ str(average) + "점으로 합격입니다.")
else:
    print("평균 점수는 "+ str((a+b+c)/3) + "점으로 불합격입니다.")