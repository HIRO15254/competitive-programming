S = list(input())
N = int(input())
now = 0
ques = []

now_2 = 1
for i in range(len(S)):
    if S[len(S) - i - 1] == "1":
        now += now_2
    elif S[len(S) - i - 1] == "?":
        ques.append(now_2)
    now_2 *= 2
ques.sort(reverse=True)

if now > N:
    print(-1)
    exit()

for i in ques:
    if now + i <= N:
        now += i
print(now)
