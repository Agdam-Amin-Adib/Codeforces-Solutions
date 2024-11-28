x=int(input())
one=0
two=0
three=0
four=0
arr = list(map(int, input().split()))
for i in range (x):
    if arr[i]==1:
        one+=1
    elif arr[i]==2:
        two+=1
    elif arr[i]==3:
        three+=1
    elif arr[i]==4:
        four+=1
taxi = four
while(three>0 and one>0):
    three-=1
    one-=1
    taxi+=1
taxi+=three
while(one>1):
    two+=1
    one-=2
while(two>1):
    two-=2
    taxi+=1
if one==1 and two==1:
    taxi+=1
else :
    taxi=taxi+one+two
print(taxi)