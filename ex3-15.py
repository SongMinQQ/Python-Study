number=[]
for i in range(5):
    num=int(input("숫자를 입력하세요. : "))
    number.append(num)
for i in range(5):
    for j in range(i,5):
        if number[i]>number[j]:
            result=number[i]
            number[i]=number[j]
            number[j]=result
print(number)