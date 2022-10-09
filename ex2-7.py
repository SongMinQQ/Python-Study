print("""=====도형 목록=====
1.원
2.삼각형
3.직사각형
4.정사각형
===================""")
def circle(a):
    result1=a*a*3.14
    return result1
def triangle(a,b):
    result2=(a*b)/2
    return result2
def quadrangle(a,b):
    result3=a*b
    return result3
def square(a):
    result4=a*b
    return result4

i=int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해 주세요 : "))
if i==1:
    a=int(input("반지름을 입력해 주세요 : "))
    result1=circle(a)
    print(result1)
elif i==2:
    b=int(input("밑변을 입력해 주세요 : "))
    c=int(input("높이를 입력해 주세요 : "))
    result2=triangle(b,c)
    print(result2)
elif i==3:
    d=int(input("가로 길이를 입력해 주세요 : "))
    e=int(input("세로 길이를 입력해 주세요 : "))
    result3=quadrangle(d,e)
    print(result3)
elif i==4:
    f=int(input("한 변의 길이를 입력해 주세요 : "))
    result4=square(f)
    print(result4)