h=int(input("삼각형의 높이를 입력해 주세요 : "))

#for i in range(0,h):
    #for j in range(0,h-1-i):
        #print(" ",end='')
    #for k in range(0,i+1):
        #print("*",end='')
#print('')
for i in range(1,h+1):
    print(' '*(h-i)+"*"*i)
