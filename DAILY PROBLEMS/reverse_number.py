a=[3,4,7,6,5,2]
i=0
j=len(a)-1
while i<j :
     a[i],a[j]=a[j],a[i]
     i+=1
     j-=1
     
print(a)



a=int(input("enter your number : "))

if a%2==0:
    print(f"your number a is even")
    
else :
    print(f"your number a is odd")