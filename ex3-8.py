print("1. 10초  2. 30초  3. 1분  4. 10분  5. 시작")
time=0
i=0
while True:
    i=int(input("원하는 버튼의 숫자를 입력해 주세요. : "))
    if i==5:
        print("\n전자레인지를 작동합니다.")
        break#i변수에 5의 값이 들어오면 무한루프 탈출
    if i==1:
        time+=10
    elif i==2:
        time+=30
    elif i==3:
        time+=60
    elif i==4:
        time+=600
    else:
        print("잘못된 입력입니다.")
    change_time=0
    if time>=60:
        change_time=time//60
        print(str(change_time)+':'+"%02d"%(time%60))#60초 이상이 될 경우 분:초 형식으로 변환 출력
    if time<60:
        print("00:"+str(time))#60초 미만일 경우에는 앞의 분은 00:으로 고정 후 뒤에 초만 출력
