input_num = int(input())
N = list(map(int, input().rstrip().split(" ")))
ans = True
for i in range(input_num):
    if N[i] % 2 == 0:
        if N[i] % 3 != 0 and N[i] % 5 != 0:
            ans = False
if ans:
    print("APPROVED")
else:
    print("DENIED")
