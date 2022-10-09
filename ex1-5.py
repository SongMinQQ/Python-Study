birthday=int(input("생년월일을 입력해 주세요(8자리) : "))
year=birthday//10000
month=(birthday%10000)//100
day=birthday%100
print(year,"년",month,"월",day,"일 생이네요!")