N, A, B = map(int, input().rstrip().split(" "))
ans = int(N / (A + B)) * A
if N % (A + B) >= A:
    ans += A
else:
    ans += N % (A + B)
print(ans)
