from re import I


num=input("각 숫자를 공백으로 구분하여 입력해 주세요 : ")
a=num.split()
num1=0
num2=0
for c in a:
    sum=0
    for d in c:
        sum+=int(d)
        if sum>num1:
            num1=sum
            num2=c
print(num2)