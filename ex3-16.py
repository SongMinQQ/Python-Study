total=0
yoil=''
month_last=['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
last=list(map(int,month_last))
month=int(input("월: "))
day=int(input("일: "))
for i in range(month-1):
    total=total+last[i]
total=total+day
if total%7==0:
    yoil='금'
if total%7==1:
    yoil='토'
if total%7==2:
    yoil='일'
if total%7==3:
    yoil='월'
if total%7==4:
    yoil='화'
if total%7==5:
    yoil='수'
if total%7==6:
    yoil='목'
print("2022년 %d월 %d일은 %s요일입니다."%(month,day,yoil))