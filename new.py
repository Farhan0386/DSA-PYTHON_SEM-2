a=(3,4,5,6,7,8,)
print(a)

b=a[0]
for i in range(len(a)):
    if a[i]<b:
        b=a[i]
        print(b)