N, A, B = map(int, input().rstrip().split(" "))
S = list(input())
rev = S[A - 1:B]
rev.reverse()
S[A - 1:B] = rev
print("".join(S))
