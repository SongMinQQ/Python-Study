def gugudan(a):
    for i in range(1,10):
        print("%d x %d = %d"%(a,i,a*i))

while True:
    a=int(input("2부터 9 사이 숫자를 입력해 주세요.(1을 누르면 프로그램이 종료됩니다.) "))
    if a==1:
        print("프로그램을 종료합니다.")
        break
    if 10>a>1:
        gugudan(a)
        print("\n")
    else:
        print("범위 외의 숫자입니다. 다시 시도하세요.")