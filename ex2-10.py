numbers=[]
a=int(input("숫자를 입력해 주세요 : "))
b=int(input("몇 번째 약수를 알고 싶나요? : "))
for i in range(1,a+1):
    if (a%i==0):
        numbers.append(i)
if len(numbers)<b:
    print("입력한 숫자만큼의 약수가 존재하지 않습니다.")
else:
    print("%d의 %d번째 약수는 %d입니다."%(a,b,numbers[b-1]))