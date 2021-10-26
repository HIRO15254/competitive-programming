A, B, C = map(int, input().split(" "))
p = 0
ans = 0
while p < C:
    ans += 1
    p += A
    if ans % 7 == 0:
        p += B
print(ans)
