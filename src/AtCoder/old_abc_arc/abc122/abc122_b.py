S = input()
ans = 0
streak = 0
for i in range(len(S)):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        streak += 1
    else:
        if ans < streak:
            ans = streak
        streak = 0
if ans < streak:
    ans = streak
print(ans)
