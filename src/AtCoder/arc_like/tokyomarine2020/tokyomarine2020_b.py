A, V = map(int, input().rstrip().split(" "))
B, W = map(int, input().rstrip().split(" "))
T = int(input())
if(abs(A - B) <= (V - W) * T):
    print("YES")
else:
    print("NO")
