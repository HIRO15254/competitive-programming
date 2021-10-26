inp = input().rstrip().split(" ")
HP = int(inp[0])
N = int(inp[1])
inp = input().rstrip().split(" ")
for i in range(N):
    HP -= int(inp[i])
if HP <= 0:
    print("Yes")
else:
    print("No")
