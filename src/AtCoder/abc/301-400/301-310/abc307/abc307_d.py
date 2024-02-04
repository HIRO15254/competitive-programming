from collections import deque

N = int(input())
S = input()
ans = deque()
ans.append("")

for i in range(N):
    if S[i] == "(":
        ans.append("(")
    elif S[i] == ")" and len(ans) > 1:
        ans.pop()
    else:
        pop = ans.pop()
        ans.append(pop + S[i])
while ans:
    print(ans.popleft(), end="")
print("")
