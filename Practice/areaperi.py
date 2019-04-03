l=int(input())
b=int(input())
p=2*l+2*b
a=l*b
if p>a:
    print('Peri')
    print(p)
elif a>p:
    print('Area')
    print(a)
else:
    print('Eq')
    print(p)
