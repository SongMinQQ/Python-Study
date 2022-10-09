word=[]
a=input("단어를 입력해 주세요. : ")
for i in word:
    word.append(i)
changeword=list(reversed(word))
if word == changeword:
    print("%s는 회문입니다."%(a))
else:
    print("%s는 회문이 아닙니다."%(a))