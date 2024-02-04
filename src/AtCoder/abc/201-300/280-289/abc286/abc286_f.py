mod = [4, 5, 7, 9, 11, 13, 17, 19, 23]
print(sum(mod))
A = []
counter = 0
for i in mod:
    for j in range(2, i + 1):
        A.append(counter + j)
    A.append(counter + 1)
    counter += i
print(" ".join(map(str, A)))
B = list(map(int, input().split()))
counter = 0
mod_ans = []
for i in mod:
    mod_ans.append(B[counter] - counter - 1)
    counter += i
now = mod_ans[0]
mod_now = mod[0]
for i in range(1, len(mod)):
    while now % mod[i] != mod_ans[i]:
        now += mod_now
    mod_now *= mod[i]
    now %= mod_now
print(now)
