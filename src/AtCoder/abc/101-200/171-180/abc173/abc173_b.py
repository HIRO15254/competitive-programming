ans = [0, 0, 0, 0]
N = int(input())
for i in range(N):
    S = input()
    if S == "AC":
        ans[0] += 1
    if S == "WA":
        ans[1] += 1
    if S == "TLE":
        ans[2] += 1
    if S == "RE":
        ans[3] += 1
print("AC x " + str(ans[0]))
print("WA x " + str(ans[1]))
print("TLE x " + str(ans[2]))
print("RE x " + str(ans[3]))
