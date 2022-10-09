class Discount:
    def __init__(self,total,halin):
        self.total=total
        self.halin=halin
    def last(self):
        return self.total - ((self.total*self.halin)/100)
total=int(input("원가를 입력하세요. : "))
halin=int(input("몇 퍼센트(%)할인하나요? :"))
discount=Discount(total,halin)
print("최종 금액은",discount.last(),"입니다.")
