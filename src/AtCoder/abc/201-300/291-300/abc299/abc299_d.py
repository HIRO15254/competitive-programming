N = int(input())
mi = 1
ma = N
while ma - mi > 1:
    mid = (mi + ma) // 2
    print("?", mid)
    ans = int(input())
    if ans == 0:
        mi = mid
    else:
        ma = mid
print("!", mi)
