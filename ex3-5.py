word=[]
number=0
first_word=input()
word.append(first_word)
while True:
    words=input()
    if word[number][-1]!=words[0]:
        print("틀린 단어를 입력하셨습니다. 게임을 종료합니다.")
        break
    if words in word:
        print("앞에서 사용한 단어와 동일한 단어를 입력하셨습니다. 게임을 종료합니다.")
        break
    if ((number+1)%5)==4:
        print("(중간 점검) 현재 %d개의 단어를 입력하셨습니다."%(number+2))
    number+=1
    word.append(words)