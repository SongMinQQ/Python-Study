word=input("문장을 입력해 주세요. : ")
devide=word.split(" ")
devide=set(devide)
devide=list(devide)
devide.sort()#sort함수는 기본적으로 오름차순으로 정렬해준다. reverse=true를 괄호에 넣으면 내림차순이된다.
for i in devide:
    print(i,end=" ")