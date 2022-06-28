s=input()
n=''
c=0
for i in s:
    if i not in n:
        c+=1
        n=n+i
if c==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")