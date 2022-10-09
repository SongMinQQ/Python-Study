i=int(input("숫자를 입력해 주세요 : "))
fact=1
for p in range(1,i+1):
    fact*=p
print("%d!은 %d입니다."%(i,fact))