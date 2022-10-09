#시간 변환 계산기
time=int(input("시간(초)을 입력해 주세요:"))
calculate_minute=time%3600
calculate_second=calculate_minute%60
if time>=86400:
    print(time,"초 =",int(time/86400),"일",int(time/3600),"시간",int(calculate_minute/60),"분",int(calculate_second%60),"초")
if 3600<=time>=60:
    print(time,"초 =",int(time/3600),"시간",int(calculate_minute/60),"분",int(calculate_second%60),"초")
if 61>=time>=60:
    print(time,"초 =",int(calculate_minute/60),"분",int(calculate_second%60),"초")