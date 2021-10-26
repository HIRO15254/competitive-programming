N = int(input())
ans = 0
for i in range(1, N + 1):
    k = i
    while k != 0:
        if k % 10 != 7:
            k = k // 10
        else:
            break
    else:
        k2 = i
        while k2 != 0:
            if k2 % 8 != 7:
                k2 = k2 // 8
            else:
                break
        else:
            ans += 1
print(ans)
