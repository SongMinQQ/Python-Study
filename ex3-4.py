num=input("숫자 두 개를 입력해 주세요(예: '3 5') ")
a=num.split()
b=list(map(int,a))
x=int(input("배수를 알고 싶은 숫자를 입력해 주세요. "))
for c in range(b[0],b[1]+1):
    result=0
    if c%x==0:
        result=c
        print(result,end=" ")