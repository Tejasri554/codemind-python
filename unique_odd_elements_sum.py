n=int(input())
l=list(map(int,input().split()))
s=[]
odd=0
for i in l:
    if i not in s:
        s.append(i)
for i in s:
    if i%2!=0:
        odd=odd+i
print(odd)        