#영어 문장 대소문자 교정 프로그램
#조건 1: 문장은 마침표를 기준으로 구분 / 조건 2: 각 문장의 첫번째 글자와 '나'를 뜻하는 i는 반드시 대문자 / 조건 3:그 외의 글자는 전부 소문자여야함
sentence=input("문장을 입력해 주세요 : ")
sentence=sentence.lower()#조건 1, 3 
sentence=sentence.split('.')
last_sentence = []
for s in sentence:
    s=s.capitalize()#조건 2 첫 글자는 반드시 대문자로 출력해야 되는데 . 뒤에 문장 띄어쓰면 작동 안함
    if s in'i':
        s.replace('i','I')
        last_sentence.append(s)#s안에 있는 문자열 데이터를 last_sentence 리스트에 삽입하겠다
    elif s in'i':
        s.replace('i','I')
        last_sentence.append(s)
    elif s in'i':
        s.replace('i','I')
        last_sentence.append(s)
    elif s in'i':
        s.replace('i','I')
        last_sentence.append(s)
    else:
        last_sentence.append(s)
print('.'.join(last_sentence))
