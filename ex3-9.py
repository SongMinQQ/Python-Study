a=input()
b=len(a)
if b%2==0:
    c=b//2-1
    print(a[c:c+2])
else:
    c=b//2
    print(a[c])