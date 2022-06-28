n=input()
x=n.split()
c=0
for i in x:
    for j in i:
        if j==' ':
            continue
        else:
            c+=1
print(c)            