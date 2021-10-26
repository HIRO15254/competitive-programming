S = list(input())
a = S.count('a')
b = S.count('b')
c = S.count('c')

if a > b and a > c:
    print("a")
elif b > c and b > a:
    print("b")
else:
    print("c")
