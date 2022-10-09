n=int(input("숫자를 입력해 주세요 : "))
d=2
while d<=n:
    if n%d==0:
        print(d,end=" ")
        n= n//d
    else:
        d=d+1