n=int(input())
s=0
l=list(map(int,input().split()))
for i in l:
        s=s+i
r=float(s/n)
print("%.2f"%r)        