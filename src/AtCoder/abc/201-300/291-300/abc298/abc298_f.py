from collections import deque
N = int(input())
R_dict = dict()
C_dict = dict()
inp_dict = dict()

for i in range(N):
    r, c, x = map(int, input().split())
    inp_dict[(r, c)] = x
    if r not in R_dict:
        R_dict[r] = x
    else:
        R_dict[r] += x
    if c not in C_dict:
        C_dict[c] = x
    else:
        C_dict[c] += x
R_dict[-1] = -10 ** 18
C_dict[-1] = -10 ** 18
ans = 0
sorted_R = sorted(R_dict.items(), key=lambda x: x[1], reverse=True)
sorted_C = sorted(C_dict.items(), key=lambda x: x[1], reverse=True)
queue = deque([(0, 0)])
while queue:
    R_counter, C_counter = queue.popleft()
    if (sorted_R[R_counter][1] + sorted_C[C_counter][1] > ans):
        if (sorted_R[R_counter][0], sorted_C[C_counter][0]) in inp_dict:
            ans = max(ans, sorted_R[R_counter][1] + sorted_C[C_counter][1] - inp_dict[(sorted_R[R_counter][0], sorted_C[C_counter][0])])
        else:
            ans = max(ans, sorted_R[R_counter][1] + sorted_C[C_counter][1])
        if R_counter != N:
            queue.append((R_counter + 1, C_counter))
        if C_counter != N:
            queue.append((R_counter, C_counter + 1))
print(ans)
