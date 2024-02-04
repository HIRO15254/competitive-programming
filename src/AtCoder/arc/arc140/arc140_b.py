from collections import deque

N = int(input())
S = list(input()) + ["E"]
lev = []
a_counter = 0
r_checker = False
c_counter = 0

for i in range(N + 1):
    if S[i] == "A" and not r_checker:
        a_counter += 1
    elif S[i] == "R" and a_counter != 0 and not r_checker:
        r_checker = True
    elif S[i] == "C" and r_checker:
        c_counter += 1
    else:
        if c_counter != 0:
            lev.append(min(a_counter, c_counter))
        a_counter = 1 if S[i] == "A" else 0
        r_checker = False
        c_counter = 0

lev.sort()
levs = deque(lev)
ans = 0
while levs:
    if ans % 2 == 0:
        q = levs.pop()
        q -= 1
        if q > 1:
            levs.append(q)
        elif q == 1:
            levs.appendleft(q)
    else:
        levs.popleft()
    ans += 1
print(ans)
