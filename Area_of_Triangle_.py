a,b,c=map(int,input().split())
s=(a+b+c)/2
import math
area=float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("%.2f"%area)