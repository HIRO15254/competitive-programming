from collections import deque
S = list(input())
R = False
S1 = ""
S2 = ""
S3 = ""
for i in S:
    if i == "R":
        R = not R
    else:
        if R:
            S1 += i
        else:
            S2 += i
if R:
    S3 = S2[::-1] + S1
else:
    S3 = S1[::-1] + S2
on_ans = [True] * len(S3)


q = deque()
for i in range(len(S3)):
    if len(q) == 0:
        q.append(i)
    else:
        j = q.pop()
        if S3[j] == S3[i]:
            on_ans[i] = False
            on_ans[j] = False
        else:
            q.append(j)
            q.append(i)
ans = ""

for i in range(len(S3)):
    if on_ans[i]:
        ans += S3[i]
print(ans)
