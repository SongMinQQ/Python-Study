i=int(input("정수를 입력하세요 : "))
def plus(i):
    ls=0
    for su in range(i+1):
        ls += su
    return ls
result=plus(i)
print("0부터",i,"까지의 합계는",result,"입니다.")