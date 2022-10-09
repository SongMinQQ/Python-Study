result=0
quiz=input("퀴즈 결과를 입력해 주세요.(예: OOXOXXO): ").split('X')
for i in quiz:
    for j in range(0,len(i)+1):
        result = result+j
print(result)