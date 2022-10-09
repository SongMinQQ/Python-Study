class Calculate:
    def __init__(self,ga,se):
        self.ga=ga
        self.se=se
    def wide(self):
        return (self.ga * 2) + (self.se *2)
    def area(self):
        return self.ga * self.se
ga=int(input("가로: "))
se=int(input("세로: "))
calculate=Calculate(ga,se)
print("직사각형의 둘레는 %d이고, 넓이는 %d입니다."%(calculate.wide(),calculate.area()))