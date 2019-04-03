import time
import datetime

T=int(input())
for i in range(7):
    n=int(input())
    for j in range(n):
        (t1, t2)=input().split(' ')
tsec=T*60*60
seconds = time.time(t1)
print(seconds)
