numbers=[]
plus=0
for i in range(7):
    a=int(input("정수를 입력하세요 : "))
    numbers.append(a)
    plus=plus+a
print("평균 : %0.1f"%(plus/7))