print("            <8월 달력>")
print(" 일   월   화   수   목   금   토")
print("    ",end='')
for i in range(1,32):
    if i%7==0:
        print("\n")
    print("%3d"%(i),end="  ")