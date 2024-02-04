S = [0] + list(map(int, input().split()))
ans = True
for i in range(8):
    if S[i] <= S[i + 1] and 100 <= S[i + 1] and S[i] <= 675 and S[i] % 25 == 0:
        pass
    else:
        ans = False
if ans:
    print("Yes")
else:
    print("No")
