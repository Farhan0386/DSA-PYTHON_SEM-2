a=[3,2,4,2,3]
b=[3,2,4,2,3]

i=0
j=len(a)-1

while i<j :
     a[i],a[j]=a[j],a[i]
     i+=1
     j-=1

if a==b:
    print(f" array {a} is palindrome")
else :
    print(f" array {a} is not palindrome")