time=input("24시 기준의 시간을 입력해 주세요. : ")
a=time[0:2]
a=int(a)
if a>=12:
    b=a%12
    if a==12:
        print("변환 시간: %d%s PM"%(a,time[2:5]))
    else:
        print("변환 시간: %d%s PM"%(b,time[2:5]))
else:
    print("변환 시간: %d%s AM"%(a,time[2:5]))