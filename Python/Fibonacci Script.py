fValue = int(input("How many sequences:"))
f1 = 0
f2 = 1
count = 0
while fValue > count:
    print(f1,end='  ,  ')
    fs = f1 + f2
    f1 = f2
    f2 = fs
    count += 1


