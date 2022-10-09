def change(c):
    c=list(str(c))
    c.reverse()
    xc=''.join(c)
    return int(xc)
def sosu(c):
    for i in range(2,c+1):
        result=True
        for j in range(2,i):
            if i%j==0:
                result=False
                break
    return result
num_list=[]
calculate=2
a=int(input("입력받을 숫자의 개수를 입력해 주세요. : "))
for i in range(a):
    b=input("%d번째 숫자를 입력해 주세요. : "%(i+1))
    num_list.append(b)
for i in num_list:
    if sosu(change(i)):
        print(i,end=" ")