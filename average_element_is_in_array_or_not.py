n=int(input())
s=0
l=list(map(int,input().split()))
for i in l:
    s=s+int(i)
r=int(s/n)
if r in l:
    print(True)
else:
    print(False)