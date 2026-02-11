import math
l1=[3,4,9,12,6,16,18,4,8]
ans=-math.inf

for i in range(len(l1)):
    if l1[i]>ans:
     ans=l1[i]
ans2=-math.inf
for b in range(len(l1)):
   if l1[b]>ans2 and l1[b]<ans:
     ans2=l1[b]

print(ans2)