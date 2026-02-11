a=[3,2,4,2,3]
i=0
j=len(a)
sum=0
while i<j :
    sum*=10
    sum+=a[i]
    i+=1
print(sum)

b=int(sum)
k=0
l=len(sum)-1
while k<l:
    b[k],b[l]=b[l],b[k]
print(b)
print("hello    world")
# if b==sum :
#     print(f"number {sum} is palindrome")
# else :
#    print(f"{sum} is not palidrome")