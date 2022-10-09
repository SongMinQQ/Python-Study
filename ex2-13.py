def find_max(a):
    max=0
    for i in range(1,len(a)):
        if a[i] > max:
            max=a[i]
    return max
num_list=[10,7,5,11,4,1,90]
print(find_max(num_list))