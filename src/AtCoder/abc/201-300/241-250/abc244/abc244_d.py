S = input().split(" ")
T = input().split(" ")
ans = 0
for i in range(3):
    ans += 1 if S[i] == T[i] else 0
if ans != 1:
    print("Yes")
else:
    print("No")