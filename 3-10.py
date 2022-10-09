def bot(a):
    if a == 1:
        return '가위'
    elif a == 2:
        return '바위'
    else:
        return '보'
def human(a):
    if a == '가위':
        return 1
    if a == '바위':
        return 2
    if a == '보':
        return 3
def winner(a,b):
    return a - b
import random
a= random.randrange(1,4)
user=input("가위바위보 게임입니다. 무엇을 낼지 입력해 주세요. : ")
print("사용자: %s"%(user))
print("컴퓨터: %s"%(bot(a)))
h=human(user)
win=winner(h,a)
if win == 0:
    print("비겼습니다.")
elif (win == 1) or (win == -2):
    print("축하합니다. 당신이 이겼습니다.")
else:
    print("당신이 패배했습니다.")